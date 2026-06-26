from typing import ClassVar

from .BasePreference import BasePreference


class NetworkShare(BasePreference):
    nshares: ClassVar[dict] = {}

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.name = kwargs.get("name")
        self.action = kwargs.get("action")
        self.path = kwargs.get("path")
        self.allRegular = kwargs.get("allRegular")
        self.comment = kwargs.get("comment")
        self.limitUsers = kwargs.get("limitUsers")
        self.abe = kwargs.get("abe")

        NetworkShare.set_nshare(self)

    @classmethod
    def set_nshare(cls, nshare):
        cls.nshares.setdefault(nshare.policy_name, []).append(nshare)