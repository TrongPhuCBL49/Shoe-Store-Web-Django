# Generated by Django 2.2.5 on 2019-11-28 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20191123_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='parent_Id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='parent_Ids', to='product.Category'),
        ),
    ]
