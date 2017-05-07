"""
This script runs the anglehack application using a development server.
"""

from os import environ
from anglehack import app

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '55535'))
    except ValueError:
        PORT = 55535
    app.run(HOST, PORT)
