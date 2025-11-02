from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    chrome = playwright.chromium.launch(headless=False)
    context = chrome.new_context()
    page = context.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    email_field = page.get_by_test_id("registration-form-email-input").locator("input")
    email_field.fill("user.name@gmail.com")

    username_field = page.get_by_test_id("registration-form-username-input").locator("input")
    username_field.fill("username")

    password_field = page.get_by_test_id("registration-form-password-input").locator("input")
    password_field.fill("password")

    registration_button = page.get_by_test_id("registration-page-registration-button")
    registration_button.click()

    context.storage_state(path="registration-state.json")

with (sync_playwright() as playwright):
    chrome = playwright.chromium.launch(headless=False)
    context = chrome.new_context(storage_state="registration-state.json")
    page = context.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    courses_header = page.get_by_test_id("courses-list-toolbar-title-text")
    expect(courses_header).to_be_visible()
    expect(courses_header).to_have_text("Courses")

    no_results_block = page.get_by_test_id("courses-list-empty-view-title-text")
    expect(no_results_block).to_be_visible()
    expect(no_results_block).to_have_text("There is no results")

    no_results_icon = page.get_by_test_id("courses-list-empty-view-icon")
    expect(no_results_icon).to_be_visible()

    no_results_description = page.get_by_test_id("courses-list-empty-view-description-text")
    expect(no_results_description).to_be_visible()
    expect(no_results_description).to_have_text("Results from the load test pipeline will be displayed here")