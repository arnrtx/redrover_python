from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def test_add_remove_elements(driver, wait):
    driver.get("https://the-internet.herokuapp.com/")
    driver.find_element(By.CSS_SELECTOR, '#content > ul > li:nth-child(2) > a').click()

    assert driver.current_url == "https://the-internet.herokuapp.com/add_remove_elements/", "Неверная ссылка"
    print("Находимся на верной странице")

    try:
        delete_button = driver.find_element(By.XPATH, '//*[text()="Delete"]')
        assert False, "Кнопка 'Delete' должна отсутствовать до добавления элемента."
    except NoSuchElementException:
        print("Кнопка 'Delete' отсутствует до добавления элемента")

    add_button = driver.find_element(By.XPATH, '//*[text()="Add Element"]')
    add_button.click()
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[text()="Delete"]')))

    delete_button = driver.find_element(By.XPATH, '//*[text()="Delete"]')
    delete_button.click()
    wait.until(EC.invisibility_of_element(delete_button))

    try:
        delete_button = driver.find_element(By.XPATH, '//*[text()="Delete"]')
        assert False, "Кнопка 'Delete' должна исчезнуть после удаления элемента."
    except NoSuchElementException:
        print("Кнопка 'Delete' исчезла после удаления элемента")

    driver.quit()
