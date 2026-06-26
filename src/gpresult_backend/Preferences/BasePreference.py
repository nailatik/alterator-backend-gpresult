class BasePreference:
    def __init__(self, **kwargs):
        self.policy_name = kwargs.get("policy_name")
        self.disabled = kwargs.get("disabled")
        self.remove_policy = kwargs.get("remove_policy")

        self.uid = kwargs.get("uid")
        self.bypass_errors = kwargs.get("bypass_errors")
        self.apply_once = kwargs.get("apply_once")
        self.changed = kwargs.get("changed")
        self.filters = kwargs.get("filters")