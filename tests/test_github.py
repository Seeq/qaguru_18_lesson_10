import allure
from selene import browser, by, have
from selene.support.shared.jquery_style import s


def test_selene_no_steps():
    browser.open("https://github.com")
    s('.search-input-container').click()
    s('#query-builder-test').send_keys('Seeq/qaguru_18_lesson_10')
    s('#query-builder-test').submit()
    s(by.link_text('Seeq/qaguru_18_lesson_10')).click()
    s('#issues-tab').click()
    s("[data-testid='issue-pr-title-link']").should(have.text('Not an issue actually'))


def test_steps():
    with allure.step("Открываем главную страницу"):
        browser.open("https://github.com")

    with allure.step("Ищем репозиторий"):
        s('.search-input-container').click()
        s('#query-builder-test').send_keys('Seeq/qaguru_18_lesson_10')
        s('#query-builder-test').submit()

    with allure.step("Переходим по ссылке репозитория"):
        s(by.link_text('Seeq/qaguru_18_lesson_10')).click()

    with allure.step("Открываем таб Issues"):
        s("#issues-tab").click()

    with allure.step("Проверяем наличие Issue с определенным Title"):
        s("[data-testid='issue-pr-title-link']").should(have.text('Not an issue actually'))


def test_decorator_steps():
    open_main_page()
    search_repo()
    open_repo_page()
    open_issue_page()
    should_see_issue_name()


@allure.step("Открываем главную страницу")
def open_main_page():
    browser.open("https://github.com/")


@allure.step("Ищем репозиторий")
def search_repo():
    s('.search-input-container').click()
    s('#query-builder-test').send_keys('Seeq/qaguru_18_lesson_10')
    s('#query-builder-test').submit()


@allure.step("Переходим по ссылке репозитория")
def open_repo_page():
    s(by.link_text('Seeq/qaguru_18_lesson_10')).click()


@allure.step("Открываем таб Issues")
def open_issue_page():
    s("#issues-tab").click()


@allure.step("Проверяем наличие Issue с определенным Title")
def should_see_issue_name():
    s("[data-testid='issue-pr-title-link']").should(have.text('Not an issue actually'))


@allure.tag("web")
@allure.label("owner", "Seeq")
@allure.feature("Issues")
@allure.story("Проверяем наличие Issue с Title 'Not an issue actually'")
@allure.link("https://github.com", "qa")

def test_with_annotations():
    open_main_page()
    search_repo()
    open_repo_page()
    open_issue_page()
    should_see_issue_name()
