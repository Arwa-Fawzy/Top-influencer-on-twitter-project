#import necessary packages
import csv 

#loading the excel file into python 
followers_csv=open('D:/CS/3rd/algorithms/project/twitter.csv')
# 1  2
# 3  2
# 1 follows 2 
# 3 follows 2
#followers_col={2:[1,3]}

#reading the file to assign it into a dictionary 
reader=csv.reader(followers_csv)
#initializing a dictionary 
followers_col={}
#initializing a new dictionary
new_Col={}
#List of lengths 
data=[]
#set the influencer a key and his followers is a value which is list 
for follower in reader:
    index=int(follower[1])
    if index not in followers_col:
        followers_col[index]=[]
    followers_col[index].append(int(follower[0]))


#set the influencer a key and his followers is a value which is length of the list  
for key, value in followers_col.items(): 
    new_Col[int(key)]=len(value)
    
#collecting the values into a list (lengths of lists)
for key, value in new_Col.items():
    data.append(value)

#radix sort to sort the list 
def countingSort(array, place):
    size = len(array)
    output = [0] * size
    count = [0] * 10

    # Calculate count of elements
    for i in range(0, size):
        index = array[i] // place
        count[index % 10] += 1

    # Calculate cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Place the elements in sorted order
    i = size - 1
    while i >= 0:
        index = array[i] // place
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, size):
        array[i] = output[i]

# Main function to implement radix sort
def radixSort(array):
    # Get maximum element
    max_element = max(array)

    # Apply counting sort to sort elements based on place value.
    place = 1
    while max_element // place > 0:
        countingSort(array, place)
        place *= 10

radixSort(data)
#list of influencers from least one to top one 
sorted_according_to_followers=[]

j=0
for i,value in new_Col.items():
    if value==data[j]:
        sorted_according_to_followers.append(i)
        j+=1

sorted_according_to_followers.reverse()
print("The top influencer is ")
print(sorted_according_to_followers[0])
#print("and his number of influencers is ")
#print(new_Col[sorted_according_to_followers[0]])

#Bonus question 
common=[]
recommend=[]
count=0
for key, value in followers_col.items():
    for i in value:
        common.append(i)
    person=key
    break

it=0
for key, value in followers_col.items():
    for i in value:
        if i==common[it]:
            count+=1
            it+=1
    if count>=1000:
        recommend.append(key)
        #print("The person whose ID is ") 
        #print(key)
        #print("is recommened for")
        #print(person)
        it=0
