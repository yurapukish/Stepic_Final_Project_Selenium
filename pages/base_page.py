class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser, self.url = browser, url
        self.browser.implicitly_wait(timeout)
    
    def open(self):
        self.browser.get(self.url)