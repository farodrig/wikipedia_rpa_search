from typing import Optional

from RPA.Browser.Selenium import AliasType, Selenium


class Robot:
    def __init__(self, name, browser: Optional[Selenium] = None):
        self.name = name
        self.browser = browser or Selenium()

    def say_hello(self):
        print("Hello, my name is " + self.name)

    def say_goodbye(self):
        print("Goodbye, my name is " + self.name)

    def open_webpage(self, webpage) -> AliasType:
        return self.browser.open_available_browser(webpage)
