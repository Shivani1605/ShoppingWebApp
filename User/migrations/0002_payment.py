# Generated by Django 3.2.4 on 2021-07-17 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=20)),
                ('card_no', models.CharField(max_length=16)),
                ('cvv', models.CharField(max_length=4)),
                ('expiry', models.CharField(max_length=8)),
                ('balance', models.FloatField(default=10000)),
            ],
            options={
                'db_table': 'Payment',
            },
        ),
    ]