# Interface **org.altlinux.alterator.gpresult1**

Read-only interface exposing Group Policy (gpresult) results over D-Bus.


All GPO-returning methods deliver a JSON document via stdout_strings.

Notes:
- scope is either "user" or "machine".
- previous_value (renamed from mod_previous_value) may be null.
- The "password" field is always replaced with "***REDACTED***" before output to prevent GPP credential leakage over the network (cf. MS14-025).

| Method | Summary |
|--------|---------|
| [GetOperationSystemName](#method-GetOperationSystemName) | Returns OS name and system information from the alterator-systeminfo backend. |
| [GetAllGPOs](#method-GetAllGPOs) | Returns all applied GPOs for both machine and user scopes. |
| [GetUserGPOs](#method-GetUserGPOs) | Returns GPOs applied to the current user scope. |
| [GetMachineGPOs](#method-GetMachineGPOs) | Returns GPOs applied to the machine scope. |
| [GetGPObyGUID](#method-GetGPObyGUID) | Returns GPOs matching the given GUID across both scopes. |
| [GetGPObyName](#method-GetGPObyName) | Returns GPOs matching the given display name across both scopes. |


## Methods

### **GetOperationSystemName**() -> ([stdout_strings](#argument-stdout_strings-of-GetOperationSystemName) : `as`, [stderr_strings](#argument-stderr_strings-of-GetOperationSystemName) : `as`, [response](#argument-response-of-GetOperationSystemName) : `i`)<a id="method-GetOperationSystemName"></a>

Returns OS name and system information from the alterator-systeminfo backend.


Delegates to the external /usr/lib/alterator/backends/systeminfo binary.
The output is NOT gpresult GPO-JSON; its shape is owned by alterator-systeminfo.

#### Output arguments

##### **stdout_strings** : `as` <a id="argument-stdout_strings-of-GetOperationSystemName"></a>

Raw output from alterator-systeminfo; format is defined by that backend.

##### **stderr_strings** : `as` <a id="argument-stderr_strings-of-GetOperationSystemName"></a>

##### **response** : `i` <a id="argument-response-of-GetOperationSystemName"></a>

### **GetAllGPOs**() -> ([stdout_strings](#argument-stdout_strings-of-GetAllGPOs) : `as`, [stderr_strings](#argument-stderr_strings-of-GetAllGPOs) : `as`, [response](#argument-response-of-GetAllGPOs) : `i`)<a id="method-GetAllGPOs"></a>

Returns all applied GPOs for both machine and user scopes.

#### Output arguments

##### **stdout_strings** : `as` <a id="argument-stdout_strings-of-GetAllGPOs"></a>

JSON envelope: {"all": [GPO, ...]}. GPO shape defined at interface level.

##### **stderr_strings** : `as` <a id="argument-stderr_strings-of-GetAllGPOs"></a>

##### **response** : `i` <a id="argument-response-of-GetAllGPOs"></a>

### **GetUserGPOs**() -> ([stdout_strings](#argument-stdout_strings-of-GetUserGPOs) : `as`, [stderr_strings](#argument-stderr_strings-of-GetUserGPOs) : `as`, [response](#argument-response-of-GetUserGPOs) : `i`)<a id="method-GetUserGPOs"></a>

Returns GPOs applied to the current user scope.

#### Output arguments

##### **stdout_strings** : `as` <a id="argument-stdout_strings-of-GetUserGPOs"></a>

JSON envelope: {"user": [GPO, ...]}. GPO shape defined at interface level.

##### **stderr_strings** : `as` <a id="argument-stderr_strings-of-GetUserGPOs"></a>

##### **response** : `i` <a id="argument-response-of-GetUserGPOs"></a>

### **GetMachineGPOs**() -> ([stdout_strings](#argument-stdout_strings-of-GetMachineGPOs) : `as`, [stderr_strings](#argument-stderr_strings-of-GetMachineGPOs) : `as`, [response](#argument-response-of-GetMachineGPOs) : `i`)<a id="method-GetMachineGPOs"></a>

Returns GPOs applied to the machine scope.

#### Output arguments

##### **stdout_strings** : `as` <a id="argument-stdout_strings-of-GetMachineGPOs"></a>

JSON envelope: {"machine": [GPO, ...]}. GPO shape defined at interface level.

##### **stderr_strings** : `as` <a id="argument-stderr_strings-of-GetMachineGPOs"></a>

##### **response** : `i` <a id="argument-response-of-GetMachineGPOs"></a>

### **GetGPObyGUID**([guid](#argument-guid-of-GetGPObyGUID) : `s`) -> ([stdout_strings](#argument-stdout_strings-of-GetGPObyGUID) : `as`, [stderr_strings](#argument-stderr_strings-of-GetGPObyGUID) : `as`, [response](#argument-response-of-GetGPObyGUID) : `i`)<a id="method-GetGPObyGUID"></a>

Returns GPOs matching the given GUID across both scopes.


Always searches both user and machine scopes; the client selects the relevant
scope from the returned envelope keys.

#### Input arguments

##### **guid** : `s` <a id="argument-guid-of-GetGPObyGUID"></a>

The GPO GUID to search for (e.g. "31B2F340-016D-11D2-945F-00C04FB984F9").

#### Output arguments

##### **stdout_strings** : `as` <a id="argument-stdout_strings-of-GetGPObyGUID"></a>

JSON envelope: {"user": [GPO, ...], "machine": [GPO, ...]}. GPO shape defined at interface level.

##### **stderr_strings** : `as` <a id="argument-stderr_strings-of-GetGPObyGUID"></a>

##### **response** : `i` <a id="argument-response-of-GetGPObyGUID"></a>

### **GetGPObyName**([name](#argument-name-of-GetGPObyName) : `s`) -> ([stdout_strings](#argument-stdout_strings-of-GetGPObyName) : `as`, [stderr_strings](#argument-stderr_strings-of-GetGPObyName) : `as`, [response](#argument-response-of-GetGPObyName) : `i`)<a id="method-GetGPObyName"></a>

Returns GPOs matching the given display name across both scopes.


The caller MUST quote name values
(e.g. "Default Domain Policy"), following the same convention as
exclude_pkgnames in apt1 -- the executor splits argv on spaces and an
unquoted multi-word name would be truncated.

Always searches both user and machine scopes; the client selects the relevant
scope from the returned envelope keys.

#### Input arguments

##### **name** : `s` <a id="argument-name-of-GetGPObyName"></a>

The GPO display name to search for.

#### Output arguments

##### **stdout_strings** : `as` <a id="argument-stdout_strings-of-GetGPObyName"></a>

JSON envelope: {"user": [GPO, ...], "machine": [GPO, ...]}. GPO shape defined at interface level.

##### **stderr_strings** : `as` <a id="argument-stderr_strings-of-GetGPObyName"></a>

##### **response** : `i` <a id="argument-response-of-GetGPObyName"></a>

