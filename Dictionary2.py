#Create a dictionary to hold student details with register numbers as the key. Print those details whose register numbers are even.

dist = {
    1: {
        "name": "Sama",
        "phone number": 121
    },
    2: {
        "name": "Rama",
        "phone number": 221
    },
    3: {
        "name": "John",
        "phone number": 312
    },
    4: {
        "name": "Cand",
        "phone number": 311
    },
    5: {
        "name": "Gale",
        "phone number": 213
    },
    6: {
        "name": "Ames",
        "phone number": 111
    }
}

for i in dist.keys():
    if(i % 2 == 0):
        print(dist.get(i))
