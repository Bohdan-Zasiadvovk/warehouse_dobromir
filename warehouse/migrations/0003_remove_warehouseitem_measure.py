# Generated by Django 5.0 on 2024-01-20 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0002_rename_warehouse_record_item_warehouseitem_warehouse_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='warehouseitem',
            name='measure',
        ),
    ]
