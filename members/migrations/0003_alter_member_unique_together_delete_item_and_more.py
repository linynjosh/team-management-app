# Generated by Django 4.2.7 on 2023-12-01 00:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_member'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='member',
            unique_together={('first', 'last')},
        ),
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.DeleteModel(
            name='TodoList',
        ),
    ]
