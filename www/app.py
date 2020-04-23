#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Michael Liao'

'''
async web application.
'''

import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web

def index(request):
    return web.Response(body=b'<h1>Awesome</h1>',headers={'content-type':'text/html'})

async def init(event_loop):
		#运行Web服务器
		app = web.Application()
		#创建一个Application实例并在特定的HTTP方法和路径上注册请求处理程序
		app.add_routes([web.get( '/', index)])

		runner = web.AppRunner(app)
		await runner.setup()
		site = web.TCPSite(runner,'127.0.0.1',9000)
		logging.info('server started at http://127.0.0.1:9000...')
		await site.start()
    #srv = await event_loop.create_server(app_runner.app.make_handler(), '127.0.0.1', 9000)
    #logging.info('server started at http://127.0.0.1:9000...')
    #return srv
	
loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()

