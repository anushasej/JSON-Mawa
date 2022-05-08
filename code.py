import json

 ####Adding data into JSON###
'''
dic = {
    'Name' : 'Prave',
    'Eid' : "124",
    'ph.no': '9011',
    'Add' : 'ATP'
}
# The above dict gonna to be inserted in json file list

try:
    fp = open('employees.json','r+')
    d = json.load(fp)
    
    print(d)
    d.append(dic)
    fp.seek(0)
    fp.truncate()
    json.dump(d,fp,indent=4)
    fp.close()
except:
    print('ERROR')
    
    '''


###Reading data in JSON
'''
try: 
    with open('employees.json','r') as f:
        d = json.load(f)
except:
    print("error")
print(d)
'''

###Operations on data in JSON
# using == for getting particular dict
'''
try: 
    with open('employees.json','r') as f:
        d = json.load(f)
except:
    print("error")
for i in d:
    if i['Name'] == 'Prave':
        print(i)
'''

###Updating the field/key value in the specific dict
'''
with open('employees.json','r+') as f:
    d = json.load(f)
    print(d)
    for i in d:
        if i['Eid'] == '124':
            i['Eid'] = '123'
            break
    f.seek(0)
    f.truncate()
    json.dump(d,f,indent=4)
'''
## removing a dictionary from json example based on Eid
'''
with open('employees.json','r+') as f:
    d = json.load(f)
    print(d)
    for i in range(len(d)):
        if d[i]['Eid'] == '124':
            d.pop(i)
            break
    f.seek(0)
    f.truncate()
    json.dump(d,f,indent=4)
'''

