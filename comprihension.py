#list comprehanson
my_list = [1,23,4,5,6,7,4,3,2,3,5,6,7]

y = [i**2 for i in my_list if i%2 ==1]
print(y)

dictionary = {'name':'Shyam','age':16, 'eamil':'shyam10kwd@gmail.com'}

y = [(key, dictionary[key]) for key in dictionary]
print(y)