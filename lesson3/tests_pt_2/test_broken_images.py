from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def test_broken_images(driver, wait):
    driver.get("https://the-internet.herokuapp.com/")
    driver.find_element(By.CSS_SELECTOR, '#content > ul > li:nth-child(4) > a').click()

    assert driver.current_url == "https://the-internet.herokuapp.com/broken_images", "Неверная ссылка"
    print("Находимся на верной странице")

    images = driver.find_elements(By.TAG_NAME, "img")
    broken_images = []

    for image in images:
        width = driver.execute_script("return arguments[0].naturalWidth;", image)
        height = driver.execute_script("return arguments[0].naturalHeight;", image)

        if width == 0 or height == 0:
            broken_images.append(image.get_attribute("src"))

    assert len(broken_images) == 0, f"Сломанные изображения: {broken_images}"
    if broken_images:
        print("Найдены сломанные изображения:", broken_images)
    else:
        print("Все изображения загружены корректно.")

    driver.quit()