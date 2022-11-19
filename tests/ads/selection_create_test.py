import pytest
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lesson28.settings')
import django
django.setup()

@pytest.mark.django_db
def test_selection_create(client, user_token, user, ad):

    data = {
        "owner": user.id,
        "name": "Test",
        "items": [ad.id]
    }

    expected_response = {
        "id": 1,
        "owner": user.id,
        "name": "Test",
        "items": [ad.id]
    }

    response = client.post(
        "/selection/create/",
        data,
        content_type='application/json',
        HTTP_AUTHORIZATION='Bearer ' + user_token
    )

    assert response.status_code == 201
    assert response.data == expected_response
