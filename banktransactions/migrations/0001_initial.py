# Generated by Django 4.0.4 on 2022-05-02 10:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bankusers', '0001_initial'),
        ('bankaccounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BankTransactions',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('transaction_action', models.CharField(max_length=100)),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('account', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='bankaccounts.bankaccount')),
                ('users', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='bankusers.bankuser')),
            ],
        ),
    ]