from typing import ClassVar

from .BasePreference import BasePreference


class Shortcut(BasePreference):
    shortcuts: ClassVar[dict] = {}

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.dest = kwargs.get("dest")
        self.path = kwargs.get("path")
        self.expanded_path = kwargs.get("expanded_path")
        self.arguments = kwargs.get("arguments")
        self.name = kwargs.get("name")
        self.action = kwargs.get("action")
        self.changed = kwargs.get("changed")
        self.icon = kwargs.get("icon")
        self.comment = kwargs.get("comment")
        self.is_in_user_context = kwargs.get("is_in_user_context")
        self.type = kwargs.get("type")
        self.desktop_file_template = kwargs.get("desktop_file_template")

        Shortcut.set_shortcut(self)

    @classmethod
    def set_shortcut(cls, shortcut):
        cls.shortcuts.setdefault(shortcut.policy_name, []).append(shortcut)