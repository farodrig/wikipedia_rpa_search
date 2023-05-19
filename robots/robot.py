from typing import Optional

from rich import print
from RPA.Browser.Selenium import AliasType, Selenium


class Robot:
    def __init__(self, name, browser: Optional[Selenium] = None):
        self.name = name
        self.browser = browser or Selenium()

    def say_hello(self):
        print(f"Hello, my name is {self.name} :robot:")

    def say_goodbye(self):
        print(f"Goodbye, my name is {self.name}")

    def open_webpage(self, webpage) -> AliasType:
        return self.browser.open_available_browser(webpage)
