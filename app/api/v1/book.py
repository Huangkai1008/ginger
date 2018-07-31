from app.libs.redprint import Redprint


api = Redprint('book')


@api.route('/book/get')
def get_book():
    return 'get book'


@api.route('/book/create')
def create_book():
    return 'create book'