from aiohttp import web
from datetime import datetime


async def task_type(request: web.Request) -> web.json_response:

    types = request.app['db']['duration_default_task']

    return web.json_response({
        'ok': True,
        'msg': 'Succefully',
        'types': types
    })


async def create_task(request: web.Request) -> web.json_response:

    task = await request.json()

    insert_id = 0 if len(request.app['db']['tasks']) < 1 else max([ task.get('id') for task in request.app['db']['tasks'] ])

    task['id'] = insert_id + 1
    tasks = request.app['db']['tasks'].append({
        'id': task.get('id'),
        'create_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'update_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'description': task.get('description'),
        'status': '1',
        'optionalMinutes': int(task.get('optionalMinutes')),
        'optionalSeconds': int(task.get('optionalSeconds')),
        'status_time': int(task.get('status_time')),
        'status_task': 'create',
        'duration': int(task.get('duration')),
        'to_play': int(task.get('to_play')),
    })

    return web.json_response({
        'ok': True,
        'msg': 'Task created successfully',
        'task': task,
    }, status=201)


async def list_task(request: web.Request) -> web.json_response:

    tasks = request.app['db']['tasks']

    return web.json_response({
        'ok': True,
        'msg': 'Succefully',
        'tasks': tasks
    }, status=200)


async def get_task(request: web.Request) -> web.json_response:
    
    task_id = int(request.match_info.get('task_id') or 0)

    task = None
    for task_db in request.app['db']['tasks']:
        if task_db.get('id') == task_id:
            task = task_db
    
    return web.json_response({
        'ok': True,
        'msg': 'succefully',
        'task': task
    }, status=200)


async def update_task(request: web.Request) -> web.json_response:

    task = await request.json()

    tasks_db = request.app['db']['tasks']

    for index, task_db in enumerate(tasks_db):
        if task_db.get('id') == task.get('id'):
            tasks_db[index] = {
                'id': task.get('id'),
                'create_date': tasks_db[index].get('create_date'),
                'update_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'description': task.get('description'),
                'status': '1',
                'optionalMinutes': int(task.get('optionalMinutes')),
                'optionalSeconds': int(task.get('optionalSeconds')),
                'status_time': int(task.get('status_time')),
                'status_task': task.get('status_task'),
                'duration': int(task.get('duration')),
                'to_play': int(task.get('to_play')),
            }

            break

    return web.json_response({
        'ok': True,
        'msg': 'Task updated successfully',
        'task': task
    }, status=200)


async def delete_task(request: web.Request) -> web.json_response:

    task = int(request.match_info.get('task_id') or 0)

    tasks_db = request.app['db']['tasks']

    for index, task_db in enumerate(tasks_db):
        if task_db.get('id') == task:
            del tasks_db[index]

    return web.json_response({
        'ok': True,
        'msg': 'Task was delete succefully',
        'tasks': tasks_db
    }, status=200)
