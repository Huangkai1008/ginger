from flask import jsonify, g

from app.libs.error_code import DeleteSuccess, AuthFailed
from app.libs.redprint import Redprint
from app.libs.token_auth import auth
from app.models.base import db
from app.models.user import User

api = Redprint('user')


@api.route('/<int:uid>', methods=['GET'])
@auth.login_required
def super_get_user(uid):
    """
    管理员获取用户信息
    :param uid:
    :return:
    """
    is_admin = g.user.is_admin
    if not is_admin:
        raise AuthFailed()
    user = User.query.filter_by(id=uid).first_or_404()
    return jsonify(user)


@api.route('', methods=['GET'])
@auth.login_required
def get_user():
    """
    普通用户获取用户信息
    :return:
    """
    uid = g.user.id
    user = User.query.filter_by(id=uid).first_or_404()
    return jsonify(user)


@api.route('/<int:uid>', methods=['DELETE'])
def super_delete_user(uid):
    """
    管理员删除用户
    :param uid:
    :return:
    """
    pass


@api.route('/', methods=['DELETE'])
@auth.login_required
def delete_user():
    """
    :return:
    """
    uid = g.user.uid
    with db.auto_commit():
        user = User.query.filter_by(id=uid).first_or_404()
        user.delete()
    return DeleteSuccess()
