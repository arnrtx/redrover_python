from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def test_registration(driver, wait):
    driver.get('https://victoretc.github.io/selenium_waits/')
    visible_after_button = wait.until(EC.element_to_be_clickable((By.ID, "startTest")))
    assert visible_after_button.text == 'Начать тестирование'

    visible_after_button.click()
    result_element = wait.until(EC.visibility_of_element_located((By.ID, "register")))
    assert result_element.text == "Зарегистрироваться", "Клик не привел к ожидаемому результату"
    print("Тест пройден: клик по кнопке работает корректно")

    driver.get('https://victoretc.github.io/selenium_waits/')
    visible_after_button = wait.until(EC.element_to_be_clickable((By.ID, "startTest")))
    visible_after_button.click()

    login_field = driver.find_element(By.ID, "login")
    password_field = driver.find_element(By.ID, "password")
    login_field.send_keys("login")
    password_field.send_keys("password")
    assert login_field.get_attribute("value") == "login" and password_field.get_attribute("value") == "password", "Текст в полях не соответствует ожидаемым"
    print("Текст введен в поля корректно")

    checkbox = driver.find_element(By.ID, "agree")
    checkbox.click()

    register_button = driver.find_element(By.ID, "register")
    register_button.click()

    loader = wait.until(EC.visibility_of_element_located((By.ID, "loader")))
    assert loader.is_displayed(), 'Лоадер не появился'
    print("Появился лоадер")

    success_text = wait.until(EC.visibility_of_element_located((By.ID, "successMessage")))
    assert success_text.is_displayed(), 'Нет сообщения об успешной регистрации'
    print("Есть сообщение об успешной регистрации")