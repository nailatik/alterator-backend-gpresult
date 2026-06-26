PATH_DB = "/etc/dconf/db/policy"


def get_path_to_policy(uid=None):
    if uid:
        return PATH_DB + str(uid)

    return PATH_DB