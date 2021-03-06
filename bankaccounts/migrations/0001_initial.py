# Generated by Django 4.0.4 on 2022-05-02 10:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bankusers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BankAccount',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankusers.bankuser')),
            ],
        ),
    ]
