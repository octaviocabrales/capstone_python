class BasePage:
    def __init__(self, driver) :
        self.driver = driver

    def open_window(self):
        self.driver.maximize_window()