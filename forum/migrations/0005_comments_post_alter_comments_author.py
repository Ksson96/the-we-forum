# Generated by Django 4.0.2 on 2022-02-28 12:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forum', '0004_alter_post_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='post',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='post_comments', to='forum.post'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comments',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_comments', to=settings.AUTH_USER_MODEL),
        ),
    ]
