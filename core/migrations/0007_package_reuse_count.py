# Generated by Django 5.0.6 on 2024-06-12 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_package_recipient_alter_package_sender'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='reuse_count',
            field=models.IntegerField(default=0),
        ),
    ]
