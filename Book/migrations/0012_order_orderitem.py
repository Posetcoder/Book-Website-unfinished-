# Generated by Django 4.0.3 on 2022-03-11 06:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0011_book_externalbuy'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(default=0)),
                ('status', models.CharField(default='created', max_length=50)),
                ('address', models.TextField(blank=True, null=True)),
                ('contactnum', models.CharField(blank=True, max_length=15, null=True)),
                ('paymentrefnum', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Book.book')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Book.order')),
            ],
        ),
    ]
