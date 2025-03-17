import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Регистрация опций для командной строки
def pytest_addoption(parser):
    # Параметр для выбора браузера (оставляем как есть)
    parser.addoption(
        '--browser_name',
        action='store',
        default='chrome',
        help='Choose browser: chrome or firefox'
    )

    # Новый параметр для выбора языка
    parser.addoption(
        '--language',
        action='store',
        default='en',
        help='Choose language: en, es, fr, ru, etc.'
    )


# Фикстура для браузера (с сохранением функционала)
@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    browser = None

    # Устанавливаем язык для браузера (для Chrome)
    if browser_name == "chrome":
        print(f"\nstart chrome browser with {user_language} language...")
        options = webdriver.ChromeOptions()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)

    elif browser_name == "firefox":
        print(f"\nstart firefox browser with {user_language} language...")
        options = webdriver.FirefoxOptions()
        options.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(options=options)

    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    yield browser
    print("\nquit browser..")
    browser.quit()