# Generated by Django 4.1.3 on 2022-12-04 08:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0002_alter_simplifiedurl_redirection_path'),
    ]

    operations = [
        migrations.RenameField(
            model_name='simplifiedurl',
            old_name='redirection_path',
            new_name='redirection_shortcut',
        ),
    ]
