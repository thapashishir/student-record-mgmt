# Generated by Django 4.0.4 on 2022-07-29 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('student_name', models.CharField(max_length=100)),
                ('roll_no', models.IntegerField()),
                ('gender', models.CharField(max_length=20)),
                ('faculty', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'students',
            },
        ),
    ]
