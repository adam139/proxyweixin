# -*- coding: utf-8 -*-
# filename: main.py
import web
from handler import Handle
from token_handler import Auth

urls = (
    '/notify', 'Handle',
    '/wx', 'Auth'
)


if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()
