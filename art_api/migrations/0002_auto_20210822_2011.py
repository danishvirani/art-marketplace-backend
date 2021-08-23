# Generated by Django 3.2.6 on 2021-08-22 20:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('art_api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='art',
        ),
        migrations.AlterField(
            model_name='art',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='art', to='art_api.artist'),
        ),
        migrations.AlterField(
            model_name='art',
            name='image',
            field=models.CharField(max_length=200),
        ),
    ]