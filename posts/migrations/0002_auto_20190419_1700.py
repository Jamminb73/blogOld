# Generated by Django 2.1.7 on 2019-04-19 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-date_posted']},
        ),
    ]
