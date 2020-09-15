import random
from faker import Faker


async def init_db(app):
    app['db'] = {
        'duration_default_task': [
            {
                'id': 1,
                'type': 'Corta',
                'text': '15 min.',
                'duration': 15
            },
            {
                'id': 2,
                'type': 'Media',
                'text': '30 min.',
                'duration': 30
            },
            {
                'id': 3,
                'type': 'Larga',
                'text': '1 hr.',
                'duration': 60
            },
        ],
        'tasks': []
    }

async def close_db(app):
    del app['db']


async def generate_random_data(app):

    fake = Faker()

    for i in range(1, 51):
        optionalMinutes = random.randint(15, 120) * 60

        if i % 2:
            time_complete = int((80 * optionalMinutes) / 100.0)
        else:
            time_complete = int((100 * optionalMinutes) / 100.0)

        app['db']['tasks'].append({
            'id': i,
            'description': fake.name(),
            'status': '1',
            'optionalMinutes': optionalMinutes,
            'optionalSeconds': 0,
            'status_time': time_complete,
            'status_task': 'stop',
            'duration': 0,
        })