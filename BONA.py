# First Concept 
def getgrade(score):
    if score >= 80:
        return 'A'
    elif score in range(70,80):
        return 'B'

name = input("Name: ")
year = input("Class of ")
print("Kindly input your grades for the following:")

math = int(input("pure Mathematics: "))
print(f"Grade: {getgrade(math)}")

chemistry = int(input("Chemistry: "))
print(f"Grade: {getgrade(chemistry)}")

# Concept Upgrade 1
"""
Update includes:
- Ability to create several instances of students
- method for storing subjects and scores for each student
- method for displaying grades for each student
- More grading options, I guess...
"""
class Student:
    """Model of a student"""

    def __init__(self, name, year):
        """Initializing..."""
        self.name = name
        self.year = year
    def subjects(self):
        """Storing subjects"""
        print("Put in 3 subjects")
        self.sub1 = input("Subject 1: ")
        self.sub1score = int(input("Score: "))
        self.sub2 = input("Subject 2: ")
        self.sub2score = int(input("Score: "))
        self.sub3 = input("Subject 3: ")
        self.sub3score = int(input("Score: "))
    def getgrade(self):
        """Produces grade"""
        link = {self.sub1:self.sub1score, self.sub2:self.sub2score, self.sub3:self.sub3score}
        nlink = link.copy()
        for item, score in nlink.items():
            if score >= 90:
                nlink[item] = f'{score} (A*)'
            elif score in range(80,90):
                nlink[item] = f'{score} (A)'
            elif score in range(70,80):
                nlink[item] = f'{score} (B)'
            elif score in range(60,70):
                nlink[item] = f'{score} (C)'
            else:
                nlink[item] = f'{score} (FAIL)'
        print(f"\n{self.name.title()}'s grades:")
        for i,j in nlink.items():
            print(f"{i} : {j}")

# Concept Upgrade 2
"""
Update Includes:
-Freedom to input as many subjects as possible
"""
class Pupil:
    """Model of a pupil"""
    def __init__(self, name, year):
        """Initializing..."""
        self.name = name
        self.year = year
    def store(self, **subjects):
        """Storing subjects"""
        quest = int(input("How many subjects do you want to enter? (integers only) "))
        for i in range(quest):
            sub = input("Subject name:")
            score = int(input("Score: "))
            subjects[sub] = score   
        self.subjects = subjects
    def getgrade(self):
        """Produces grade"""
        nlink = self.subjects.copy()
        for item, score in nlink.items():
            if score >= 90:
                nlink[item] = f'{score} (A*)'
            elif score in range(80,90):
                nlink[item] = f'{score} (A)'
            elif score in range(70,80):
                nlink[item] = f'{score} (B)'
            elif score in range(60,70):
                nlink[item] = f'{score} (C)'
            else:
                nlink[item] = f'{score} (FAIL)'
        print(f"\n{self.name.title()}'s grades:")
        for i,j in nlink.items():
            print(f"{i} : {j}")           

kofi= Student('kofi', 2005)
kofi.subjects()
kofi.getgrade()
bernard= Pupil('bernard', 2003)
bernard.store()
bernard.getgrade()
