from aiohttp import web
from routers.tasks import task_urls

def setup_routers(app: web.Application):
    base_url = f'/api/{ app["config"]["api"]["version"] }'
    task_urls(app, base_url)