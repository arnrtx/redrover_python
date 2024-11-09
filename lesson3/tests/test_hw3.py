import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

@allure.title("Тест регистрации")
@allure.description("Проверка процесса регистрации с подтверждением сообщения об успешной регистрации")
def test_registration(driver, wait):
    with allure.step("Открытие страницы"):
        driver.get('https://victoretc.github.io/selenium_waits/')

    with allure.step("Проверка и нажатие кнопки 'Начать тестирование'"):
        visible_after_button = wait.until(EC.element_to_be_clickable((By.ID, "startTest")))
        assert visible_after_button.text == 'Начать тестирование'
        visible_after_button.click()

    with allure.step("Проверка появления кнопки 'Зарегистрироваться'"):
        result_element = wait.until(EC.visibility_of_element_located((By.ID, "register")))
        assert result_element.text == "Зарегистрироваться", "Клик не привел к ожидаемому результату"
        print("Тест пройден: клик по кнопке работает корректно")

    with allure.step("Заполнение полей 'login' и 'password'"):
        login_field = driver.find_element(By.ID, "login")
        password_field = driver.find_element(By.ID, "password")
        login_field.send_keys("login")
        password_field.send_keys("password")
        assert login_field.get_attribute("value") == "login" and password_field.get_attribute("value") == "password", "Текст в полях не соответствует ожидаемым"
        print("Текст введен в поля корректно")

    with allure.step("Выбор чекбокса и нажатие кнопки 'Зарегистрироваться'"):
        checkbox = driver.find_element(By.ID, "agree")
        checkbox.click()
        register_button = driver.find_element(By.ID, "register")
        register_button.click()

    with allure.step("Проверка появления лоадера"):
        loader = wait.until(EC.visibility_of_element_located((By.ID, "loader")))
        assert loader.is_displayed(), 'Лоадер не появился'
        print("Появился лоадер")

    with allure.step("Проверка сообщения об успешной регистрации"):
        success_text = wait.until(EC.visibility_of_element_located((By.ID, "successMessage")))
        assert success_text.is_displayed(), 'Нет сообщения об успешной регистрации'
        print("Есть сообщение об успешной регистрации")

    driver.quit()