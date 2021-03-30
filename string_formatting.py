# in this tutorial there comes string formatring

#1. how to use .format
# string = 'My name is {}, and I am from {} '.format("Shyam","Rawatsar")
# print(string)

#2. taking arguments from dictonary

# information = {'name': 'Shyam', "age": 18  }
# print('My name is {name} and I am {age} years old.'.format(**information))

#3. setting prpoerties
#foratting the placeholders
#1.1 Adign a zero pad
# for i in range(10):
#     print("THe number is {:02}".format(i))
#     print("The number is {:.3f}".format(i))

#Let's do some daytime formatting
import datetime

date = datetime.datetime.now()
print("{0:%a} {0:%b} {0:%d} {0:%H}:{0:%M} ".format(date))