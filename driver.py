from selenium import webdriver
from selenium.common import TimeoutException, StaleElementReferenceException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from config import selectors
from time import sleep

class Browser:
    def __init__(self):
        options = self._get_browser_options()
        service = Service(ChromeDriverManager().install())
        self._driver = webdriver.Chrome(service=service, options=options)
        self._wait = WebDriverWait(self._driver, 10)
        self._main_window_id = None

    def navigate_to(self, url: str) -> None:
        self._driver.get(url)
        self._main_window_id = self._driver.current_window_handle

    def click(self, selector):
        by, selector = self._get_locator_type(selector)
        for attempt in range(3): #retries
            try:
                element = self._wait.until(EC.presence_of_element_located((by, selector)))
                self._driver.execute_script("arguments[0].scrollIntoView({block:'center'});", element)
                self._wait.until(EC.element_to_be_clickable((by, selector)))
                element.click()
                return
            except (TimeoutException, StaleElementReferenceException):
                try:
                    element = self._wait.until(EC.presence_of_element_located((by, selector)))
                    self._driver.execute_script("arguments[0].click();", element) #js click
                    return
                except Exception:
                    print(f"[{attempt+1}/{3}] Refreshing page")
                    self._driver.refresh()
        raise TimeoutException(f"Cannot click element: {selector}")

    def print_opened_tab_qr_and_close(self):
        driver = self._driver
        self._wait.until(lambda d: len(d.window_handles) > 1)
        new_window_id = [i for i in driver.window_handles if i != self._main_window_id][0]
        driver.switch_to.window(new_window_id)
        driver.execute_script('window.print();')
        sleep(1)
        driver.close()
        driver.switch_to.window(self._main_window_id)

    def check_element(self, selector):
        by_method, selector = self._get_locator_type(selector)
        for attempt in range(3): #retries
            try:
                self._wait.until(EC.presence_of_element_located((by_method, selector)))
                print("Element appeared")
                return True
            except TimeoutException:
                print(f"[{attempt+1}/{3}] Refreshing page")
                self._driver.refresh()
        print("Element did not appear after all retries")
        return False

    def quit(self):
        if hasattr(self, "_driver") and self._driver:
            try:
                self._driver.quit()
            except Exception as e:
                print(f"Error when closing the browser: {e}")
            finally:
                self._driver = None

    @staticmethod
    def _get_locator_type(selector):
        selector_value = selectors[selector]

        if selector_value.startswith("//") or selector_value.startswith("./") or selector_value.startswith("("):
            by_method = By.XPATH
        elif selector_value.startswith("#"):
            by_method = By.ID
            selector_value = selector_value.replace('#', '')
        else:
            by_method = By.CSS_SELECTOR
        return by_method, selector_value

    @staticmethod
    def _get_browser_options():
        options = Options()
        options.add_argument(r"--user-data-dir=C:\All\SeleniumProfiles\User Data")
        options.add_argument('--kiosk-printing')
        options.add_argument("--profile-directory=Profile 2")
        options.add_argument("--window-size=1280,720")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)
        options.add_argument("--disable-blink-features=AutomationControlled")
        return options