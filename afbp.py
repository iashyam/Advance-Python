#there are two ways to run programs in python 
#1. to checking and eleminating exception
#2. trying and handeling exceptions

#1. TO cheking every step and eleminating exceptions
#THis is called check before you leave

a = [1,2,3,4,5,7,]

#printing the index of seven
def print_index(lst, num):
    if  num in lst:
        print(lst.index(num))
    else:
        print(f"{num} is not in list.")

print_index(a, 7)
print_index(a, 6)

def print_index2(lst, num):
    try:
        print(lst.index(num))
    except ValueError:
        print(f"{num} is not in list.")

print_index2(a, 7)
print_index2(a, 6)
