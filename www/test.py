__author__ = 'Thomas'
# -*- coding: utf-8 -*-

import orm, asyncio
from models import User, Blog, Comment

def test(loop):
    yield from orm.create_pool(loop=loop,user='root', password='123456', db='awesome')
    u = User(name='Lin', email='test@sina.com', passwd='1234567890', image='about:blank')
    yield from u.save()
loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()

