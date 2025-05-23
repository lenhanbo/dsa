# Generated by Django 5.1.7 on 2025-05-19 01:54

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0012_remove_item_seller_delete_seller_item_seller'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='seller',
            new_name='Seller',
        ),
        migrations.AddField(
            model_name='item',
            name='author',
            field=models.ForeignKey(blank=1, null=1, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
            preserve_default=1,
        ),
    ]
