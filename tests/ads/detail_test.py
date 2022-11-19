import pytest
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lesson28.settings')
import django
django.setup()



@pytest.mark.django_db
def test_ad_retrieve(client, ad, user_token):
    expected_response = {
        "id": ad.id,
        "author": ad.author.username,
        "name": ad.name,
        "price": ad.price,
        "description": None,
        "is_published": False,
        "category": ad.category.name,
        "image": None
    }

    response = client.get(
        f"/ad/{ad.pk}/",
        HTTP_AUTHORIZATION='Bearer ' + user_token
    )

    assert response.status_code == 200
    assert response.data == expected_response
