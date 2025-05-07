# pages/github_page.py

import allure
from selene import browser, have, by


class GitHubPage:

    @allure.step("Открываем главную страницу")
    def open_main_page(self):
        browser.open("https://github.com/")

    @allure.step("Ищем репозиторий")
    def search_repo(self):
        from selene.support.shared import browser
        browser.element('.search-input-container').click()
        browser.element('#query-builder-test').send_keys('Seeq/qaguru_18_lesson_10')
        browser.element('#query-builder-test').submit()

    @allure.step("Переходим по ссылке репозитория")
    def open_repo_page(self):
        browser.element(by.link_text('Seeq/qaguru_18_lesson_10')).click()

    @allure.step("Открываем таб Issues")
    def open_issue_page(self):
        browser.element("#issues-tab").click()

    @allure.step("Проверяем наличие Issue с определенным Title")
    def should_see_issue_name(self):
        browser.element("[data-testid='issue-pr-title-link']").should(have.text('Not an issue actually'))
