# Generated by Django 3.1.7 on 2021-03-11 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0004_auto_20210311_0716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='telegram_user_id',
            field=models.BigIntegerField(db_index=True, default=0),
        ),
    ]