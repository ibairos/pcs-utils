from utils import Logger
from .base import init_driver
from selenium import webdriver
import json


BASE_URL: str = "https://www.procyclingstats.com/race/{race_name}/{year}/{args}"
STAGE_URL: str = BASE_URL.format(args = "stage-{stage}")
STAGE_GC_URL: str = BASE_URL.format(args = "stage-{stage}-gc")
FINAL_GC_URL: str = BASE_URL.format(args = "gc")
FINAL_POINTS_URL: str = BASE_URL.format(args = "points")
FINAL_KOM_URL: str = BASE_URL.format(args = "kom")
FINAL_YOUTH_URL: str = BASE_URL.format(args = "youth")
FINAL_TEAMS_URL: str = BASE_URL.format(args = "teams")


def scrap_stage(race_name: str, year: int, stage: int) -> list:
    logger = Logger()
    driver: webdriver = init_driver(logger)

    url = STAGE_URL.format(race_name = race_name, year = year, stage = stage)
    driver.get(url)

    results = list()

    # TODO obtain the results
    
    # Close the driver
    driver.close()

    return results


def scrap_stage_gc(race_name: str, year: int, stage: int) -> list:
    logger = Logger()
    driver: webdriver = init_driver(logger)

    url = STAGE_GC_URL.format(race_name = race_name, year = year, stage = stage)
    driver.get(url)

    results = list()

    # TODO obtain the results
    
    # Close the driver
    driver.close()

    return results


def scrap_final_gc(race_name: str, year: int) -> list:
    logger = Logger()
    driver: webdriver = init_driver(logger)

    url = FINAL_GC_URL.format(race_name = race_name, year = year)
    driver.get(url)

    results = list()

    # TODO obtain the results
    
    # Close the driver
    driver.close()

    return results


def scrap_final_points(race_name: str, year: int) -> list:
    logger = Logger()
    driver: webdriver = init_driver(logger)

    url = FINAL_POINTS_URL.format(race_name = race_name, year = year)
    driver.get(url)

    results = list()

    # TODO obtain the results
    
    # Close the driver
    driver.close()

    return results


def scrap_final_kom(race_name: str, year: int) -> list:
    logger = Logger()
    driver: webdriver = init_driver(logger)

    url = FINAL_KOM_URL.format(race_name = race_name, year = year)
    driver.get(url)

    results = list()

    # TODO obtain the results
    
    # Close the driver
    driver.close()

    return results


def scrap_final_youth(race_name: str, year: int) -> list:
    logger = Logger()
    driver: webdriver = init_driver(logger)

    url = FINAL_YOUTH_URL.format(race_name = race_name, year = year)
    driver.get(url)

    results = list()

    # TODO obtain the results
    
    # Close the driver
    driver.close()

    return results


def scrap_final_teams(race_name: str, year: int) -> list:
    logger = Logger()
    driver: webdriver = init_driver(logger)

    url = FINAL_YOUTH_URL.format(race_name = race_name, year = year)
    driver.get(url)

    results = list()

    # TODO obtain the results
    
    # Close the driver
    driver.close()

    return results