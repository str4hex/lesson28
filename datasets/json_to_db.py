import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lesson28.settings')
application = get_asgi_application()

import json
from app.models import Ad, Category, User, Location

with open('ad.json', 'r', encoding='utf-8') as file_json:
    load = json.load(file_json)

    for load_db in range(len(load)):
        ad = Ad(Id=load[load_db]['Id'],
                name=load[load_db]['name'],
                author_id=load[load_db]['author_id'],
                price=load[load_db]['price'],
                description=load[load_db]['description'],
                image=load[load_db]['image'],
                is_published=load[load_db]['is_published'].title(),
                category_id=load[load_db]['category_id']
                )
        ad.save()

with open('category.json', 'r', encoding='utf-8') as file_json:
    load = json.load(file_json)

    for load_db in range(len(load)):

        cat = Category(id=load[load_db]['id'],
                       name=load[load_db]['name'])
        cat.save()


with open('location.json', 'r', encoding='utf-8') as file_json:
    load = json.load(file_json)

    for load_db in range(len(load)):
        loc = Location(id=load[load_db]['id'],
                       name=load[load_db]['name'],
                       lat=load[load_db]['lat'],
                       lng=load[load_db]['lng'],
                       )
        loc.save()

with open('user.json', 'r', encoding='utf-8') as file_json:
    load = json.load(file_json)

    for load_db in range(len(load)):
        user = User(id=load[load_db]['id'],
                    first_name=load[load_db]['first_name'],
                    last_name=load[load_db]['last_name'],
                    username=load[load_db]['username'],
                    password=load[load_db]['password'],
                    role=load[load_db]['role'],
                    age=load[load_db]['age'],
                    location_id=load[load_db]['location_id'],
                    )
        user.save()
