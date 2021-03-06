# -*- coding: utf-8 -*-
"""
    Created by Huang
    Date: 2018/9/1
"""


class Scope:
    allow_api = set()
    allow_module = set()
    forbidden = set()

    def __add__(self, other):
        self.allow_module = self.allow_module | other.allow_module
        self.allow_api = self.allow_api | other.allow_api
        self.forbidden = self.forbidden | other.forbidden
        return self


class SuperScope(Scope):
    allow_api = {'v1.user'}


class UserScope(Scope):
    forbidden = {'v1.user+super_get_user', 'v1.user+super_delete_user'}

    def __init__(self):
        self + SuperScope()


def is_in_scope(scope, endpoint):
    scope = globals()[scope]()
    splits = endpoint.split('+')
    red_name = splits[0]
    if endpoint in scope.forbidden:
        return False
    return (endpoint in scope.allow_api) or (red_name in scope.allow_module)