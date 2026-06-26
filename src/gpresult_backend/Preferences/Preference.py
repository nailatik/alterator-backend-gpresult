from typing import ClassVar

from .Drive import Drive
from .EnvVar import EnvVar
from .File import File
from .Folder import Folder
from .Inifile import Inifile
from .Networkshare import NetworkShare
from .Shortcut import Shortcut


class Preference:
    preferences: ClassVar[dict] = {}

    def __init__(self, obj, pref_type, **kwargs):
        self.obj = obj
        self.type = pref_type
        self.policy_name = kwargs.get("policy_name")

        if pref_type == "Folders":
            self.preference_obj = Folder(**kwargs)
        elif pref_type == "Inifiles":
            self.preference_obj = Inifile(**kwargs)
        elif pref_type == "Shortcuts":
            self.preference_obj = Shortcut(**kwargs)
        elif pref_type == "Environmentvariables":
            self.preference_obj = EnvVar(**kwargs)
        elif pref_type == "Drives":
            self.preference_obj = Drive(**kwargs)
        elif pref_type == "Files":
            self.preference_obj = File(**kwargs)
        elif pref_type == "Networkshares":
            self.preference_obj = NetworkShare(**kwargs)

        Preference.set_preference(self)

    @classmethod
    def set_preference(cls, pref):
        cls.preferences.setdefault(pref.policy_name, []).append(pref)

    @classmethod
    def clear_preferences(cls):
        cls.preferences.clear()