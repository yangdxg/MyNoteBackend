# Generated by Django 2.1.7 on 2019-04-10 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.CharField(default='', max_length=30, verbose_name='邮箱')),
                ('phone', models.CharField(default='', max_length=11, unique=True, verbose_name='手机号码')),
                ('username', models.CharField(default='', max_length=20, verbose_name='用户名')),
                ('gender', models.CharField(choices=[('2', '女'), ('1', '男')], default='1', max_length=10, verbose_name='性别')),
                ('avatar', models.ImageField(default='/default/default_head.jpg', upload_to='', verbose_name='头像')),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
                'db_table': 'users',
            },
        ),
    ]