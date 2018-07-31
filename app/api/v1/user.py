from app.libs.redprint import Redprint


api = Redprint('user')


@api.route('/user/get')
def get_user():
    return 'i am kevin'
