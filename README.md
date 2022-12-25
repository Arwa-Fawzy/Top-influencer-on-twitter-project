# Top-influencer-on-twitter-project-
Getting the top influencer given a comma-separated file to represent some Twitter users and the users they follow. In “twitter.csv” file, each row represents a certain user’s id and the id of another user he/she follows.

# Program aim 
This project is to make a program that stores this data in a suitable data structure that
helps the program to retrieve the Top-influencer that has the highest number of followers,
when required, and then the next Top-influencer and so on.
Additionally, this project time complexity analysis illustration is supported to the program’s algorithm in
a pdf document.

# Followers' Suggestions 
Furthermore, this program may take a Twitter account id from the user and calculate its
closest group of Twitter users to recommend as a new friend. Closest means they have at
least a threshold number of Twitter accounts in common. One of the following program responsibilities in this is to determine this threshold.

# Dataset 
The attached dataset contains `2,420,766` different following states (edges) and around
`81,000` different Twitter accounts.

### Pseudocode 
* Loading the excel file into python                                                                                                                             
* Reading a CSV file into a Python Dictionary
* The dictionary key is the person ID and its value is a list of his followers 
* Creating a new dictionary; its key is the person’s ID and his value is the length of the list that contains his followers
* Initializing a list that includes the lengths of lists only 
* Applying radix sort that is based on count sort on the list
* Accessing each person’s ID (the key) from the original dictionary (by its value which is the length of the list) in order from least influencer to the top one 
* Finally, there was a function that recommend a person for another if both of them have at least 1000 common followers 

# Time complexity analysis

The time complexity of loading the CSV file into the dictionary, copying it to the new dictionary, and copying the lengths to the new list is O(N) times. Then, the time complexity of radix sort is known as O(nd), where n is the size of the list and d is the number of digits in the largest number which is a constant. Therefore, the total time complexity is O(2N) which is finally O(N) times. The time complexity of followers’ suggestions is O(n^2). 

## Credits
This project was created by Ahmed Zaky Baioumy, 6 Decemeber 2022.

This code was written by Arwa Fawzy, 20 December 2022.

