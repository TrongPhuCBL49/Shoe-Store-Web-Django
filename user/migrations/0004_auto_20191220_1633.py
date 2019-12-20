# Generated by Django 2.2 on 2019-12-20 09:33

from django.db import migrations
import user.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('cart', '0002_auto_20191220_1629'),
        ('order', '0002_auto_20191220_1629'),
        ('admin', '0004_auto_20191220_1629'),
        ('user', '0003_auto_20191220_1629'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='CustomerUser',
        ),
        migrations.AlterModelManagers(
            name='customeruser',
            managers=[
                ('objects', user.models.CustomerUserManager()),
            ],
        ),
    ]
