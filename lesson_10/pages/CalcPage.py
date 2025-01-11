import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@allure.epic("HW10")
@allure.feature("Результат сложения")
class CalcPage:

    def __init__(self, driver):
        self._driver = driver

    @allure.step("Открыть страницу.")
    def open_pages(self):
        """
        Эта функция открывает страницу.
        :return: Страница открыта.
        """
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    @allure.step("Ввести значение в поле")
    def delay(self):
        """
        Эта функция очищает поле и вводит новое значение.
        Происходит задержка на время указанное в поле.
        :return:Задержка сработала.
        """
        self._driver.find_element(By.CSS_SELECTOR, "[id = delay]").clear()
        self._driver.find_element(By.CSS_SELECTOR, "[id = delay]").send_keys("45")

    @allure.step("Кликнуть на кнопки")
    def data_entry(self):
        """
        Эта функция находит  параметры и кликает на кнопки.
        :return:[param_1(7) + param_2(8) = ]
        """
        self._driver.find_element(By.XPATH, ('//span[text()="7"]')).click()
        self._driver.find_element(By.XPATH, ('//span[text()="+"]')).click()
        self._driver.find_element(By.XPATH, ('//span[text()="8"]')).click()
        self._driver.find_element(By.XPATH, ('//span[text()="="]')).click()

    @allure.step("Проверить результат")
    def get_result(self):
        """
        Эта функция показывает результат
        :return:(res == "15")
        """
        WebDriverWait(self._driver, 60).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
                                        )
        res = self._driver.find_element(By.CLASS_NAME, "screen").text
        assert res == "15"

    @allure.step("Закрыть браузер")
    def close_driver(self):
        """
        Эта функция выхода .
        :return: quit
        """
        self._driver.quit()