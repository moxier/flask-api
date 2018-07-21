"""
    Created by Amirk on 2018-07-21.
"""
from app.libs.enums import ClintTypeEnum
from app.libs.error_code import Success
from app.libs.redprint import RedPrint
from app.model.user import User
from app.vaildators.forms import UserEmailForm, ClientForm

api = RedPrint('clint')


@api.route('/register', methods=['POST'])
def creat_clint():
    form = ClientForm().validate_for_api()
    promise = {
        ClintTypeEnum.USER_EMAIL: __register_user_by_email,
    }
    promise[form.type.data]()
    return Success()


def __register_user_by_email():
    form = UserEmailForm().validate_for_api()
    User.register_user_by_email(
        form.nickname.data,
        form.account.data,
        form.secret.data)
