# Generated by Django 4.0 on 2021-12-14 08:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('nft_management', '0001_initial'),
        ('admin_site_management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='faq',
            name='category_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='nft_management.category'),
        ),
    ]