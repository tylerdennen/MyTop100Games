# Generated by Django 3.0.6 on 2020-05-21 18:47
import requests
from django.db import migrations
from datetime import date


def populate_games(apps, schema_editor):
    Game = apps.get_model('rating', 'Game')
    Genre = apps.get_model('rating', 'Genre')
    Platform = apps.get_model('rating', 'Platform')

    data = requests.get('https://api.rawg.io/api/games').json()
    for game in data['results']:
        try:
            year, month, day = [int(obj) for obj in game['released'].split('-')]
            game_db = Game.objects.create(name=game['name'], slug=game['slug'], image=game['background_image'],
                                          date_released=date(year, month, day))
        except AttributeError:
            game_db = Game.objects.create(name=game['name'], slug=game['slug'], image=game['background_image'])
        print(f'Successfully added {game_db}')
        for platform in game['platforms']:
            platform_db, created = Platform.objects.get_or_create(name=platform['platform']['name'],
                                                                  slug=platform['platform']['slug'])
            game_db.platforms.add(platform_db)
            print(f'Successfully added {platform_db} to {game_db}')
        for genre in game['genres']:
            genre_db, created = Genre.objects.get_or_create(name=genre['name'], slug=genre['slug'])
            game_db.genres.add(genre_db)
            print(f'Successfully added {genre_db} to {game_db}')


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0004_auto_20200521_2146'),
    ]

    operations = [
        migrations.RunPython(populate_games)
    ]
