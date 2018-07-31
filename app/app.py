from flask import Flask


def create_app():
    # __name__为配置信息
    app = Flask(__name__)
    # 导入配置项
    app.config.from_object('app.config.setting')
    app.config.from_object('app.config.secure')
    return app
