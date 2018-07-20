"""
    Created by Amirk on 2018-07-20.
"""

from app.libs.redprint import RedPrint

api = RedPrint('book')


@api.route('/get')
def get_book():
    return 'get book'

@api.route('/create')
def create_book():
    return 'create book'