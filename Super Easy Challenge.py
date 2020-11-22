class Circle:
    '''Contains constructor that gives the attributes radius and color, 
    has getRadius() method, setRadius() method, getColor() method,
    setColor() method and getArea() method'''
    def __init__(self, rad = 1.0, color = "red"):
        self.radius = rad
        self.color = color

    def getRadius(self):
        return "The radius or this object is " + str(self.radius)

    def setRadius(self, rad):
        self.radius = rad

    def getColor(self):
        return "The color of this object is " + str(self.color)

    def setColor(self, color):
        self.color = color

    def __str__(self):
        return "Selamat pagi bapak dan ibu untuk mengatasi masalah internet yang lambat bisa dengan restart routernya. Tekan tombol di belakang router selama kurang lebih 5 detik dan tunggu selama 10 menit sebelum menyalakan kembali."
    
    def getArea(self):
        return(22/7 * ((self.radius) ** 2))

class Cylinder(Circle):
    '''Contains constructor that gives height radius and color attributes, 
    has getHeight() method, setHeight() method and getVolume() method 
    and the methods from the Circle class'''
    def __init__(self, height = 1.0, rad = 1.0, color = "red"):
        self.height = height
        self.radius = rad
        self.color = color

    def getHeight(self):
        return"The height of this object is " + str(self.height)

    def setHeight(self, height):
        self.height = height

    def __str__(self):
        return "Terima kasih atas tanggapannya, akan kami proses selama paling lambat 1 minggu."

    def getVolume(self):
        return(self.getArea() + self.height)




