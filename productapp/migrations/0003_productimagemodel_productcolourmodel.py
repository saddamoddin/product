# Generated by Django 4.1.4 on 2022-12-29 12:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0002_rename_productmainmodel1_productmainmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='productImageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(upload_to='images')),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_img_details', to='productapp.productmainmodel')),
            ],
        ),
        migrations.CreateModel(
            name='productColourModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Colour', models.CharField(max_length=100)),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_details', to='productapp.productmainmodel')),
            ],
        ),
    ]
