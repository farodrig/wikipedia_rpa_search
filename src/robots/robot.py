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
        alias = self.browser.open_available_browser(webpage, headless=True)
        self.browser.set_window_size(width=1920, height=1200)
        return alias
