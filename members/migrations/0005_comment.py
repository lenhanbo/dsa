# Generated by Django 5.1.7 on 2025-04-08 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0004_user_display_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=1000, null=True)),
                ('Comment', models.CharField(max_length=1000, null=True)),
            ],
        ),
    ]
