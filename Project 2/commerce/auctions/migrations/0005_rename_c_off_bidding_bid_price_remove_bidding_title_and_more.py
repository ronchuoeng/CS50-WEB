# Generated by Django 4.1.2 on 2022-11-16 09:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_bidding'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bidding',
            old_name='c_off',
            new_name='bid_price',
        ),
        migrations.RemoveField(
            model_name='bidding',
            name='title',
        ),
        migrations.AddField(
            model_name='listing',
            name='c_off',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bidprices', to='auctions.bidding'),
        ),
    ]