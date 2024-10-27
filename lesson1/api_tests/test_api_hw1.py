import requests
import logging
import allure
import pytest

# Конфигурация логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

BASE_URL = "http://127.0.0.1:8000"  # Адрес API
AUTH = ('username', 'password')  # Учетные данные для аутентификации

@pytest.fixture(scope='module')
def test_data():
    return {
        "name": "Test Case 1",
        "description": "Description of test case 1",
        "steps": ["Step 1", "Step 2"],
        "expected_result": "Expected result",
        "priority": "средний"
    }

@allure.feature('Test Cases')
@allure.story('Create a Test Case')
def test_create_test_case(test_data):
    logger.info("Создание тест-кейса: %s", test_data)
    response = requests.post(f"{BASE_URL}/testcases/", json=test_data, auth=AUTH)

    logger.info("Ответ: %s", response.json())
    assert response.status_code == 200
    assert response.json()["name"] == test_data["name"]

@allure.feature('Test Cases')
@allure.story('Get All Test Cases')
def test_get_all_test_cases():
    response = requests.get(f"{BASE_URL}/testcases/", auth=AUTH)
    logger.info("Ответ на получение всех тест-кейсов: %s", response.json())

    assert response.status_code == 200
    assert isinstance(response.json(), list)

@allure.feature('Test Cases')
@allure.story('Get a Single Test Case')
def test_get_single_test_case():
    response = requests.get(f"{BASE_URL}/testcases/0", auth=AUTH)
    logger.info("Ответ на получение тест-кейса 0: %s", response.json())

    if response.status_code == 200:
        assert response.json()["id"] == 0
    else:
        assert response.status_code == 404

@allure.feature('Test Cases')
@allure.story('Update a Test Case')
def test_update_test_case():
    updated_data = {
        "id": 0,
        "name": "Updated Test Case",
        "description": "Updated description",
        "steps": ["Updated Step 1", "Updated Step 2"],
        "expected_result": "Updated result",
        "priority": "высокий"
    }
    logger.info("Обновление тест-кейса с ID 0: %s", updated_data)
    response = requests.put(f"{BASE_URL}/testcases/0", json=updated_data, auth=AUTH)

    logger.info("Ответ на обновление тест-кейса: %s", response.json())
    if response.status_code == 200:
        assert response.json()["name"] == updated_data["name"]
    else:
        assert response.status_code == 404

@allure.feature('Test Cases')
@allure.story('Delete a Test Case')
def test_delete_test_case():
    response = requests.delete(f"{BASE_URL}/testcases/0", auth=AUTH)
    logger.info("Ответ на удаление тест-кейса: %s", response.json())

    if response.status_code == 200:
        assert response.json()["detail"] == "Test case deleted."
    else:
        assert response.status_code == 404
