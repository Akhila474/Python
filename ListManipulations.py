#Create any list and do the following manipulations:
  1)Find the length of the list
  2)Create a new list as an existing list
  3)Use slice operator
  4)Replace the second element of the list with a fruit name
  5)Concatenate two lists
  6)Find out atleast two ways to copy and clone a list
  7)Find out atleast one way to split a list into evenly sized chunks
  
  
  
list1 = ["Sam","Mathew",20,65.3]
print("Length of list1 is ",len(list1))
list2 = list1[0:2]
print("New list from the existing list : ",list2)
print("Using slice operator : ",list1[1:])
list1[1]="apple"
print("List1 after replacement : ",list1)
list3=["John","Goel",19,98.3]
print("Concatenating two strings : ",(list1+list3))
list4=[]
list4 = list1.copy()
print("Cloning 1 (using copy()) : ",list4)
list5=[]
list5=list(list1)
print("Cloning 2 (using list()) : ",list5)
def chunkList(initialList, chunkSize):
    finalList = []
    for i in range(0, len(initialList), chunkSize):
        finalList.append(initialList[i:i+chunkSize])
    return finalList
list6=[]
list6=chunkList(list1,2)
print("list after splitting into even size : ",list6)
