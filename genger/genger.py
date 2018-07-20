"""
    Created by Amirk on 2018-07-20.
"""
from app.app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
