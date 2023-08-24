# Generated by Django 4.2.4 on 2023-08-23 10:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_img', models.ImageField(upload_to='profile')),
                ('occupation', models.CharField(max_length=128)),
                ('follower', models.IntegerField()),
                ('description', models.CharField(max_length=150)),
                ('verify', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail', models.TextField()),
                ('like', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ReplyComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail', models.TextField()),
                ('link', models.IntegerField()),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.comment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follow_date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.author')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poster', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=150)),
                ('detail', models.TextField()),
                ('like', models.IntegerField()),
                ('read', models.IntegerField()),
                ('write', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.author')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='content',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.content'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='author',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.category'),
        ),
        migrations.AddField(
            model_name='author',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
