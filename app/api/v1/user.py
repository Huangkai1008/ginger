from app.libs.redprint import Redprint
from app.libs.token_auth import auth


api = Redprint('user')


# @auth.login_required()
@api.route('/get')
def get_user():
    return 'i am kevin huang'


@api.route('/create')
def create_user():
    pass