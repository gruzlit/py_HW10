import allure
from selenium.webdriver.common.by import By


@allure.epic("HW10")
@allure.feature("Цвета полей")
class MainPage:


    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    @allure.step("Заполнить поля.")
    def data_entry(self):
        """
         Эта функция заполняет поля значениями.
        :return:["first-name", "last-name", "address", "city", "country", "e-mail", "phone", "job-position", "company"]
        """
        self._driver.find_element(By.CSS_SELECTOR, "[name = first-name]").send_keys("Иван")
        self._driver.find_element(By.CSS_SELECTOR, "[name = last-name]").send_keys("Петров")
        self._driver.find_element(By.CSS_SELECTOR, "[name = address]").send_keys("Ленина, 55-3")
        self._driver.find_element(By.CSS_SELECTOR, "[name = e-mail]").send_keys("test@skypro.com")
        self._driver.find_element(By.CSS_SELECTOR, "[name = phone]").send_keys("+7985899998787")
        self._driver.find_element(By.CSS_SELECTOR, "[name = zip-code]").send_keys("")
        self._driver.find_element(By.CSS_SELECTOR, "[name = city]").send_keys("Москва")
        self._driver.find_element(By.CSS_SELECTOR, "[name = country]").send_keys("Россия")
        self._driver.find_element(By.CSS_SELECTOR, "[name = job-position]").send_keys("QA")
        self._driver.find_element(By.CSS_SELECTOR, "[name = company]").send_keys("SkyPro")

    @allure.step("Кликнуть на кнопку 'submit'.")
    def search_button(self):
        """
        Эта функция находит кнопку "submit".
        :return: Кнопка отработала.
        """
        self._driver.find_element(By.CSS_SELECTOR, "button[type = 'submit']").click()

    @allure.step("Проверить цвет поля 'zip-code'.")
    def get_color(self):
        """
        Эта функция проверяет ,что цвет поля zip-code подсвечен красным .
        :return: color == "rgba(132, 32, 41, 1)"
        """
        color = self._driver.find_element(By.CSS_SELECTOR, "[id = zip-code]").value_of_css_property("color")
        assert color == "rgba(132, 32, 41, 1)"

    @allure.step("Проверить цвет остальных полей полей.")
    def get_color2(self):
        """
        Эта функция проверяет , что цвет этих полей подсвечен зеленым .
        :return:color == "rgba(15, 81, 50, 1)"
        """
        elements = ["first-name", "last-name", "address", "city", "country", "e-mail", "phone", "job-position", "company"]
        for i in elements:
            color = self._driver.find_element(By.CSS_SELECTOR, "[id=%s]" % i).value_of_css_property("color")

        assert color == "rgba(15, 81, 50, 1)"

    @allure.step("Закрыть браузер")
    def close_driver(self):
        """
        Эта функция выхода
        :return: quit
        """
        self._driver.quit()