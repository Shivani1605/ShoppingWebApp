# Generated by Django 3.2.4 on 2021-07-17 05:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Admin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('username', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'UserInfo',
            },
        ),
        migrations.CreateModel(
            name='MyCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField()),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.userinfo')),
            ],
            options={
                'db_table': 'MyCart',
            },
        ),
    ]
