# Generated by Django 5.1.7 on 2025-05-19 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='content',
            field=models.CharField(max_length=10000000, null=1),
            preserve_default=1,
        ),
    ]
