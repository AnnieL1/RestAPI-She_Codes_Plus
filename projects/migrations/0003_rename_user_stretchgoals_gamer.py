# Generated by Django 4.1.5 on 2023-01-27 22:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stretchgoals',
            old_name='user',
            new_name='gamer',
        ),
    ]