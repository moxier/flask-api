"""
    Created by Amirk on 2018-07-20.
"""

from app.libs.redprint import RedPrint
from app.libs.token_auth import auth
from app.model.user import User

api = RedPrint('user')


@api.route('/<int:uid>', methods=['GET'])
@auth.login_required
def get_user(uid):
    user = User.query.get_or_404(uid)
    return 'GET user'


@api.route('', methods=['PUT'])
def put_user():
    return 'PUT user'


@api.route('', methods=['DELETE'])
def delete_user():
    return 'DELETE user'


@api.route('', methods=['POST'])
def post_user():
    return 'POST user'
