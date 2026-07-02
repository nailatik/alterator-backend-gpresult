# -*- coding: utf-8 -*-
"""Validation of the arguments the wrapper receives over D-Bus."""

import re

from .errors import BackendError, ExitCode

_GUID_RE = re.compile(
    r"^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{12}$"
)
_CONTROL_RE = re.compile(r"[\x00-\x1f\x7f]")


def validate_guid(guid):
    if not guid or not _GUID_RE.match(guid.strip("{}")):
        raise BackendError(f"invalid GPO GUID: {guid!r}", ExitCode.DATA_ERROR)
    return guid


def validate_name(name):
    if not name or not name.strip():
        raise BackendError("GPO name must not be empty", ExitCode.DATA_ERROR)
    if _CONTROL_RE.search(name):
        raise BackendError("GPO name contains control characters", ExitCode.DATA_ERROR)
    return name
