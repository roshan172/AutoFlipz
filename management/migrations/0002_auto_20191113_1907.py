# Generated by Django 2.2.6 on 2019-11-13 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarBrand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brandName', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Car Brands',
                'verbose_name_plural': 'Car Brands',
            },
        ),
        migrations.AddField(
            model_name='application',
            name='vehicleNumber',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelName', models.CharField(max_length=200)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.CarBrand')),
            ],
            options={
                'verbose_name': 'Car Models',
                'verbose_name_plural': 'Car Models',
            },
        ),
        migrations.AddField(
            model_name='application',
            name='carBrand',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='management.CarBrand'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='application',
            name='carModel',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='management.CarModel'),
            preserve_default=False,
        ),
    ]
