# Generated by Django 4.1.6 on 2023-02-13 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_alter_imdbtitle_release_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imdbtitle',
            name='rating',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True),
        ),
    ]
