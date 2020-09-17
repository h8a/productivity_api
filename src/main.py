from aiohttp import web
from aiohttp_middlewares import cors_middleware
from aiohttp_middlewares.cors import DEFAULT_ALLOW_HEADERS, DEFAULT_ALLOW_METHODS
from db import init_db, close_db, generate_random_data
from router import setup_routers
from settings import ENVIRONMENT


async def init_app():
    app = web.Application(
        middlewares=[
            cors_middleware(
                # allow_all=True
                origins=ENVIRONMENT['headers']['origin'],
                allow_headers=('Access-Control-Allow-Origin', 'Access-Control-Allow-Headers')+DEFAULT_ALLOW_HEADERS,
                allow_methods=DEFAULT_ALLOW_METHODS,
                allow_credentials=True,
            )
        ]
    )

    app['config'] = ENVIRONMENT

    app.on_startup.append(init_db)
    app.on_startup.append(generate_random_data)
    app.on_cleanup.append(close_db)

    setup_routers(app)

    return app


def main():
    app = init_app()

    web.run_app(app,
                host=ENVIRONMENT['api'].get('host'),
                port=ENVIRONMENT['api'].get('port'))


if __name__ == "__main__":
    main()