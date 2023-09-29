from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


class BaseUIMethods:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    # получение элемента
    def element_presence(self, locator: tuple[str, str], driver: WebDriver, message: str='',
                         waiting_time: int = 10) -> WebElement:
        """
        Функция на поиск элемента на странице
        """
        return WebDriverWait(driver, waiting_time).until(expected_conditions.presence_of_element_located(locator),
                                                         message=message)

    # получение текста элемента
    def element_text(self, locator: tuple[str, str], driver: WebDriver, message: str, waiting_time: int = 10):
        element = self.element_presence(locator, driver, message, waiting_time)
        return element.get_attribute('innerText')

    # получение значения элемента
    def get_value(self, locator: tuple[str, str], driver: WebDriver, message: str, waiting_time: int = 10):
        element = self.element_presence(locator, driver, message, waiting_time)
        return element.get_attribute('value')

    # получение всех элементов
    def list_of_element_presence(self, locator: tuple[str, str], driver: WebDriver, message: str,
                                 waiting_time: int = 10) -> WebElement:
        return WebDriverWait(driver, waiting_time).until(expected_conditions.presence_of_all_elements_located(locator),
                                                         message=message)

    # кликать по элементу
    def click_element(self, locator: tuple[str, str], driver: WebDriver, message: str,
                      waiting_time: int = 10):
        self.element_presence(locator, driver, message, waiting_time).click()

    # кликабельный ли элемент
    def element_to_be_clickable(self, locator: tuple[str, str], driver: WebDriver, message: str,
                                waiting_time: int = 10):
        return WebDriverWait(driver, waiting_time).until(expected_conditions.element_to_be_clickable(locator),
                                                         message=message)

    # не кликательный элемент
    def element_not_to_be_clickable(self, locator: tuple[str, str], driver: WebDriver, message: str,
                                    waiting_time: int = 10):
        return WebDriverWait(driver, waiting_time).until_not(expected_conditions.element_to_be_clickable(locator),
                                                             message=message)

    # видимость элемента на странице
    def visibility_of_element_located(self, locator: tuple[str, str], driver: WebDriver, message: str,
                                      waiting_time: int = 10):
        return WebDriverWait(driver, waiting_time).until(expected_conditions.visibility_of_element_located(locator),
                                                         message=message)

    # если элемент откреплен в ДОМ
    def staleness(self, locator: tuple[str, str], driver: WebDriver, message: str,
                  waiting_time: int = 10):
        return WebDriverWait(driver, waiting_time).until(expected_conditions.staleness_of(locator),
                                                         message=message)
    #обновление страницы
    def refresh_page(self):
        current_url = self.driver.current_url
        self.driver.refresh()
        assert current_url == self.driver.current_url

