# Generated by Django 3.2.6 on 2021-08-25 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('art_api', '0004_alter_user_use'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='use',
            field=models.CharField(max_length=32),
        ),
    ]