import sys

upl_list = ['C:\\programming\\Test\\folder 1\\list 1.txt',
            'C:\\programming\\Test\\folder 1\\list 2',
            'C:\\programming\\Test\\folder 1\\list 23',
            'C:\\programming\\Test\\folder 1\\list 3']

list_info = []
list_defect = []

try:
    for url in upl_list:
        try:
            #with open('url') as r:
            #    list_info.append(r)
            r = open(url)
            list_info.append(r.read())
        except:
            list_defect.append(url)
            # sys.exit()
            continue
    print(list_info)

finally:
    r = open('C:\\programming\\Test\\folder 1\\save.txt', 'a')
    for i in list_info:
        r.write(i)
    r.write(str(list_defect))
    r.close()
