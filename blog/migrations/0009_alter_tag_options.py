# Generated by Django 3.2.6 on 2022-11-13 18:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_tag_value'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['value']},
        ),
    ]
