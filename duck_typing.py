#duck typing in python
class duck:
    def fly(self):
        print('Flap! Flap')
    
    def quack(self):
        print('Quack! Quack!')
    
class person:
    def quack(self):
        print("I am quacking like a  duck!")

    def fly(self):
        print("I am flaping my arms like a duck!")


# Non duck typing is in old concept in programmig that belives that only duck can quack and fly
# ie a quack function can be executed only if there it is method of a duck class.

def call(object):
    if isinstance(object, duck):
        object.quack()
        object.fly()
    else:
        print('The object must be a duck!')

# person_object = person()
# print("calling for person")
# call(person_object)
# print("calling for duck")
# duck_object = duck()
# call(duck_object)


#duck typing is a concept of python programming claiming that a method can be executed if the method is in the class.  \+ 

def call2(object):
    try:
        object.fly()
        object.quack()
    except AttributeError as e:
        print(e)

person_object = person()
print("calling for person")
call2(person_object)
print("calling for duck")
duck_object = duck()
call2(duck_object)
normal_string = 'hi'
call2(normal_string)