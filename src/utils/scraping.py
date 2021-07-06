import urllib
from bs4 import BeautifulSoup


def get_soup(url: str):

    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html, 'html.parser')
    return soup


def get_title(url: str) -> str:

    soup = get_soup(url)
    title_tag = soup.find('h1', attrs={'class': 'title mathjax'})
    title = str(title_tag.contents[1])
    return title


def get_date(url: str) -> str:

    soup = get_soup(url)
    date_tag = soup.find('div', attrs={'class': 'dateline'})
    date = str(date_tag.contents[0])
    date = date.replace('\n', '')
    date = date.replace('[', '')
    date = date.replace(']', '')

    sub_pos = date.find('Submitted on')
    date_list = date[sub_pos:].split(' ')

    month_en2num = {
        'Jan': '1', 'Feb': '2', 'Mar': '3',
        'Apr': '4', 'May': '5', 'Jun': '6',
        'Jul': '7', 'Aug': '8', 'Sep': '9',
        'Oct': '10', 'Nov': '11', 'Dec': '12',
    }
    day = date_list[2]
    month = month_en2num[date_list[3]]
    year = date_list[4]
    return f"{year:>04}{month:>02}{day:>02}"


def get_authors(url: str) -> str:

    soup = get_soup(url)
    authors_tag = soup.find('div', attrs={'class': 'authors'})
    authors_content = authors_tag.contents
    authors_list = []
    for i in range(1, len(authors_content), 2):
        authors_list.append(str(authors_content[i].contents[0]))
    return ', '.join(authors_list)
