import csv
import glob
import os


def chooseMost(List):
    """
    Select elements in list appear in the most times
    :param List:
    :return:
    """
    temp = []
    for i in List:
        temp += [List.count(i)]
    return List[temp.index(max(temp))]
    pass


def filterRepeatElement(List):
    """
    filter repeating elements in list
    :param List:
    :return:
    """
    new_list = []
    for id in List:
        if id not in new_list:
            new_list.append(id)
    return new_list
    pass


def reconstructList(List):
    """
    the element of list is dictionary,the key of dictionary is tuple(name,city),
    and the value of dictionary is tuple(district,location,brand);Under the condition of the same key,
    Take the value elements, in the most times to reconstruct the new List
    :param List:
    :return: results[]
    """

    results = []
    # A list of keys stored in different dictionary
    keys = []
    # A list of value , Store the value of each key
    values = []
    for data in List:
        key = data.keys()
        keys.append(key)
    pass
    # filter the same key
    keys = filterRepeatElement(keys)
    for key in keys:
        for data in List:
            if data.get(key[0]):
                values.append(data.get(key[0]))
        pass
        value = chooseMost(values)
        dict = {key[0]: value}
        results.append(dict)
        values = []
    #print len(results)
    return results
    pass

path = 'F://work'
names = os.listdir(path)
os.chdir(path)
all_info= []
for fname in names:
    fname = os.path.join(path, fname)
    csvfile = open(fname,'rb')

    try:
        reader = csv.DictReader(csvfile)
        for row in reader:
            all_info.append(row)

    finally:
        csvfile.close()
pass





community_list = []
tuple_1 = ()
tuple_2 = ()
for item in all_info:
    tuple_1 = (item['name'], item['city'])
    tuple_2 = (item['district'], item['location'], item['brand'])
    dict = {tuple_1: tuple_2}
    community_list.append(dict)
    pass

community_list = reconstructList(community_list)

with open('F://results/community_list.csv', 'wb') as csvfile:
    fieldnames = ['zsp_id','name', 'city', 'district', 'location', 'brand']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    zsp_id=0
    for item in community_list:
        zsp_id+=1
        name=item.keys()[0][0]
        city=item.keys()[0][1]
        district=item.values()[0][0]
        location=item.values()[0][1]
        brand=item.values()[0][2]
        dict[name]=zsp_id
        writer.writerow({'zsp_id':zsp_id,'name': name, 'city': city,'district':district,'location':location,'brand':brand})

    pass
csvfile.close()




with open('F://results/house_list.csv','wb') as csvfile:
     fieldnames=['domain','zsp_id','id','info_type','house_id','house_type','proportion','price','years','hotline','url']
     writer=csv.DictWriter(csvfile,fieldnames=fieldnames)
     writer.writeheader()
     for item in all_info:
         name=item.get('name')
         for key in dict.keys():
             if name==key:
                 zsp_id=dict.get(key)
             pass

         domain=item.get('domain')
         id=item.get('id')
         info_type=item.get('info_type')
         house_id=item.get('house_id')
         house_type=item.get('house_type')
         proportion=item.get('proportion')
         price=item.get('price')
         years=item.get('years')
         hotline=item.get('hotline')
         url=item.get('url')

         writer.writerow({'domain':domain,'zsp_id':zsp_id,'id':id,'info_type':info_type,'house_id':house_id,'house_type':house_type,'proportion':proportion,'price':price,'years':years,'hotline':hotline,'url':url})

     pass
csvfile.close()

