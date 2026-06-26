from typing import ClassVar

from .BasePreference import BasePreference


class Inifile(BasePreference):
    inifiles: ClassVar[dict] = {}

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.path = kwargs.get("path")
        self.section = kwargs.get("section")
        self.property = kwargs.get("property")
        self.value = kwargs.get("value")
        self.action = kwargs.get("action")

        Inifile.set_inifile(self)

    @classmethod
    def set_inifile(cls, ini):
        cls.inifiles.setdefault(ini.policy_name, []).append(ini)