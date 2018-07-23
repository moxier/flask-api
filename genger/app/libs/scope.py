"""
    Created by Amirk on 2018-07-23.
"""


class Scope:
    allow_api = ()

    # allow_modul = ()

    def __add__(self, other):
        self + other.allow_api


class AdminScope(Scope):
    allow_api = ('bp_v1.super_get_user',
                 'bp_v1.super_delete_user',
                 )

    # allow_modul = ('user')
    def __init__(self):
        self + UserScope()


class UserScope(Scope):
    allow_api = ('bp_v1.get_user',
                 'bp_v1.delete_user',
                 'bp_v1.update_user',
                 )


def is_in_scope(scope, endpoint):
    scope = globals()[scope]()
    if endpoint in scope.allow_api:
        return True
    else:
        return False
