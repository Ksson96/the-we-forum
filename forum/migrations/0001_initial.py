# Generated by Django 4.0.2 on 2022-02-10 14:04

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
            name='Category',
            fields=[
                ('category', models.CharField(max_length=30, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('post_id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=300)),
                ('content', models.TextField(blank=True)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='forum_posts', to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(default='No Category', on_delete=django.db.models.deletion.SET_DEFAULT, related_name='post_category', to='forum.category')),
                ('likes', models.ManyToManyField(related_name='post_likes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_comments', to=settings.AUTH_USER_MODEL)),
                ('likes', models.ManyToManyField(related_name='comment_likes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
