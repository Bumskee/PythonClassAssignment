class Person:
    '''Contain the constructor for the name and address attributes'''
    def __init__(self, name, address):
        '''Constructor'''
        self.__name = name
        self.__address = address
    
    def getName(self):
        '''returns the object's name'''
        return self.__name

    def getAddress(self):
        '''returns the object's address'''
        return self.__address

    def setAddress(self, address):
        '''change the attributes value of the object address'''
        self.__address = address

    def __str__(self):
        return ("{}({})".format(str(self.__name), str(self.__address)))

class Student(Person):
    '''Contain the constructor for the name, address, numCourses, and courses attributes with the numCourses and courses has the default value of 0 and an empty dictionary respectively'''
    def __init__(self, name, address, numCourses = 0, courses = {}):
        super().__init__(name, address)
        self.__numCourses = numCourses
        self.__courses = courses

    def addCourseGrade(self, course, grade):
        '''add a key value of course name and value pair of grade to the courses attributes'''
        if course not in self.__courses:
            self.__courses[course] = grade
            self.__numCourses = len(self.__courses)
        else :
            print("Course already existed")

    def printGrades(self):
        '''Print the grades that the student have'''
        grades = []
        for k in self.__courses:
            grades.append(self.__courses[k])
        print(grades)
    
    def getAverageGrade(self):
        '''returns the average of the students grades'''
        grades = []
        for k in self.__courses:
            grades.append(self.__courses[k])
        return sum(grades) / len(grades)

    def __str__(self):
        return ("Student : {}({})".format(str(self.__name), str(self.__address)))

class Teacher(Person):
    '''Contain the constructor for the name, address, numCourses, and courses attributes with the numCourses and courses has the default value of 0 and an empty list respectively'''
    def __init__(self, name, address, numCourses = 0, courses = []):
        super().__init__(name, address)
        self.__numCourses = numCourses
        self.__courses = courses

    def addCourse(self, course):
        '''Adds a course to the courses attributes if it is not in the courses attributes'''
        if course not in self.__courses:
            self.__courses.append(course)
            self.__numCourses = len(self.__courses) 
        else:
            print("Course already existed")  
            
    def removeCourse(self, course):
        '''Removes a coursefrom the courses attributes if it is in the courses attributes'''
        if course in self.__courses:
            self.__courses.remove(course)   
        else:
            print("Course doesn't exist") 