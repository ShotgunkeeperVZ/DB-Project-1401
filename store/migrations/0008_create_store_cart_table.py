# Generated by Django 4.0.6 on 2022-07-12 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_create_store_cartitem_table'),
    ]

    operations = [
        migrations.RunSQL("""
            CREATE TABLE store_cart (
                id SERIAL,
                cartitem_id INT,
                total_price INT NOT NULL DEFAULT 0 CHECK ( total_price >= 0 ),
                PRIMARY KEY (id),
                CONSTRAINT fk_cartitem
                    FOREIGN KEY (cartitem_id)
                    REFERENCES store_cartitem(id)
            );
        """, """
            DROP TABLE store_cart;
        """)
    ]
