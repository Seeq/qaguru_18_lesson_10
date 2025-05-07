import allure
from selene import browser, by, have
from selene.support.shared.jquery_style import s

from pages.github_pages import GitHubPage

page = GitHubPage()


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
    page.open_main_page()
    page.search_repo()
    page.open_repo_page()
    page.open_issue_page()
    page.should_see_issue_name()


def test_with_annotations():
    page.open_main_page()
    page.search_repo()
    page.open_repo_page()
    page.open_issue_page()
    page.should_see_issue_name()
