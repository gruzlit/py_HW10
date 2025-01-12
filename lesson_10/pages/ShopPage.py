import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

@allure.epic("HW10")
@allure.feature("Стоимость товаров")
class ShopPage:

    def __init__(self, driver):
        self._driver = driver

    @allure.step("Открыть страницу.")
    def open_pages(self):
        """
        Эта функция открывает страницу.
        :return: Страница открыта.
        """
        self._driver.get("https://www.saucedemo.com/")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    @allure.step("Авторизировать пользователя.")
    def authorization(self):
        """
        Эта функция авторизирует пользователя.
        :return: [ user-name = standard_user,password = secret_sauce]
        """
        self._driver.find_element(By.CSS_SELECTOR, "[id = user-name]").send_keys("standard_user")
        self._driver.find_element(By.CSS_SELECTOR, "[id = password]").send_keys("secret_sauce")

    @allure.step("Нажать на кнопку 'submit'")
    def click_submit(self):
        """
        Эта функция находит кнопку "submit"
        :return: Кнопка отработала.
        """
        WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[type = submit]'))
        )
        self._driver.find_element(By.CSS_SELECTOR, "[type = submit]").click()

    @allure.step("Добавить товары в корзину.")
    def add_product(self):
        """
        "Эта функция добавляет товары в корзину.
        :return: [add-to-cart-sauce-labs-backpack,add-to-cart-sauce-labs-bolt-t-shirt, add-to-cart-sauce-labs-onesie]
        """
        self._driver.find_element(By.CSS_SELECTOR, "[id = add-to-cart-sauce-labs-backpack]").click()
        self._driver.find_element(By.CSS_SELECTOR, "[id = add-to-cart-sauce-labs-bolt-t-shirt]").click()
        self._driver.find_element(By.CSS_SELECTOR, "[id = add-to-cart-sauce-labs-onesie]").click()

    @allure.step("Перейти в корзину.")
    def go_to_cart(self):
        """
        Эта функция позволяет перейти в корзину.
        :return:[shopping_cart_container]
        """
        self._driver.find_element(By.CSS_SELECTOR, "[id = shopping_cart_container]").click()

    @allure.step("Нажать кнопку 'checkout'")
    def checkout(self):
        """
        Эта функция позволяет найти кнопку "checkout" и кликнуть на нее.
        :return: Кнопка отрабатывает.
        """
        self._driver.find_element(By.CSS_SELECTOR, "[id = checkout]").click()

    @allure.step("Заполнить поля своими данными")
    def data_entry(self):
        """
        Эта функция заполряет поля своими данными.
        :return:[first-name, last-name, postal-code]
        """
        self._driver.find_element(By.CSS_SELECTOR, "[id = first-name]").send_keys("Владимир")
        self._driver.find_element(By.CSS_SELECTOR, "[id = last-name]").send_keys("Ахалкаци")
        self._driver.find_element(By.CSS_SELECTOR, "[id = postal-code]").send_keys("647000")

    @allure.step("Нажать кнопку 'continue'")
    def continue_click(self):
        """
        Эта функция находит кнопку "continue" и кликает на нее.
        :return:Кнопка отрабатывает.
        """
        self._driver.find_element(By.CSS_SELECTOR, "[id = continue]").click()

    @allure.step("Прочитать со страницы итоговую стоимость")
    def get_total(self):
        """
        Эта функция проверяет итоговую стоимость.
        :return:[total]
        """
        total = self._driver.find_element(By.CSS_SELECTOR, "div.summary_total_label").text
        assert total == 'Total: $58.29'

    @allure.step("Нажать кнопку 'finish'")
    def click_finish(self):
        """
        Эта функция находит кнопку "finish" и кликает на нее.
        :return:Кнопка отрабатывает.
        """
        self._driver.find_element(By.CSS_SELECTOR, "[id = finish]").click()

    @allure.step("Закрыть браузер")
    def close_driver(self):
        """
        Эта функция выхода.
        :return:quit
        """
        self._driver.quit()
