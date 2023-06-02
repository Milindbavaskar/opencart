import pytest
from selenium import webdriver


@pytest.fixture()
def setup():
    driver = webdriver.Edge()
    driver.get("https://tutorialsninja.com/demo/")
    return driver



@pytest.fixture(params=[
    ("Kmahajan@xyz.com", "Test@1234", "Pass"),
    ("Kmahajan@xyz.com1", "Test@1234", "Fail"),
    ("Kmahajan@xyz.com", "Test@12341", "Fail"),
    ("Kmahajan@xyz.com1", "Test@12341", "Fail")
])
def getdataforlogin(request):
    return request.param
