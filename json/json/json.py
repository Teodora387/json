import json
with open("C:/teo/cursuri/sem1/p1/ex4_input4.json", "r") as f:
    data4=json.load(f)
    s=0
    count=0
    for i in data4:
        count+=1
        for key, values in i.items():
            if key == 'pret':
                s+=value
    avg=s//count
    maxim=0
    l=0
    months=[]
    destination=""
    for i in data4:
        for key, value in i.items():
            if key=='rezervari':
                if int(value)>maxim:
                    maxim==value
                    l=i
    for key, value in l.items():
        if key == 'destinatie':
            destination=value
        if key == 'perioade':
            months=value
    print('destination: ', destination)
    print('month:', months)
