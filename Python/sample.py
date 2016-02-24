import csv
import glob
import os

path = 'F://work'
names = os.listdir(path)
os.chdir(path)
all_info= []
for fname in names:
    print fname


    fname = os.path.join(path, fname)
    csvfile = open(fname,'r')
    try:
        reader = csv.DictReader(csvfile)
        for row in reader:
            all_info.append(row)

    finally:
        csvfile.close()


print len(all_info)