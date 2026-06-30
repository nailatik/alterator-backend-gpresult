from typing import ClassVar


class GPO:
    gpos: ClassVar[
        list
    ] = []  # List of all GPOs retrieved from /etc/dconf/db/policy<guid>

    def __init__(self, obj, **kwargs):
        self.path = kwargs.get("correct_path")  # Sysvol path
        self.name = kwargs.get("display_name")  # Displayed GPO name
        self.guid = kwargs.get("name")  # GUID
        self.version = kwargs.get("version")  # Version
        self.obj = obj  # Whether the GPO refers to a machine or user object
        self.keys_values = []  # List of keys and values related to GPOs
        self.preferences = []  # Preferences list

        GPO.set_gpo(self)

    def get_sorted_keys_values(self):
        return sorted(self.keys_values, key=lambda x: x.key)

    @staticmethod
    def normalize_guid(guid):
        # GPO GUIDs are stored wrapped in braces;
        # accept both braced/unbraced and any letter case from the caller.
        return guid.strip("{}").lower() if guid else guid

    @classmethod
    def get_gpos_by_guid(cls, guid, obj=None):
        gpos_res = []
        guid = cls.normalize_guid(guid)

        for gpo in cls.gpos:
            if cls.normalize_guid(gpo.guid) == guid and (
                (obj and gpo.obj == obj) or not obj
            ):
                gpos_res.append(gpo)

        return gpos_res

    @classmethod
    def get_gpos_by_name(cls, name, obj=None):
        gpos_res = []

        for gpo in cls.gpos:
            if gpo.name == name and ((obj and gpo.obj == obj) or not obj):
                gpos_res.append(gpo)

        return gpos_res

    @classmethod
    def set_keys_values(cls, kv):
        kv_policy_name = kv.policy_name

        for gpo in cls.gpos:
            if gpo.name == kv_policy_name and gpo.obj == kv.obj:
                gpo.keys_values.append(kv)
                return None

        return False

    @classmethod
    def set_gpo(cls, gpo):
        guid = gpo.guid
        obj = gpo.obj

        for e in cls.gpos:
            if e.guid == guid and e.obj == obj:
                e.path = gpo.path if not e.path else e.path
                e.name = gpo.name if not e.name else e.name
                e.version = gpo.version if not e.version else e.version
                return

        cls.gpos.append(gpo)

    @classmethod
    def get_all_gpos(cls, obj=None):
        if not obj:
            return cls.gpos
        return [gpo for gpo in cls.gpos if gpo.obj == obj]

    @classmethod
    def set_preferences(cls, gpo_name, prefs):
        for gpo in cls.gpos:
            if gpo.name == gpo_name:
                for pref in prefs:
                    if pref.obj == gpo.obj:
                        gpo.preferences.append(pref)