import os
from django.core.wsgi import get_wsgi_application
import pytest
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lesson28.settings')
application = get_wsgi_application()


@pytest.mark.django_db
def test_root_ok(client):
    response = client.get("/ad/")
    assert response.status_code == 200


@pytest.mark.django_db
def test_get_ads_id(client):
    response = client.get("/ad/1/")
    assert response.status_code == 200