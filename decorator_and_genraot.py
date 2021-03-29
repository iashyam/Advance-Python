
#defingin a decorator 
#it takes a function as argument anfd returens other function 
# there is a function defined in this function called wrapper function

# hello()
#jab bhi hum is function ko call karenge 
#decorator function execute hogs 

#decorator class
# class decorator_class:
#     def __init__(self, function):
#         self.function = function
     
#     def __call__(self):
#         print("Wrapper function executed by class")
#         return self.function()

# @decorator_class
# def hello():
#     print("Hello world!")

# hello()



def decorator_function(function):

    def wrapper_function():
        print('Wrapper function executed!')
        return function()

    return wrapper_function


#DEcorators for functions with arguments

class decorator_class:
    def __init__(self, function):
        self.function = function
     
    def __call__(self, *args, **kwargs):
        print("Wrapper function executed by class")
        return self.function(*args, **kwargs)

@decorator_class
def hello(name):
    print("Hello world!", name)

hello('Shyam')

#febonecchi series genertor 
def febonecci(numberOfTerms):
    x = 0
    y = 1
    for _ in range(numberOfTerms):
        yield x
        temp = x
        x += y
        y = temp


fistTenFebonacci = febonecci(10)
print(type(fistTenFebonacci))
for i in fistTenFebonacci:
    print(i)
