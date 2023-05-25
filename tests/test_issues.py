import allure
from allure_commons.types import Severity
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s

'''Чистый Selene'''


def test_issues_github(browser_configuration):
    browser.open('https://github.com')
    s('.header-search-input').click()
    s('.header-search-input').send_keys('eroshenkoam/allure-example')
    s('.header-search-input').submit()
    s(by.link_text('eroshenkoam/allure-example')).click()
    s('#issues-tab').click()
    s(by.partial_text('#80')).should(be.visible)


'''Лямбда шаги'''


def test_issues_dynamic_steps(browser_configuration):
    with allure.step('Открываем браузер'):
        browser.open('https://github.com')

    with allure.step('Находим репозиторий'):
        s('.header-search-input').click()
        s('.header-search-input').send_keys('eroshenkoam/allure-example')
        s('.header-search-input').submit()
        s(by.link_text('eroshenkoam/allure-example')).click()

    with allure.step('Открыть issues-tab'):
        s('#issues-tab').click()

    with allure.step('Проверить наличие issues под номером #80'):
        s(by.partial_text('#80')).should(be.visible)


'''Шаги с декоратором @allure.step'''


def test_issues_decorator_steps(browser_configuration):
    open_main_page()
    search_for_repository('eroshenkoam/allure-example')
    go_to_repository('eroshenkoam/allure-example')
    open_issue_tab()
    should_see_issue_with_number('#80')


@allure.step('Открыть главную страницу')
def open_main_page():
    browser.open('https://github.com')


@allure.step('Найти репозиторий {repo}')
def search_for_repository(repo):
    browser.element('.header-search-input').click()
    browser.element('.header-search-input').send_keys(repo)
    browser.element('.header-search-input').submit()


@allure.step('Перейти по ссылке репозитория {repo}')
def go_to_repository(repo):
    browser.element(by.link_text(repo)).click()


@allure.step('Открыть таб Issues')
def open_issue_tab():
    browser.element('#issues-tab').click()


@allure.step('Проверить наличие Issue {number}')
def should_see_issue_with_number(number):
    browser.element(by.partial_text(number)).should(be.visible)


def test_github_dynamic_labels():
    allure.dynamic.tag('web')
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.feature('Задачи в репозитории')
    allure.dynamic.story('Неавторизованный пользователь не может создать задачу в репозитории')
    allure.dynamic.link('https://github.com', name='Testing')


'''Шаги с лейблами'''


@allure.tag('critical')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'Roman Satymbaev')
@allure.feature('Задачи')
@allure.story('Авторизованный пользователь может создать задачу в репозитории')
@allure.link('https://github.com', name='Testing')
def test_github_decorator_labels():
    pass
    ...
