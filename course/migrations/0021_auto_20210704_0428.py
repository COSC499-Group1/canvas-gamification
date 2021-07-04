# Generated by Django 3.0.14 on 2021-07-04 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('canvas', '0009_auto_20210704_0428'),
        ('course', '0020_leaderboard_leaderboardstudents'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaderboard',
            name='assigned_course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='canvas.CanvasCourse', to_field='name'),
        ),
        migrations.AlterField(
            model_name='leaderboard',
            name='name',
            field=models.TextField(unique=True),
        ),
        migrations.AlterField(
            model_name='leaderboardstudents',
            name='leader_board',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='course.LeaderBoard', to_field='name'),
        ),
    ]
