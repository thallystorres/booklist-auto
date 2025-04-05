import csv
from pathlib import Path

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ROOT_FOLDER = Path(__file__).parent
DRIVER_FILE = ROOT_FOLDER / 'drivers' / 'chromedriver.exe'


def make_chrome_browser(*options: str) -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()

    if options is not None:
        for option in options:
            chrome_options.add_argument(option)

    chrome_service = Service(executable_path=str(DRIVER_FILE))
    chrome_browser = webdriver.Chrome(
        service=chrome_service,
        options=chrome_options,
    )
    return chrome_browser


def scrape_single_page(browser: webdriver.Chrome):
    books_data = []
    books = browser.find_elements(By.CSS_SELECTOR, '.product_pod')
    for book in books:
        title = book.find_element(
            By.CSS_SELECTOR, 'h3 a').get_attribute('title')
        price = book.find_element(By.CLASS_NAME, 'price_color').text
        availability = book.find_element(
            By.CSS_SELECTOR, '.instock.availability').text.strip()
    rating_element = book.find_element(By.CSS_SELECTOR, 'p.star-rating')
    class_attr = rating_element.get_attribute('class')
    rating = class_attr.split()[-1] if class_attr else 'No rating'
    book_dict = {
        'title': title,
        'price': price,
        'availability': availability,
        'rating': rating
    }
    books_data.append(book_dict)
    return books_data


if __name__ == '__main__':
    options = ()
    browser = make_chrome_browser(*options)
    browser.get('http://books.toscrape.com')
    books_pages = []
    csv_file = ROOT_FOLDER / 'books.csv'
    while True:
        books_pages.append(scrape_single_page(browser))
        try:
            button = browser.find_element(By.CLASS_NAME, 'next')
            next_link = button.find_element(By.TAG_NAME, 'a')
            next_link.click()
        except NoSuchElementException:
            with open(csv_file, 'w', encoding='utf-8', newline='') as file:
                write = csv.DictWriter(
                    file,
                    fieldnames=['title', 'price', 'availability', 'rating'])
                write.writeheader()
                for books in books_pages:
                    for book in books:
                        write.writerow(book)
            print("Fim da paginação")
            break
