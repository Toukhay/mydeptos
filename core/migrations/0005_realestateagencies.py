# Generated by Django 4.2.5 on 2023-09-20 02:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_apartments'),
    ]

    operations = [
        migrations.CreateModel(
            name='Realestateagencies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('phone', models.IntegerField(default=15)),
                ('email', models.EmailField(max_length=100)),
                ('inmobiliaria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.apartments')),
            ],
        ),
    ]