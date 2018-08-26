from flask import Flask as _Flask

from flask.json import JSONEncoder as _JSONEncoder


class JSONEncoder(_JSONEncoder):
    """
    自定义JSONEncoder
    """
    def default(self, o):
        return o.__dict__


class Flask(_Flask):
    """
    改变flask的json_encoder
    """
    json_encoder = JSONEncoder


def register_blueprints(app):
    """
    注册蓝图到flask核心对象上
    :param app:
    :return:
    """
    from app.api.v1 import create_blueprint_v1
    app.register_blueprint(create_blueprint_v1(), url_prefix='/v1')


def register_plugin(app):
    from app.models.base import db
    db.init_app(app)
    with app.app_context():
        db.create_all()


def create_app():
    # __name__为配置信息
    app = Flask(__name__)
    # 导入配置项
    app.config.from_object('app.config.setting')
    app.config.from_object('app.config.secure')

    # 调用注册蓝图的函数
    register_blueprints(app)
    register_plugin(app)

    return app
