# Generated by Django 3.0.14 on 2021-06-08 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0012_auto_20210420_2257'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
            ],
        ),
    ]
