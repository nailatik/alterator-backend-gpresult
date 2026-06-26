from typing import ClassVar

from .BasePreference import BasePreference


class EnvVar(BasePreference):
    envvars: ClassVar[dict] = {}

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.name = kwargs.get("name")
        self.value = kwargs.get("value")
        self.action = kwargs.get("action")

        EnvVar.set_envvar(self)

    @classmethod
    def set_envvar(cls, envvar):
        cls.envvars.setdefault(envvar.policy_name, []).append(envvar)