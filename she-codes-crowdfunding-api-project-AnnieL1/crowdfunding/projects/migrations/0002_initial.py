# Generated by Django 4.1.5 on 2023-01-29 23:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projects', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='stretchgoals',
            name='gamer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player_pledge', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='stretchgoals',
            name='pledge',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stretch_goal', to='projects.pledge'),
        ),
        migrations.AddField(
            model_name='project',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner_projects', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='pledge',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pledges', to='projects.project'),
        ),
        migrations.AddField(
            model_name='pledge',
            name='supporter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='supporter_pledges', to=settings.AUTH_USER_MODEL),
        ),
    ]
