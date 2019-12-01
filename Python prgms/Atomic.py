1)Create a Dictionary that contains the atomic element symbol and the name.
2)Add a unique and duplicate element into this dictionary by interacting with the user.
3)Display the number of atomic elements in this dictionary.
4)Ask user to enter an element to search in the dictionary. Display appropriate results.
Rewrite this program so that these operations are inside a function called "AtomicDictionary".Create another python file called "Atomic.py" 
and execute this function in it.


def AtomicDictionary():
    atomic={
        'H':'Hydrogen',
        'He':'Helium',
        'Li':'Lithium',
        'Be':'Berilium'
    }
    #adding unique and duplicate element 
    a=(input("Enter key:"))
    b=(input("Enter value:"))
    atomic.update({a:b}) 
    print("Updated Dict is: ", atomic) 
    c=(input("Enter key:"))
    d=(input("Enter value:"))
    atomic.update({c:d})
    print("Updated Dict is: ", atomic) 

    #display number of atomic elements in dictionary
    print("number of atomic elements",len(atomic.keys()))

    #Searching for element in dictionary
    f=(input("Enter value you want to search for:"))
    if f in atomic.values():
        print("Exists in dictionary")
    else:
        print("Does not exist in dictionary")
