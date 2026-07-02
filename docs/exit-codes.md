# Exit codes

Codes follow the BSD `sysexits.h` convention. The source of truth is
`ExitCode` in [`src/gpresult_backend/errors.py`](../src/gpresult_backend/errors.py).

| Code | Name             | Meaning |
|------|------------------|---------|
| 0    | `OK`             | Success. Payload is on stdout. |
| 2    | —                | Command-line usage error (bad/missing argument). Emitted by `argparse`, not by `ExitCode`. |
| 65   | `DATA_ERROR`     | The policy database or its metadata is malformed and cannot be parsed. |
| 66   | `NO_INPUT`       | The policy database file does not exist. |
| 70   | `SOFTWARE_ERROR` | Internal error: JSON serialization failed, or an unexpected exception was caught. |
| 74   | `IO_ERROR`       | Other read failure, e.g. reading `/etc/os-release`, or a GLib read error other than missing-file / permission. |
| 77   | `NO_PERMISSION`  | Permission denied while reading the policy database. |