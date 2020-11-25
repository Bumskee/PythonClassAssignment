class Circle:
    '''Contains constructor that gives the attributes radius and color, 
    has getRadius() method, setRadius() method, getColor() method,
    setColor() method and getArea() method'''
    def __init__(self, rad, color):
        self.__radius = rad
        self.__color = color

    def getRadius(self):
        return "The radius or this object is " + str(self.__radius)

    def setRadius(self, rad):
        self.__radius = rad

    def getColor(self):
        return "The color of this object is " + str(self.__color)

    def setColor(self, color):
        self.__color = color

    def __str__(self):
        return "Selamat pagi bapak dan ibu untuk mengatasi masalah internet yang lambat bisa dengan restart routernya. Tekan tombol di belakang router selama kurang lebih 5 detik dan tunggu selama 10 menit sebelum menyalakan kembali."
    
    def getArea(self):
        return(22/7 * ((self.__radius) ** 2))

class Cylinder(Circle):
    '''Contains constructor that gives height radius and color attributes, 
    has getHeight() method, setHeight() method and getVolume() method 
    and the methods from the Circle class'''
    def __init__(self, rad, color, height):
        super().__init__(rad, color)
        self.__height = height

    def getHeight(self):
        return"The height of this object is " + str(self.__height)

    def setHeight(self, height):
        self.__height = height

    def __str__(self):
        return "Terima kasih atas tanggapannya, akan kami proses selama paling lambat 1 minggu."

    def getVolume(self):
        return(self.getArea() * self.__height)




