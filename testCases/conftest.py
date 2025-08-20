from selenium import webdriver
import pytest


@pytest.fixture()
def setUp(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
        print("Launching in Chrome Browser")
    elif browser == "firefox":
        driver = webdriver.Firefox()
        print("Launching in FireFox Browser")
    return driver


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="Type in browser: chrome or firefox"
    )


@pytest.fixture()
def browser(request):  # -- This will return the browser value to setup method
    return request.config.getoption("--browser")


# Hook for Adding Environment info to HTML Report
def pytest_configure(config):
    if hasattr(config, "_metadata"):   # check if metadata is available
        config._metadata['Project Name'] = 'nop Commerce'
        config._metadata['Module Name'] = 'customers'
        config._metadata['Tester'] = 'RJ'

# Hook for delete/modify environment info in HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)   # use "Plugins" (capital P) for pytest-html 4.x