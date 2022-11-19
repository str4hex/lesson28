import pytest
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lesson28.settings')
import django
django.setup()

@pytest.mark.django_db
def test_ad_create(client, user, category, ad):


    expected_response = {
            "id":2,
            "name": "Testsssssssssss",
            "price": 25,
            "description": "description",
            "is_published": False,
            "image": None,
            "author": 1,
            "category": 1

    }

    data = {
        "name": "Testsssssssssss",
        "price": 25,
        "description": "description",
        "is_published": 0,
        "image": None,
        "author": user.id,
        "category": category.id
    }


    response = client.post(
        "/ad/create/",
        data,
        content_type='application/json'
    )

    assert response.status_code == 201
    assert response.data == expected_response



