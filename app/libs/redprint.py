class Redprint:
    def __init__(self, name):
        """
        初始化传入name
        :param name: 红图名称
        """
        self.name = name
        self.mound = []

    def route(self, rule, **options):
        """
        自定义路由装饰器
        :param rule: url
        :param options: methods and so on
        :return:
        """
        def decorator(f):
            self.mound.append((f, rule, options))
            return f
        return decorator

    def register(self, bp, url_prefix=None):
        """
        注册红图到蓝图
        :param bp:
        :param url_prefix:
        :return:
        """
        if url_prefix is None:
            url_prefix = '/' + self.name
        for f, rule, options in self.mound:
            endpoint = options.pop("endpoint", f.__name__)
            bp.add_url_rule(url_prefix + rule, endpoint, f, **options)


