#Superclass X
class X:
    pass

#Superclass Y
class Y:
    pass

#Superclass Z
class Z:
    pass

#Subclass A that inherits the attributes and methods from the class X and Y
class A(X, Y):
    pass

#Subclass B that inherits the attributes and methods from the class Y and Z
class B(Y, Z):
    pass

#Subclass M that inherits the attributes and methods from the class B that also inherits the attributes and methods from the class Y and Z. 
class M(B):
    pass