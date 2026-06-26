from typing import ClassVar

from .BasePreference import BasePreference


class Folder(BasePreference):
    folders: ClassVar[dict] = {}

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.path = kwargs.get("path")
        self.action = kwargs.get("action")
        self.delete_folder = kwargs.get("delete_folder")
        self.delete_sub_folder = kwargs.get("delete_sub_folder")
        self.delete_files = kwargs.get("delete_files")
        self.hidden_folder = kwargs.get("hidden_folder")

        Folder.set_folder(self)

    @classmethod
    def set_folder(cls, folder):
        cls.folders.setdefault(folder.policy_name, []).append(folder)