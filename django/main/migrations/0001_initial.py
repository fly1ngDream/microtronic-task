# Generated by Django 2.2 on 2019-04-25 14:59

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('polygon', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
            ],
        ),
    ]
