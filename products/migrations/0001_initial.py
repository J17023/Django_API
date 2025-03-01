# Generated by Django 5.1.5 on 2025-01-21 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('content', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, default=99.9, max_digits=5)),
            ],
        ),
    ]
