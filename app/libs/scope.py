# -*- coding: utf-8 -*-
"""
    Created by Huang
    Date: 2018/9/1
"""


class AdminScope:
    allow_api = ['v1.super_get_user']


class UserScope:
    allow_api = ['v1.get_user']


def is_in_scope(scope, endpoint):
    if endpoint in scope.allowed_api:
        pass