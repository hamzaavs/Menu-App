# Generated by Django 4.2.5 on 2025-02-20 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_userrole_user_roles'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserRole',
            new_name='Role',
        ),
    ]
