# Generated by Django 4.1.6 on 2023-02-20 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0004_alter_imdbtitle_rating_alter_imdbtitle_release_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='imdbtitle',
            name='votes',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]