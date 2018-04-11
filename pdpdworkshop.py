import requests
r = requests.get('https://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS')
from lxml import objectify
from pprint import pprint

r = requests.get('https://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Day=tomorrow')
from lxml import objectify
from pprint import pprint

listofdictionaries = []

root = objectify.fromstring(r.content)

def by(dictionary):
    return dictionary['brand']

for each in root.channel.item:
    #print (dir(each)) #run dir function on each
    dict_data = {
        'price': each.price.text,
        'brand': each.brand.text,
        'trading-name': getattr(each , 'trading-name').text
    }
    listofdictionaries.append(dict_data)

pprint (sorted(listofdictionaries, key=by))
# , reverse=True
# for each in root.channel.item:
    # print ("price", ':', each.price)
# print (description)
# for r in description:
#     print(r.tag, ":", r.text)
#     for r in prices:
#         print(r.tag, ":", r.text)
# print(objectify.dump(root))
# sort first
# get tomorrows
# always 1 question mark in the beginnins and the & as you add more
# dont need a comma on the last line of the dictionary
