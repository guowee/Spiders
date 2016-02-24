import csv
import os
import sys

reload(sys)
# python default encoding ascii
sys.setdefaultencoding("utf-8")

# read the information of building
path = 'F://pending/build.csv'
build_info = []

csvfile = open(path, 'rb')
try:
    reader = csv.DictReader(csvfile)
    for row in reader:
        build_info.append(row)
    pass
finally:
    csvfile.close()
pass
# read the information of house
path = 'F://pending/house_info.csv'
house_info = []
csvfile = open(path, 'rb')
try:
    reader = csv.DictReader(csvfile)
    for row in reader:
        house_info.append(row)
    pass
finally:
    csvfile.close()
pass

for item in house_info:
    for temp in build_info:
        if item.get('name') == temp.get('name'):
            item['id'] = temp.get('id')
            item['brand'] = temp.get('brand')
        pass
    pass
pass

path = 'F://outcome/lianjia_esf.csv'
with open(path, 'wb') as csvfile:
    fieldnames = ['id', 'info_type', 'name', 'city', 'district', 'location', 'price', 'brand', 'hotline', 'house_type',
                  'proportion', 'years', 'house_id', 'domain', 'url']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for item in house_info:
        id = item.get('id')
        info_type = item.get('info_type')
        name = item.get('name')
        city = item.get('city')
        district = item.get('district')
        location = item.get('location')
        price = item.get('price')
        brand = item.get('brand')
        hotline = item.get('hotline')
        house_type = item.get('house_type')
        proportion = item.get('proportion')
        years = item.get('years')
        house_id = item.get('house_id')
        domain = item.get('domain')
        url = item.get('url')

        writer.writerow(
                {'id': id, 'info_type': info_type, 'name': name, 'city': city, 'district': district,
                 'location': location, 'price': price, 'brand': brand, 'hotline': hotline, 'house_type': house_type,
                 'proportion': proportion, 'years': years, 'house_id': house_id, 'domain': domain, 'url': url})
        pass
csvfile.close()