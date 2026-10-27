import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

# Регистрация параметров для командной строки
def pytest_addoption(parser): # Позволяет нам добавлять собственные команды для терминала
    # Опция выбора браузера, parser.addoption(...): Создает новые флаги запуска.
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    # Опция для передачи языка из командной строки
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: ru, en, fr, es, etc.")

# Объявление фикстуры и считывание параметров
@pytest.fixture(scope="function")
def browser(request): # Объявляем функцию фикстуры. request — это объект pytest, умееющий собирать инфо о текущем запуске.
    browser_name = request.config.getoption("browser_name") # Метод «вытаскивает» из консоли то, что туда ввел пользователь при запуске
    user_language = request.config.getoption("language")
    browser = None # Заготовка, тут будет открытый браузер
    
    if browser_name == "chrome":
        print(f"\nstart chrome browser for test with language: {user_language}..")
        # Настройка опций для Chrome
        options = ChromeOptions()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
        
    elif browser_name == "firefox":
        print(f"\nstart firefox browser for test with language: {user_language}..")
        # Настройка опций для Firefox
        options = FirefoxOptions()
        options.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(options=options)
        
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
        
    yield browser
    print("\nquit browser..")
    browser.quit()
