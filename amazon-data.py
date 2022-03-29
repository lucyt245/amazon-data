from requests import get
from pprint import PrettyPrinter


BASE_URL ='https://status.aws.amazon.com'
ALL_JSON = '/data.json'

printer = PrettyPrinter()

# accesses the json file and stores its data
data = get(BASE_URL + ALL_JSON).json()
archive = data["archive"]


# creates a list containing issues found in said area
west_USA = []
east_USA = []
europe = []
asia = []
s_america = []
oceania = []
undefined = []


# organises the data based on its geographical location
for i in range (0, len(archive)):
    item = archive[i]['service_name']

    if 'Ohio' in item or 'N. Virginia' in item or 'US-East' in item:
        east_USA.append(item)
    
    elif 'Oregon' in item or 'California' in item or 'US-West' in item:
        west_USA.append(item)
    
    elif 'Ireland' in item or 'Frankfurt' in item or 'London' in item or 'Paris' in item or 'Milan' in item or 'Stockholm' in item:
        europe.append(item)
    
    elif 'Seoul' in item or 'Singapore' in item or 'Hong Kong' in item or 'Tokyo' in item or 'Mumbai' in item:
        asia.append(item)
    
    elif 'Sao Paulo' in item:
        s_america.append(item)

    elif 'Sydney' in item:
        oceania.append(item)
    
    else:
        undefined.append(item)
