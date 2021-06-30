# Generated by Django 3.0.14 on 2021-06-30 04:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('canvas', '0008_event_type'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course', '0019_testmodel_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeaderBoard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('is_visible', models.BooleanField(default=False)),
                ('assigned_course', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='canvas.CanvasCourse')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LeaderBoardStudents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token_value', models.IntegerField(default=0)),
                ('leader_board', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='course.LeaderBoard')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
