"""
    Created by Amirk on 2018-07-20.
"""


from app.libs.redprint import RedPrint


api = RedPrint('user')

@api.route('/get')
def get_user():
    return 'get user'
