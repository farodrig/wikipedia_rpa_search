from datetime import date, datetime, timedelta
from typing import Optional

from RPA.Browser.Selenium import Selenium
from selenium.webdriver.remote.webelement import WebElement
from yarl import URL

from config import WIKIPEDIA_URL
from DTO.person_profile import PersonProfile
from robots.robot import Robot

class WikipediaRobot(Robot):
    BASE_URL: URL = WIKIPEDIA_URL

    def __init__(self, browser: Optional[Selenium] = None):
        super().__init__("Wikipedia Robot", browser)

    def find_article(self, word: str):
        self.open_webpage(str(self.BASE_URL))
        old_timeout = self.browser.get_selenium_timeout()
        self.browser.set_selenium_timeout(timedelta(seconds=1))
        search_input_locator = '//*[@id="searchform"]/div/div/div[1]/input'
        try:
            self.browser.wait_until_element_is_visible(search_input_locator, )
        except AssertionError as ex:
            self.browser.click_element_if_visible('//*[@id="p-search"]/a')
        try:
            self.browser.input_text_when_element_is_visible(search_input_locator, word)
        except AssertionError as ex:
            self.browser.input_text_when_element_is_visible('//*[@id="searchInput"]', word)
        self.browser.click_button_when_visible('//*[@id="searchform"]/div/button')
        self.browser.set_selenium_timeout(old_timeout)
   

class PersonWikipediaRobot(WikipediaRobot):
    PROFILE_INFOBOX_LOCATOR = '//*[@id="mw-content-text"]/div[1]/table[@class="infobox biography vcard"]'

    def find_person(self, person_name: str) -> PersonProfile:
        self.find_article(person_name)
        return PersonProfile(
            name=self._find_person_name(),
            description=self._find_person_description(),
            birth_date=self._find_person_birthdate(),
            death_date=self._find_person_death_date(),
        )

    def _find_person_description(self) -> Optional[str]:
        first_stanza_locator = f'{self.PROFILE_INFOBOX_LOCATOR}/following-sibling::p[1]'
        self.browser.wait_until_element_is_visible(first_stanza_locator)
        return self.browser.get_text(first_stanza_locator)

    def _find_person_name(self) -> Optional[str]:
        name_locator = f'{self.PROFILE_INFOBOX_LOCATOR}/tbody/tr[1]/th/div'
        self.browser.wait_until_element_is_visible(name_locator)
        return self.browser.get_text(name_locator)
    
    def _find_person_birthdate(self) -> Optional[date]:
        element = self._find_person_data_from_infobox('Born')
        if not element: 
            return None
        for potencial_birthdate_str in element.text.split('\n'):
            potencial_birthdate_str = potencial_birthdate_str.split(' [')[0]
            try:
                birthdate = datetime.strptime(potencial_birthdate_str, '%d %B %Y').date()
            except ValueError as e:
                continue
            else:
                return birthdate
        return None

    def _find_person_death_date(self) -> Optional[date]:
        element = self._find_person_data_from_infobox('Died')
        if not element: 
            return None
        for potencial_death_date_str in element.text.split('\n'):
            potencial_death_date_str = potencial_death_date_str.split(' (')[0]
            try:
                death_date = datetime.strptime(potencial_death_date_str, '%d %B %Y').date()
            except ValueError as e:
                continue
            else:
                return death_date
        return None
    
    def _find_person_data_from_infobox(self, key: str) -> Optional[WebElement]:
        locator = f'{self.PROFILE_INFOBOX_LOCATOR}/tbody/tr/th[text()="{key}"]/following-sibling::td'
        try:
            self.browser.wait_until_element_is_visible(locator)
        except AssertionError as ex:
            return None
        else:
            return self.browser.find_element(locator)
