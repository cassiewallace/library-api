# Generated by Django 2.2.4 on 2019-09-27 20:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20190927_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='checked_out_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='checked_out_books', to=settings.AUTH_USER_MODEL),
        ),
    ]
