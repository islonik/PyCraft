# Generated by Django 5.0.3 on 2024-05-05 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lemon', '0004_alter_cart_token'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='token',
            new_name='user',
        ),
    ]