class Person:
    '''Contain the constructor for the name and address attributes'''
    def __init__(self, name, address):
        '''Constructor'''
        self.name = name
        self.address = address
    
    def getName(self):
        '''returns the object's name'''
        return self.name

    def getAddress(self):
        '''returns the object's address'''
        return self.address

    def setAddress(self, address):
        '''change the attributes value of the object address'''
        self.address = address

    def __str__(self):
        return ("{}({})".format(str(self.name), str(self.address)))

class Student(Person):
    '''Contain the constructor for the name, address, numCourses, and courses attributes with the numCourses and courses has the default value of 0 and an empty dictionary respectively'''
    def __init__(self, name, address, numCourses = 0, courses = {}):
        self.name = name
        self.address = address
        self.numCourses = numCourses
        self.courses = courses

    def addCourseGrade(self, course, grade):
        '''add a key value of course name and value pair of grade to the courses attributes'''
        if course not in self.courses:
            self.courses[course] = grade
            self.numCourses = len(self.courses)
        else :
            print("Course already existed")

    def printGrades(self):
        '''Print the grades that the student have'''
        grades = []
        for k in self.courses:
            grades.append(self.courses[k])
        print(grades)
    
    def getAverageGrade(self):
        '''returns the average of the students grades'''
        grades = []
        for k in self.courses:
            grades.append(self.courses[k])
        return sum(grades) / len(grades)

    def __str__(self):
        return ("Student : {}({})".format(str(self.name), str(self.address)))

class Teacher(Person):
    '''Contain the constructor for the name, address, numCourses, and courses attributes with the numCourses and courses has the default value of 0 and an empty list respectively'''
    def __init__(self, name, address, numCourses = 0, courses = []):
        self.name = name
        self.address = address
        self.numCourses = numCourses
        self.courses = courses

    def addCourse(self, course):
        '''Adds a course to the courses attributes if it is not in the courses attributes'''
        if course not in self.courses:
            self.courses.append(course)
            self.numCourses = len(self.courses) 
        else:
            print("Course already existed")  
            
    def removeCourse(self, course):
        '''Removes a coursefrom the courses attributes if it is in the courses attributes'''
        if course in self.courses:
            self.courses.remove(course)   
        else:
            print("Course doesn't exist") 




