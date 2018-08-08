from app.libs.redprint import Redprint


api = Redprint('user')


@api.route('/get')
def get_user():
    return 'i am kevin huang'


@api.route('/create')
def create_user():
    pass