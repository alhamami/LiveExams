# Generated by Django 3.0.5 on 2022-05-16 23:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20220517_0240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='exam_creation_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 17, 2, 43, 22, 325032)),
        ),
        migrations.AlterField(
            model_name='takenexam',
            name='done_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 17, 2, 43, 22, 334033)),
        ),
    ]
