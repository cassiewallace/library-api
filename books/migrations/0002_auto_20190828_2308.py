# Generated by Django 2.2.4 on 2019-08-28 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=125)),
                ('author', models.CharField(max_length=125)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.DeleteModel(
            name='Books',
        ),
    ]
