# Generated by Django 5.0.3 on 2024-05-06 19:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lemon', '0005_rename_token_cart_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(default=-1)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='customer', to=settings.AUTH_USER_MODEL)),
                ('delivery', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='delivery', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='lemon.meal')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='lemon.order')),
            ],
        ),
    ]
