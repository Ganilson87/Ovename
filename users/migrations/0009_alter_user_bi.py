# Generated by Django 4.1.5 on 2023-01-27 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_user_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='bi',
            field=models.CharField(max_length=15),
        ),
    ]