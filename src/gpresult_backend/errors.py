# -*- coding: utf-8 -*-
"""Exit codes and error type shared by the backend and its CLI wrapper.

The wrapper is invoked by alterator-module-executor with ``exit_status = true``,
so the process exit code is returned to the client as the integer ``response``.
These codes let the client tell failure classes apart without parsing stderr.

Values follow the BSD ``sysexits.h`` convention (see /usr/include/sysexits.h).
"""

from enum import IntEnum


class ExitCode(IntEnum):
    OK = 0                # success
    DATA_ERROR = 65       # policy database / metadata is malformed (EX_DATAERR)
    NO_INPUT = 66         # policy database file does not exist (EX_NOINPUT)
    SOFTWARE_ERROR = 70   # internal error: serialization / unexpected (EX_SOFTWARE)
    IO_ERROR = 74         # other read failure, e.g. os-release (EX_IOERR)
    NO_PERMISSION = 77    # permission denied reading the database (EX_NOPERM)


class BackendError(Exception):
    """An error carrying the exit code the client should receive."""

    def __init__(self, message, code=ExitCode.SOFTWARE_ERROR):
        super().__init__(message)
        self.code = code
