# Generated by Django 2.2 on 2020-03-10 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('databasePracticeApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wizard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('house', models.CharField(max_length=45)),
                ('pet', models.CharField(max_length=45)),
                ('year', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Movie',
        ),
    ]