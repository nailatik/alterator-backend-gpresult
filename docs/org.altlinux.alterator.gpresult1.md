# Interface **org.altlinux.alterator.gpresult1**

Read-only interface exposing Group Policy (gpresult) results over D-Bus.


Each stdout_strings element is one standalone GPO JSON object (no envelope, no array).
GetAllGPOs is the exception: it splits results into separate "user" and "machine" out arguments.

The full GPO JSON object shape (fields, key/value entries, preference attributes)
is documented in docs/gpo-json-schema.md.

Notes:
- previous_value (renamed from mod_previous_value) may be null.
- The "password" field is always replaced with "***REDACTED***" before output to prevent GPP credential leakage over the network (cf. MS14-025).

| Method | Summary |
|--------|---------|
| [GetOperatingSystemName](#method-GetOperatingSystemName) | Returns the operating system pretty name. |
| [GetAllGPOs](#method-GetAllGPOs) | Returns all applied GPOs, split into separate user and machine scopes. |
| [GetUserGPOs](#method-GetUserGPOs) | Returns GPOs applied to the current user scope. |
| [GetMachineGPOs](#method-GetMachineGPOs) | Returns GPOs applied to the machine scope. |
| [GetGPObyGUID](#method-GetGPObyGUID) | Returns GPOs matching the given GUID across both scopes. |
| [GetGPObyName](#method-GetGPObyName) | Returns GPOs matching the given display name across both scopes. |


## Methods

### **GetOperatingSystemName**() -> ([stdout_strings](#argument-stdout_strings-of-GetOperatingSystemName) : `as`, [stderr_strings](#argument-stderr_strings-of-GetOperatingSystemName) : `as`, [response](#argument-response-of-GetOperatingSystemName) : `i`)<a id="method-GetOperatingSystemName"></a>

Returns the operating system pretty name.


The PRETTY_NAME field of /etc/os-release (falling back to NAME), e.g.
"ALT Workstation 11.2 (Prometheus)".

#### Output arguments

##### **stdout_strings** : `as` <a id="argument-stdout_strings-of-GetOperatingSystemName"></a>

One element: the OS pretty name from /etc/os-release.

##### **stderr_strings** : `as` <a id="argument-stderr_strings-of-GetOperatingSystemName"></a>

##### **response** : `i` <a id="argument-response-of-GetOperatingSystemName"></a>

### **GetAllGPOs**() -> ([user](#argument-user-of-GetAllGPOs) : `as`, [machine](#argument-machine-of-GetAllGPOs) : `as`, [stderr_strings](#argument-stderr_strings-of-GetAllGPOs) : `as`, [response](#argument-response-of-GetAllGPOs) : `i`)<a id="method-GetAllGPOs"></a>

Returns all applied GPOs, split into separate user and machine scopes.

#### Output arguments

##### **user** : `as` <a id="argument-user-of-GetAllGPOs"></a>

One GPO object per element (user scope). GPO shape: see docs/gpo-json-schema.md.

##### **machine** : `as` <a id="argument-machine-of-GetAllGPOs"></a>

One GPO object per element (machine scope). GPO shape: see docs/gpo-json-schema.md.

##### **stderr_strings** : `as` <a id="argument-stderr_strings-of-GetAllGPOs"></a>

##### **response** : `i` <a id="argument-response-of-GetAllGPOs"></a>

### **GetUserGPOs**() -> ([stdout_strings](#argument-stdout_strings-of-GetUserGPOs) : `as`, [stderr_strings](#argument-stderr_strings-of-GetUserGPOs) : `as`, [response](#argument-response-of-GetUserGPOs) : `i`)<a id="method-GetUserGPOs"></a>

Returns GPOs applied to the current user scope.

#### Output arguments

##### **stdout_strings** : `as` <a id="argument-stdout_strings-of-GetUserGPOs"></a>

One GPO object per element (user scope). GPO shape: see docs/gpo-json-schema.md.

##### **stderr_strings** : `as` <a id="argument-stderr_strings-of-GetUserGPOs"></a>

##### **response** : `i` <a id="argument-response-of-GetUserGPOs"></a>

### **GetMachineGPOs**() -> ([stdout_strings](#argument-stdout_strings-of-GetMachineGPOs) : `as`, [stderr_strings](#argument-stderr_strings-of-GetMachineGPOs) : `as`, [response](#argument-response-of-GetMachineGPOs) : `i`)<a id="method-GetMachineGPOs"></a>

Returns GPOs applied to the machine scope.

#### Output arguments

##### **stdout_strings** : `as` <a id="argument-stdout_strings-of-GetMachineGPOs"></a>

One GPO object per element (machine scope). GPO shape: see docs/gpo-json-schema.md.

##### **stderr_strings** : `as` <a id="argument-stderr_strings-of-GetMachineGPOs"></a>

##### **response** : `i` <a id="argument-response-of-GetMachineGPOs"></a>

### **GetGPObyGUID**([guid](#argument-guid-of-GetGPObyGUID) : `s`) -> ([stdout_strings](#argument-stdout_strings-of-GetGPObyGUID) : `as`, [stderr_strings](#argument-stderr_strings-of-GetGPObyGUID) : `as`, [response](#argument-response-of-GetGPObyGUID) : `i`)<a id="method-GetGPObyGUID"></a>

Returns GPOs matching the given GUID across both scopes.


Always searches both user and machine scopes.

#### Input arguments

##### **guid** : `s` <a id="argument-guid-of-GetGPObyGUID"></a>

The GPO GUID to search for (e.g. "31B2F340-016D-11D2-945F-00C04FB984F9").

#### Output arguments

##### **stdout_strings** : `as` <a id="argument-stdout_strings-of-GetGPObyGUID"></a>

One GPO object per element, from both scopes. GPO shape: see docs/gpo-json-schema.md.

##### **stderr_strings** : `as` <a id="argument-stderr_strings-of-GetGPObyGUID"></a>

##### **response** : `i` <a id="argument-response-of-GetGPObyGUID"></a>

### **GetGPObyName**([name](#argument-name-of-GetGPObyName) : `s`) -> ([stdout_strings](#argument-stdout_strings-of-GetGPObyName) : `as`, [stderr_strings](#argument-stderr_strings-of-GetGPObyName) : `as`, [response](#argument-response-of-GetGPObyName) : `i`)<a id="method-GetGPObyName"></a>

Returns GPOs matching the given display name across both scopes.


The caller MUST quote name values
(e.g. "Default Domain Policy"), following the same convention as
exclude_pkgnames in apt1 -- the executor splits argv on spaces and an
unquoted multi-word name would be truncated.

Always searches both user and machine scopes.

#### Input arguments

##### **name** : `s` <a id="argument-name-of-GetGPObyName"></a>

The GPO display name to search for.

#### Output arguments

##### **stdout_strings** : `as` <a id="argument-stdout_strings-of-GetGPObyName"></a>

One GPO object per element, from both scopes. GPO shape: see docs/gpo-json-schema.md.

##### **stderr_strings** : `as` <a id="argument-stderr_strings-of-GetGPObyName"></a>

##### **response** : `i` <a id="argument-response-of-GetGPObyName"></a>

