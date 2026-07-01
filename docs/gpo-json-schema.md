# GPO JSON payload schema

GPO data is returned over D-Bus as an array of JSON strings. This file documents
that payload; the transport contract is in
[`org.altlinux.alterator.gpresult1.md`](org.altlinux.alterator.gpresult1.md).

Notes:

- Any field may be `null` when absent in the policy database; only `guid`, `keys`,
  `preferences`, `type` and `attributes` are always present.
- Values are passed through verbatim from SYSVOL, so the values below are GPP
  conventions, not a closed enum enforced in code.
- The preference `password` field is always `"***REDACTED***"` when present.

## GPO object

Top-level object in each returned string.

| Field         | JSON type                 | Description / possible values |
|---------------|---------------------------|-------------------------------|
| `guid`        | string                    | GPO GUID as stored, e.g. `{31B2F340-016D-11D2-945F-00C04FB984F9}` (may be brace-wrapped). Lookups accept braced/unbraced and any case. |
| `name`        | string \| null            | GPO display name, e.g. `Default Domain Policy`. |
| `path`        | string \| null            | SYSVOL path of the GPO. |
| `version`     | integer \| string \| null | GPO version number. |
| `keys`        | array of [KeyValue](#keys-element) | Registry-style key/value entries, sorted by `key`. May be empty. |
| `preferences` | array of [Preference](#preferences-element) | Group Policy Preferences items. May be empty. |

## `keys[]` element

| Field            | JSON type                 | Description / possible values |
|------------------|---------------------------|-------------------------------|
| `key`            | string                    | Registry/dconf key path, e.g. `/software/...`. |
| `value`          | string \| integer         | Effective value of the key. |
| `previous_value` | string \| integer \| null | Value before the last policy reload; `null` if none. |
| `type`           | string \| null            | Declared data type of the value. |
| `is_list`        | boolean \| null           | Whether the value represents a list. |
| `reloaded`       | boolean \| null           | Reloaded together with the policy key (`reloaded_with_policy_key`). |

## `preferences[]` element

Each entry wraps a category tag and its attribute set.

| Field        | JSON type | Description / possible values |
|--------------|-----------|-------------------------------|
| `type`       | string    | Category: `Drives`, `Environmentvariables`, `Files`, `Folders`, `Inifiles`, `Networkshares`, `Shortcuts`. |
| `attributes` | object    | The common attributes below plus the per-category fields. |

The envelope `type` (category) is distinct from the `attributes.type` that
`Shortcuts` carries.

### Common attributes

Present in `attributes` for every category (from `BasePreference`).

| Field           | JSON type       | Description |
|-----------------|-----------------|-------------|
| `policy_name`   | string \| null  | Name of the owning GPO. |
| `disabled`      | boolean \| null | The item is disabled. |
| `remove_policy` | boolean \| null | Remove the item when the policy no longer applies. |
| `uid`           | string \| null  | GPP item UID. |
| `bypass_errors` | boolean \| null | Continue applying on error. |
| `apply_once`    | boolean \| null | Apply the item only once. |
| `changed`       | string \| null  | Last-changed timestamp. |
| `filters`       | any \| null     | Item-level targeting filters. |

### `Drives` — mapped network drives

| Field        | JSON type       | Description |
|--------------|-----------------|-------------|
| `action`     | string \| null  | GPP action: `Create` / `Replace` / `Update` / `Delete`. |
| `path`       | string \| null  | UNC path of the shared folder. |
| `dir`        | string \| null  | Drive letter / mount directory. |
| `label`      | string \| null  | Drive label. |
| `login`      | string \| null  | User name used to connect. |
| `password`   | string \| null  | Always `"***REDACTED***"` when present. |
| `persistent` | boolean \| null | Reconnect the drive at logon. |
| `useLetter`  | boolean \| null | Use the specified drive letter. |
| `thisDrive`  | string \| null  | Visibility of this drive. |
| `allDrives`  | string \| null  | Visibility of all drives. |

### `Environmentvariables` — environment variables

| Field   | JSON type      | Description |
|---------|----------------|-------------|
| `action`| string \| null | GPP action: `Create` / `Replace` / `Update` / `Delete`. |
| `name`  | string \| null | Variable name. |
| `value` | string \| null | Variable value. |

### `Files` — file operations

| Field        | JSON type       | Description |
|--------------|-----------------|-------------|
| `action`     | string \| null  | GPP action: `Create` / `Replace` / `Update` / `Delete`. |
| `fromPath`   | string \| null  | Source path. |
| `source`     | string \| null  | Source file. |
| `targetPath` | string \| null  | Destination path. |
| `readOnly`   | boolean \| null | Set the read-only attribute. |
| `archive`    | boolean \| null | Set the archive attribute. |
| `hidden`     | boolean \| null | Set the hidden attribute. |
| `suppress`   | boolean \| null | Suppress errors if the source does not exist. |
| `executable` | boolean \| null | Set the executable attribute. |

### `Folders` — folder operations

| Field               | JSON type       | Description |
|---------------------|-----------------|-------------|
| `action`            | string \| null  | GPP action: `Create` / `Replace` / `Update` / `Delete`. |
| `path`              | string \| null  | Folder path. |
| `delete_folder`     | boolean \| null | Delete the folder itself. |
| `delete_sub_folder` | boolean \| null | Delete sub-folders. |
| `delete_files`      | boolean \| null | Delete files inside the folder. |
| `hidden_folder`     | boolean \| null | Set the hidden attribute. |

### `Inifiles` — INI file settings

| Field      | JSON type      | Description |
|------------|----------------|-------------|
| `action`   | string \| null | GPP action: `Create` / `Replace` / `Update` / `Delete`. |
| `path`     | string \| null | Path to the `.ini` file. |
| `section`  | string \| null | INI section name. |
| `property` | string \| null | Property (key) name. |
| `value`    | string \| null | Property value. |

### `Networkshares` — network shares

| Field        | JSON type       | Description |
|--------------|-----------------|-------------|
| `action`     | string \| null  | GPP action: `Create` / `Replace` / `Update` / `Delete`. |
| `name`       | string \| null  | Share name. |
| `path`       | string \| null  | Path of the shared folder. |
| `comment`    | string \| null  | Share comment. |
| `allRegular` | boolean \| null | Re-share all regular shares. |
| `limitUsers` | string \| null  | User limit. |
| `abe`        | boolean \| null | Access-based enumeration. |

### `Shortcuts` — shortcuts

| Field                  | JSON type       | Description |
|------------------------|-----------------|-------------|
| `action`               | string \| null  | GPP action: `Create` / `Replace` / `Update` / `Delete`. |
| `name`                 | string \| null  | Shortcut name. |
| `path`                 | string \| null  | Location of the shortcut. |
| `dest`                 | string \| null  | Target the shortcut points to. |
| `expanded_path`        | string \| null  | Target path with variables expanded. |
| `arguments`            | string \| null  | Command-line arguments. |
| `icon`                 | string \| null  | Icon path/name. |
| `comment`              | string \| null  | Shortcut comment. |
| `type`                 | string \| null  | Shortcut type (distinct from the envelope `type`). |
| `changed`              | string \| null  | Last-changed timestamp (overrides the common `changed`). |
| `is_in_user_context`   | boolean \| null | Applied in the user context. |
| `desktop_file_template`| string \| null  | Template for the generated `.desktop` file. |
