from flask import Flask


def register_blueprints(app):
    """
    注册蓝图
    :param app:
    :return:
    """
    from app.api.v1.user import user
    from app.api.v1.book import book
    app.register_blueprint(user)
    app.register_blueprint(book)


def create_app():
    # __name__为配置信息
    app = Flask(__name__)
    # 导入配置项
    app.config.from_object('app.config.setting')
    app.config.from_object('app.config.secure')

    # 调用注册蓝图的函数
    register_blueprints(app)

    return app
