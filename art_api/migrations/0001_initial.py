# Generated by Django 3.2.6 on 2021-08-19 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Art',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('author', models.CharField(max_length=32)),
                ('rating', models.IntegerField(null=True)),
                ('image', models.CharField(max_length=32)),
                ('price', models.IntegerField()),
                ('description', models.CharField(max_length=200)),
                ('created_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('bio', models.CharField(max_length=200)),
                ('art', models.ManyToManyField(to='art_api.Art')),
            ],
        ),
    ]