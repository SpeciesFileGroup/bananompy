import requests
import bananompy
from bs4 import BeautifulSoup
from requests.exceptions import JSONDecodeError

class NoResultException(Exception):
    pass


class MustAcknowledgeTemporaryIdentifiers(Exception):
    def __init__(self):
        super().__init__("Error: to use this function, you must acknowledge that agent string identifiers are temporary, meaning that the same agent string identifier can return different data. The website will also go down every 2 weeks while new agent strings are loaded. Pass ack_temp_ids=True to dismiss this message and use the function anyway.")


def bionom_get(url, args, **kwargs):
    args = args_mapper(args)

    resp = requests.get(url, params=args, headers=get_agent(), **kwargs)
    resp.raise_for_status()
    
    try:
        return resp.json()
    except JSONDecodeError:
        return str(resp.content)


def bionom_get_agent_list(url, args, **kwargs):
    args = args_mapper(args)

    resp = requests.get(url, params=args, headers=get_agent(), **kwargs)
    resp.raise_for_status()

    soup = BeautifulSoup(resp.content, 'lxml')
    lists = soup.find_all('ul', {'class': 'list-unstyled m-2'})
    agents = []
    for list in lists:
        items = list.find_all('a')
        for a in items:
            agents.append({'id': a['href'].replace('https://bionomia.net/agent/', ''), 'name': a.text, 'url': a['href']})
    return agents


def bionom_get_agent_specimens(url, args, **kwargs):
    args = args_mapper(args)

    resp = requests.get(url, params=args, headers=get_agent(), **kwargs)
    resp.raise_for_status()

    soup = BeautifulSoup(resp.content, 'lxml')
    table = soup.find('table', {'class': 'table table-hover table-sm'})
    rows = table.find_all('tr')
    header = rows.pop(0)
    header = header.find_all('th')
    headers = []
    for col in header:
        headers.append(col.text.lower().replace(' ', '_').strip())
    specimens = []
    for row in rows:
        td = row.find_all('td')
        i = 0
        specimen = {}
        for col in td:
            if i == 0:
                url = col.find('a')['href']
                gbif_id = url.replace('https://gbif.org/occurrence/', '')
                specimen['gbif_id'] = gbif_id
                specimen['url'] = url
            specimen[headers[i]] = col.text.strip()
            i += 1
        specimens.append(specimen)
    return specimens


def args_mapper(args):

    map = {
        'callback': 'callback',
        'dataset_id': 'datasetKey',
        'date': 'date',
        'families_collected': 'families_collected',
        'families_identified': 'families_identified',
        'has_occurrences': 'has_occurrences',
        'is_public': 'is_public',
        'limit': 'limit',
        'names': 'names',
        'occurrence_id': 'occurrenceID',
        'page': 'page',
        'q': 'q',
        'strict': 'strict'
    }

    margs = {}
    for k, v in args.items():
        if v != '' and v is not None:
            margs[map[k]] = v
    return margs


def get_agent():
    return {
        "user-agent": "python-requests/"
        + requests.__version__
        + ",bananompy/"
        + bananompy.__version__
    }

BASEURL = "https://api.bionomia.net/"