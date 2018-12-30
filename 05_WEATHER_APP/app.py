import requests
import bs4
import collections

WeatherReport = collections.namedtuple('WeatherReport', 'cond, temp, scale, loc')

def main():
    print_header()
    zip_code = input('Type zipcode of the location you want weather for (23401): ')
    html = get_html_from_web(zip_code)
    report = get_weather_from_html(html)
    print('The temperature in {} is {} {} and {}'.format(
        report.loc,
        report.temp,
        report.scale,
        report.cond
    ))

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
    
    loc = cleanup_text(loc)
    loc = find_city_and_state_from_location(loc)
    condition = cleanup_text(condition)
    temp = cleanup_text(temp)
    scale = cleanup_text(scale)

    # return condition, temp, scale, loc
    report = WeatherReport(cond=condition, temp=temp, scale=scale, loc=loc)
    return report


def cleanup_text(text):
    if not text:
        return text

    text = text.strip()
    return text

def find_city_and_state_from_location(loc: str):
    parts = loc.split('\n')
    return parts[0].strip()


if __name__ == '__main__':
    main()
