# Generated by Django 4.1.6 on 2023-04-07 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0008_imdbrating_delete_imdbtitle'),
    ]

    operations = [
        migrations.CreateModel(
            name='TitleGridSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('setting', models.CharField(max_length=50)),
                ('value', models.IntegerField()),
            ],
        ),
    ]