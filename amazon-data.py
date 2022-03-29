from requests import get
from pprint import PrettyPrinter

BASE_URL ='https://status.aws.amazon.com'
ALL_JSON = '/data.json'

printer = PrettyPrinter()

data = get(BASE_URL + ALL_JSON).json()
archive = data["archive"]
name_list = []

for i in range (0, len(archive)):
    if 'Ohio' in archive[i]['service_name']:
        name_list.append(archive[i]['service_name'])

printer.pprint(name_list[15:])
