# Generated by Django 2.1.7 on 2019-02-21 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('convert', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='history',
            old_name='history_text',
            new_name='history_url',
        ),
        migrations.AddField(
            model_name='history',
            name='history_title',
            field=models.TextField(null=True),
        ),
    ]