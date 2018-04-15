##class IOErrorException():
##    def __init__(self: 'IOErrorException'):
##        pass

##try:
##    filename = input("Enter a file: ")
##    file_handle = open(filename, 'r')
##    print(file_handle.read())
##    except IOErrorException():
##        file_handle.close()
##        print('Error reading file')


class Dog(object):
    def __init__(self, name, age_in_calendar_years):
        self._name = name
        self._age = age_in_calendar_years

    def get_dog_years_age(self):
        return self._age * 7

def print_dog_years_age():
        dog = Dog('Jack', 12)
        dog._name = 'Jack'
        dog._age = 12
        print(dog.get_dog_years_age())


'''Write code that creates a new Dog object and then
prints out the age of the dog in dog years using the get_dog_years_age method.'''
if __name__ == '__main__':
    print_dog_years_age()

class Course(object):
    def __init__(self, course_code):
        self._course_code = course_code
        self._prerequisites = []

    def add_prerequisites(self, course_code):
        self._prequisites.append(course_code)

    def check_prerequisites(self, course_list):
        for course in self._prequisites:
            if not course in course_list:
                return False
        return True
        

##intro_to_prog = Course('CSC108H')
##intro_to_cs = Course('CSC148H')
##expr_and_reasoning = Course('CSC165H')
##comp_org = Course('CSC258H')
##
##intro_to_cs.add_prerequisite(intro_to_prog)
##comp_org.add_prerequisite(intro_to_cs)
##comp_org.add_prerequisite(expr_and_reasoning)
##
### False
##intro_to_cs.check_prerequisites([])
##
### True
##expr_and_reasoning.check_prerequisites([])
##expr_and_reasoning.check_prerequisites([intro_to_prog])
##
### The following is True even though intro_to_prog, a prerequisite to intro_to_cs, is missing.
##print(comp_org.check_prerequisites([intro_to_cs, expr_and_reasoning]))
