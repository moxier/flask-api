"""
    Created by Amirk on 2018-07-22.
"""
from flask import current_app, jsonify

from app.libs.enums import ClintTypeEnum
from app.libs.redprint import RedPrint
from app.model.user import User
from app.vaildators.forms import ClientForm
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

api = RedPrint('token')


@api.route('', methods=['POST'])
def get_token():
    form = ClientForm().validate_for_api()
    promise = {
        ClintTypeEnum.USER_EMAIL: User.verify,
    }
    identity = promise[form.type.data](
        form.account.data,
        form.secret.data
    )
    # token
    expiration = current_app.config['TOKEN_EXPIRATION']
    token = generate_auth_token(identity['uid'],
                                form.type.data,
                                None,

                                expiration)

    return jsonify({'token': token.decode('ascii')})


def generate_auth_token(uid, ac_type, scope=None,
                        expiration=7200):
    s = Serializer(current_app.config['SECRET_KEY'],
                   expires_in=expiration)
    return s.dumps({
        'uid': uid,
        'type': ac_type.value
    })
