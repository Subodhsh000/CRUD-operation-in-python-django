# Generated by Django 5.0 on 2024-01-01 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kakashi_app', '0002_alter_msg_email_alter_msg_mobile_alter_msg_msg_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='msg',
            name='mobile',
            field=models.BigIntegerField(),
        ),
    ]
