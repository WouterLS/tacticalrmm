# Generated by Django 3.0.2 on 2020-01-12 00:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0015_agent_is_updating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agent',
            name='status',
        ),
    ]
