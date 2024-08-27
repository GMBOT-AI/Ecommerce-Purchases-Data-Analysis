"""1. Display Top 10 Rows of The Dataset
2. Check Last 10 Rows of The Dataset
3. Check Datatype of Each Column
4. Check null values in the dataset
5. How many rows and columns are there in our Dataset? 
6. Highest and Lowest Purchase Prices.
7. Average Purchase Price
8. How many people have French 'fr' as their Language?
9. Job Title Contains Engineer
10. Find The Email of the person with the following IP Address: 132.207.160.22
11. How many People have Mastercard as their Credit Card Provider and made a purchase above 50?
12. Find the email of the person with the following Credit Card Number: 4664825258997302
13. How many people purchase during the AM and how many people purchase during PM?
14. How many people have a credit card that expires in 2020?
15. What are the top 5 most popular email providers (e.g. gmail.com, yahoo.com, etc...) """

import pandas as pd

data= pd.read_csv('Ecommerce Puchases')

#Question 1
data.head(10)

#Question 2
data.tail(10)

#Question 3
data.dtypes

#Question 4
data.isnull().sum()

#Question 5
print(data.shape[0]) #displays rows
print(data.shape[1]) #displays columns

#Question 6
data['Purchase Price'].max()
data['Purchase Price'].min()

#Question 7
data['Purchase Price'].mean()

#Question 8
len(data[data['Language']=="fr"])

#Question 9
data[data['Job'].str.contains('Engineer', case=False)]

#Question 10
data[data['IP Adress']=="132.207.160.22"]['Email']

#Question 11
data[(data['CC Provider']=="mastercard") & (data['Purchase Price'] > 50)]

#Question 12
data[data['Credit Card']==4664825258997302]['Email']

#Question 13
data['AM or PM'].value_counts()

#Question 14
print(data['CC Exp Date'])

def funct():
    count=0
    for d in data['CC Exp Date']:
        if date.split('/')[1]==20:
            count=count+1
    print(count)
func()

#Question 15
l=[]
for x in data['Email']:
    l.append(x.split('@')[1])
    
data['temp']=l
data['temp'].value_counts().head(5)











