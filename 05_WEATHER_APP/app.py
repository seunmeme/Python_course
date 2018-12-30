import requests
import bs4

def main():
    print_header()
    zip_code = input('Type zipcode of the location you want weather for (23401): ')
    html = get_html_from_web(zip_code)
    get_weather_from_html(html)

def print_header():
    print('---------------------------------')
    print('           WEATHER APP')
    print('---------------------------------')
    print()

def get_html_from_web(zip_code):
    url = 'http://www.wunderground.com/weather-forecast/{}'.format(zip_code)
    response = requests.get(url)
    return response.text[0:]


def get_weather_from_html(html):
    soup = bs4.BeautifulSoup(html, 'html.parser')
    loc = soup.find(class_ = 'region-content-header').find('h1').get_text()
    condition = soup.find(class_ = 'condition-icon').get_text()
    temp = soup.find(class_ = 'wu-unit-temperature').find(class_ = 'wu-value').get_text()
    scale = soup.find(class_ = 'wu-unit-temperature').find(class_ = 'wu-label').get_text()
    print(condition, temp, scale, loc)


if __name__ == '__main__':
    main()
