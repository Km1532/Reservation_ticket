# Generated by Django 4.2.8 on 2024-03-22 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_review_nickname_review_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatars/'),
        ),
    ]