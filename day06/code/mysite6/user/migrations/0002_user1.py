# Generated by Django 3.2 on 2021-05-04 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30, unique=True, verbose_name='用户名')),
                ('password', models.CharField(max_length=30, verbose_name='密码')),
            ],
        ),
    ]
