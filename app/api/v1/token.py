# -*- coding: utf-8 -*-
"""
    Created by Huang
    Date: 2018/8/12
"""
from flask import current_app
from flask.json import jsonify

from app.libs.enums import ClientTypeEnum
from app.libs.redprint import Redprint
from app.models.user import User
from app.validators.forms import ClientForm
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

api = Redprint('token')


@api.route('', methods=['POST'])
def get_token():
    """
    登录
    :return:
    """
    form = ClientForm().validate_for_api()
    promise = {
        ClientTypeEnum.USER_EMAIL: User.verify,
    }
    identity = promise[form.type.data](
        form.account.data,
        form.secret.data
    )
    expiration = current_app.config['TOKEN_EXPIRATION']
    token = generate_auth_token(identity['uid'],
                                form.type.data,
                                identity['scope'],
                                expiration)
    # Token
    t = {
        'token': token.decode('ascii')
    }
    return jsonify(t), 201


def generate_auth_token(uid, ac_type, is_admin=None, expiration=7200):
    """
    生成令牌
    :param uid: 客户id
    :param ac_type: 客户端种类
    :param scope: 权限作用域
    :param expiration: 过期时间
    :return:
    """
    s = Serializer(current_app.config['SECRET_KEY'], expires_in=expiration)

    return s.dumps({
        'uid': uid,
        'type': ac_type.value,
        'scope': is_admin
    })


