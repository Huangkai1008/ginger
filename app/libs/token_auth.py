# -*- coding: utf-8 -*-
"""
    Created by Huang
    Date: 2018/8/12
"""
from collections import namedtuple

from flask import current_app, g
from flask_httpauth import HTTPBasicAuth
from itsdangerous import TimedJSONWebSignatureSerializer \
    as Serializer, BadSignature, SignatureExpired

from app.libs.error_code import AuthFailed

auth = HTTPBasicAuth()

User = namedtuple('User', ['uid', 'ac_type', 'scope'])


@auth.verify_password
def verify_password(token, password):
    """
    :key = Authorization
    :value = basic base64（account:password）
    """
    user_info = verify_auth_token(token)
    if not user_info:
        return False
    else:
        g.user = user_info
        return True


def verify_auth_token(token):
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
        # .loads 解密token
        data = s.loads(token)
    except BadSignature:
        # 令牌非法
        raise AuthFailed(msg='token is invalid', error_code=1002)
    except SignatureExpired:
        # 令牌过期
        raise AuthFailed(msg='token is expired', error_code=1003)
    uid = data['uid']
    ac_type = data['type']
    return User(uid, ac_type, '')
