# Generated by Django 4.0.6 on 2022-07-15 20:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_add_category_id_to_store_product'),
    ]

    operations = [
        migrations.RunSQL("""
            CREATE TABLE store_stores (
                id serial,
                name VARCHAR(255) NOT NULL UNIQUE,
                owner VARCHAR(255) NOT NULL,
                PRIMARY KEY (id)
            );
        """, """
            DROP TABLE store_stores;
        """)
    ]
