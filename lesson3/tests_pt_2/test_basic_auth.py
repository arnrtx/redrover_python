from selenium.webdriver.common.by import By
import pyautogui
import time

def test_basic_auth(driver, wait):
    driver.get("https://the-internet.herokuapp.com/")
    driver.find_element(By.CSS_SELECTOR, '#content > ul > li:nth-child(3) > a').click()

    assert driver.current_url == "https://the-internet.herokuapp.com/basic_auth", "Неверная ссылка"
    print("Находимся на верной странице")

    username = "admin"
    password = "admin"

    pyautogui.typewrite(username)  # Ввод логина
    pyautogui.press('tab')  # Переход на поле пароля
    pyautogui.typewrite(password)  # Ввод пароля
    pyautogui.press('enter')  # Нажатие Enter для подтверждения
    time.sleep(5)  # Ждем немного, чтобы страница успела загрузиться

    success_message = driver.find_element(By.CSS_SELECTOR, "#content > div > p").text
    assert "Congratulations" in success_message, "Аутентификация не прошла успешно"
    print("Аутентификация прошла успешно")

    driver.quit()
