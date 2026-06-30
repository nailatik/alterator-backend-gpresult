# alterator-backend-gpresult

[![License](https://img.shields.io/badge/license-GPLv3-darkred.svg)](./LICENSE.md)
[![Language](https://img.shields.io/badge/language-Python-blue.svg)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/platform-ALTLinux-yellow.svg)](https://en.altlinux.org/ALT)

`alterator-backend-gpresult` exposes Group Policy results (`gpresult`) over D-Bus,
letting a domain administrator query the GPOs applied on **any** domain machine
without explicit SSH access. Authentication and authorization are handled by
[alterator-manager](https://altlinux.space/alterator/alterator-manager) and PolicyKit.

It reads the local GVDB policy database (`/etc/dconf/db/policy<UID>`), which is
populated by [`gpupdate`](https://github.com/altlinux/gpupdate), and serves it as
JSON over the [`gpresult1`](./docs/org.altlinux.alterator.gpresult1.md) D-Bus interface.

## Architecture

| Component | Path | Role |
|-----------|------|------|
| Python library | `src/gpresult_backend/` | Reads GVDB, builds GPO/KeyValue/Preference objects |
| Wrapper | `scripts/gpresult-wrapper` | CLI over the library; emits JSON to stdout |
| Backend config | `backend/gpresult.backend` | Maps D-Bus methods to wrapper commands (alterator-module-executor) |
| Interface | `interface/*.xml`, `*.policy` | D-Bus introspection + PolicyKit action |

### Data flow

```
admin machine ──(system D-Bus)──▶ alterator-manager ──PolicyKit (action "Read")──▶ gpresult-wrapper
                                                                                           │
                                                                        /etc/dconf/db/policy* (GVDB)
                                                                                           ▼
                                                                                          JSON
```

## D-Bus interface

- **Bus name:** `org.altlinux.alterator`
- **Object path:** `/org/altlinux/alterator/gpresult`
- **Interface:** `org.altlinux.alterator.gpresult1`

Every method returns the signature `asasi` — `stdout_strings` (the JSON document),
`stderr_strings`, and an integer `response` code.

| Method | In | JSON envelope |
|--------|----|---------------|
| `GetAllGPOs` | — | `{"all": [...]}` |
| `GetUserGPOs` | — | `{"user": [...]}` |
| `GetMachineGPOs` | — | `{"machine": [...]}` |
| `GetGPObyName` | `s` name | `{"user": [...], "machine": [...]}` |
| `GetGPObyGUID` | `s` guid | `{"user": [...], "machine": [...]}` |
| `GetOperationSystemName` | — | OS name from alterator-systeminfo (not GPO JSON) |

Full method/argument documentation: [docs/org.altlinux.alterator.gpresult1.md](./docs/org.altlinux.alterator.gpresult1.md).

## Installation

```bash
sudo apt-get install alterator-backend-gpresult
```

## Usage

All applied GPOs for the machine scope:

```bash
busctl --system call org.altlinux.alterator /org/altlinux/alterator/gpresult \
    org.altlinux.alterator.gpresult1 GetMachineGPOs
```

Look up a GPO by GUID (braces and letter case are optional):

```bash
busctl --system call org.altlinux.alterator /org/altlinux/alterator/gpresult \
    org.altlinux.alterator.gpresult1 GetGPObyGUID s '{3D925F92-80AD-4D95-BD94-CAE6987863F8}'
```

Look up a GPO by display name. Multi-word names **must** be quoted inside the
argument, otherwise the executor splits them on spaces:

```bash
busctl --system call org.altlinux.alterator /org/altlinux/alterator/gpresult \
    org.altlinux.alterator.gpresult1 GetGPObyName s '"Power policy"'
```

## Security

GPP password fields are replaced with `***REDACTED***` before output to prevent
credential leakage over the network (cf. MS14-025).

## License

[GPLv3+](./LICENSE.md)
