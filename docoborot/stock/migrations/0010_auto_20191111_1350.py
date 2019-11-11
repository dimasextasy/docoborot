# Generated by Django 2.2.6 on 2019-11-11 08:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0009_auto_20191015_1238'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
            ],
            options={
                'ordering': ['-pk'],
            },
        ),
        migrations.CreateModel(
            name='DealType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=120)),
            ],
            options={
                'ordering': ['-pk'],
            },
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('surname', models.CharField(max_length=120)),
                ('patronymic', models.CharField(max_length=120)),
                ('company_name', models.CharField(max_length=120)),
            ],
            options={
                'ordering': ['-pk'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('title', models.CharField(max_length=120)),
                ('purchase_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('selling_field', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='stock.StockItem')),
            ],
            options={
                'ordering': ['-pk'],
            },
        ),
        migrations.CreateModel(
            name='DealProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.DecimalField(decimal_places=2, max_digits=10)),
                ('deal_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='stock.Deal')),
                ('product_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='stock.Product')),
            ],
            options={
                'ordering': ['-pk'],
            },
        ),
        migrations.AddField(
            model_name='deal',
            name='deal_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='stock.DealType'),
        ),
        migrations.AddField(
            model_name='deal',
            name='partner_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='stock.Partner'),
        ),
    ]
