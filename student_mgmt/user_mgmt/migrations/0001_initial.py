# Generated by Django 4.0.4 on 2022-07-29 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
