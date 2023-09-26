# Generated by Django 4.2.5 on 2023-09-25 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userApp', '0002_alter_user_email_alter_user_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'normal'), (2, 'admin')], default=1, null=True),
        ),
    ]
