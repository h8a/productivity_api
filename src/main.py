import re
from aiohttp import web
from aiohttp_middlewares import cors_middleware
from aiohttp_middlewares.cors import DEFAULT_ALLOW_HEADERS
from db import init_db, close_db, generate_random_data
from router import setup_routers
from settings import ENVIRONMENT


async def init_app():
    app = web.Application(
        middlewares=[
            cors_middleware(
                origins=[re.compile(r"ĥttps?\:\/\/"+ENVIRONMENT['headers'].get('origin'))],
                allow_credentials=True,
                allow_headers=DEFAULT_ALLOW_HEADERS,
            )
        ]
    )

    app['config'] = ENVIRONMENT

    app.on_startup.append(init_db)
    app.on_startup.append(generate_random_data)
    app.on_cleanup.append(close_db)

    setup_routers(app)

    return app