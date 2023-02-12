import requests
from requests.exceptions import MissingSchema
from scraper import handlers
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def scrape():
    resources_handler = handlers.ResourcesHandlerV1()
    items_handler = handlers.ItemsHandlerV1()

    resources = resources_handler.get_data()

    for resource in resources:
        print(f"•‎ Начинается парсинг ресурса {resource['resource_name']}")
        url = resource['resource_url']
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        for item in soup.select(resource['top_tag']):
            try:
                link = item.get('href')
                response = requests.get(link)
            except MissingSchema:
                href = item.get('href')
                link = urljoin(url, href)
                response = requests.get(link)
            soup = BeautifulSoup(response.text, 'lxml')
            title = soup.select_one(resource['title_cut'])
            date = soup.select_one(resource['date_cut'])
            body = [content.text for content in soup.select(resource['bottom_tag'])]
            items_handler.add_data(resource['id'], link, title, date, body)


if __name__ == '__main__':
    scrape()
