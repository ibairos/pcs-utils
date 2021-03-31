from utils import Logger
from .base import init_driver
from selenium import webdriver
import json


BASE_URL: str = "https://www.procyclingstats.com/teams.php?{args}"
TEAMS_BY_YEAR_URL: str = BASE_URL.format(args = "year={year}")


def scrap_teams_by_year(year: int) -> list:
    logger = Logger()
    driver: webdriver = init_driver(logger)

    url = TEAMS_BY_YEAR_URL.format(year = year)
    driver.get(url)
    
    elements = driver.find_elements_by_xpath(
        "//ul[contains(@class, 'list') and contains(@class, 'fs14') and contains(@class, 'columns2') and contains(@class, 'mob_columns1')]")

    # Get the teams from each category
    teams = list()
    for uci_category in elements:
        for team_element in uci_category.find_elements_by_xpath(".//li"):
            team = dict()
            link = team_element.find_element_by_xpath(".//a")
            team['link'] = link.get_attribute('href')
            team['name'] = link.text
            team['riders'] = list()
            teams.append(team)

    # Get the img and the riders from each team
    for team in teams:
        driver.get(team['link'])
        for infolist_element in driver.find_elements_by_xpath("//ul[contains(@class, 'infolist')]"):
            if infolist_element.text == 'Shirt:':
                team['img'] = infolist_element.find_element_by_xpath(".//img").get_attribute('src')

        riders = driver.find_element_by_xpath("//ul[contains(@class, 'list') and contains(@class, 'pad2')]").find_elements_by_xpath(".//li")
        for rider_element in riders:
            rider = dict()
            rider_link = rider_element.find_element_by_xpath(".//a")
            rider['link'] = rider_link.get_attribute('href')
            rider['preferred_name'] = rider_link.get_attribute('innerHTML')
            team['riders'].append(rider)

    # Get the information of each rider
    for team in teams:
        for rider in team['riders']:
            driver.get(rider['link'])
            rider['img'] = driver.find_element_by_xpath("//div[contains(@class, 'rdr-img-cont')]").find_element_by_xpath(".//img").get_attribute('src')
            rider['country'] = driver.find_element_by_xpath("//div[contains(@class, 'rdr-info-cont')]").find_element_by_xpath(".//a[contains(@class, 'black')]").get_attribute('innerHTML')

    # Close the driver
    driver.close()

    return teams

