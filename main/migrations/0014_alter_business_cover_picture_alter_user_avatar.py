# Generated by Django 4.0.4 on 2022-05-22 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_alter_business_cover_picture_alter_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='cover_picture',
            field=models.ImageField(blank=True, upload_to='main/images/biz_profile'),
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='main/images/user_profile'),
        ),
    ]
