from typing import ClassVar

from .BasePreference import BasePreference


class Drive(BasePreference):
    drives: ClassVar[dict] = {}

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.login = kwargs.get("login")
        self.password = kwargs.get("password")
        self.dir = kwargs.get("dir")
        self.path = kwargs.get("path")
        self.action = kwargs.get("action")
        self.thisDrive = kwargs.get("thisDrive")
        self.allDrives = kwargs.get("allDrives")
        self.label = kwargs.get("label")
        self.persistent = kwargs.get("persistent")
        self.useLetter = kwargs.get("useLetter")

        Drive.set_drive(self)

    @classmethod
    def set_drive(cls, drive):
        cls.drives.setdefault(drive.policy_name, []).append(drive)