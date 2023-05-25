import pytest
from selene.support.shared import browser


@pytest.fixture(scope='session', autouse=True)
def browser_configuration():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    yield browser
    browser.quit()