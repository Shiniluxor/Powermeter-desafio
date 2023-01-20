import pytest
import test_helpers

from django.urls import reverse


pytestmark = [pytest.mark.django_db]


def tests_Medidores_list_view(client):
    instance1 = test_helpers.create_medidores_Medidores()
    instance2 = test_helpers.create_medidores_Medidores()
    url = reverse("medidores_Medidores_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Medidores_create_view(client):
    url = reverse("medidores_Medidores_create")
    data = {
        "nombre": "text",
        "llave_id": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Medidores_detail_view(client):
    instance = test_helpers.create_medidores_Medidores()
    url = reverse("medidores_Medidores_detail", args=[instance.Id, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Medidores_update_view(client):
    instance = test_helpers.create_medidores_Medidores()
    url = reverse("medidores_Medidores_update", args=[instance.Id, ])
    data = {
        "nombre": "text",
        "llave_id": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Mediciones_list_view(client):
    instance1 = test_helpers.create_medidores_Mediciones()
    instance2 = test_helpers.create_medidores_Mediciones()
    url = reverse("medidores_Mediciones_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Mediciones_create_view(client):
    medidor_id = test_helpers.create_medidores_Medidores()
    url = reverse("medidores_Mediciones_create")
    data = {
        "consumo_reg": "text",
        "medidor_id": medidor_id.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Mediciones_detail_view(client):
    instance = test_helpers.create_medidores_Mediciones()
    url = reverse("medidores_Mediciones_detail", args=[instance.id, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Mediciones_update_view(client):
    medidor_id = test_helpers.create_medidores_Medidores()
    instance = test_helpers.create_medidores_Mediciones()
    url = reverse("medidores_Mediciones_update", args=[instance.id, ])
    data = {
        "consumo_reg": "text",
        "medidor_id": medidor_id.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302
