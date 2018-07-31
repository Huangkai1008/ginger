from flask import Flask


def register_blueprints(app):
    """
    注册蓝图到flask核心对象上
    :param app:
    :return:
    """
    from app.api.v1 import create_blueprint_v1
    app.register_blueprint(create_blueprint_v1(), url_prefix='/v1')


def create_app():
    # __name__为配置信息
    app = Flask(__name__)
    # 导入配置项
    app.config.from_object('app.config.setting')
    app.config.from_object('app.config.secure')

    # 调用注册蓝图的函数
    register_blueprints(app)

    return app
