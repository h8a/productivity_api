from aiohttp import web
from controllers.task.tasks import (create_task, list_task, update_task,
                                    delete_task, task_type, get_task)


def task_urls(app: web.Application, base_url: str):
    app.router.add_get(f'{ base_url }/task/type', task_type)
    app.router.add_post(f'{ base_url }/task', create_task)
    app.router.add_get(f'{ base_url }/task', list_task)
    app.router.add_get( base_url + '/task/{task_id}',  get_task)
    app.router.add_put( base_url + '/task/update/{task_id}',  update_task)
    app.router.add_delete( base_url + '/task/delete/{task_id}',  delete_task)