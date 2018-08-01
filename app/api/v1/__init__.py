from flask import Blueprint
from app.api.v1 import user, book


def create_blueprint_v1():
    """
    注册红图到蓝图上
    :return:
    """
    bp_v1 = Blueprint('v1', __name__)

    user.api.register(bp_v1)
    book.api.register(bp_v1)
    return bp_v1
