from typing import ClassVar

from .BasePreference import BasePreference


class File(BasePreference):
    files: ClassVar[dict] = {}

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.fromPath = kwargs.get("fromPath")
        self.source = kwargs.get("source")
        self.action = kwargs.get("action")
        self.targetPath = kwargs.get("targetPath")
        self.readOnly = kwargs.get("readOnly")
        self.archive = kwargs.get("archive")
        self.hidden = kwargs.get("hidden")
        self.suppress = kwargs.get("suppress")
        self.executable = kwargs.get("executable")

        File.set_file(self)

    @classmethod
    def set_file(cls, file):
        cls.files.setdefault(file.policy_name, []).append(file)