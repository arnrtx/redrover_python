from selenium.webdriver.common.by import By

def test_registration(driver):
    driver.implicitly_wait(10)  # время ожидания 10 секунд

    driver.get('https://victoretc.github.io/selenium_waits/')

    visible_after_button = driver.find_element(By.ID, "startTest")
    assert visible_after_button.text == 'Начать тестирование'

    visible_after_button.click()

    result_element = driver.find_element(By.ID, "register")
    assert result_element.text == "Зарегистрироваться", "Клик не привел к ожидаемому результату"
    print("Клик по кнопке работает корректно")

    driver.get('https://victoretc.github.io/selenium_waits/')
    visible_after_button = driver.find_element(By.ID, "startTest")
    visible_after_button.click()

    login_field = driver.find_element(By.ID, "login")
    password_field = driver.find_element(By.ID, "password")
    login_field.send_keys("login")
    password_field.send_keys("password")

    assert login_field.get_attribute("value") == "login" and password_field.get_attribute(
        "value") == "password", "Текст в полях не соответствует ожидаемым"
    print("Текст введен в поля корректно")

    checkbox = driver.find_element(By.ID, "agree")
    checkbox.click()

    register_button = driver.find_element(By.ID, "register")
    register_button.click()

    loader = driver.find_element(By.ID, "loader")
    assert loader.is_displayed(), 'Лоадер не появился'
    print("Появился лоадер")

    success_text = driver.find_element(By.ID, "successMessage")
    assert success_text.is_displayed(), 'Нет сообщения об успешной регистрации'
    print("Есть сообщение об успешной регистрации")