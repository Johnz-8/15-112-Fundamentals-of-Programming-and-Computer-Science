from cmu_cpcs_utils import testFunction, almostEqual

class Semester:
    def __init__(self):
        self.courses=[]
        self.coursesDict=dict()
        self.grades=[]

    def __repr__(self):
        if self.courses==[]:
            return '<Semester, no grades>'
        else:
            grades=self.grades
            res=', '.join(grades)
            return f'<Semester, grades: {res}>'

    def addGrade(self, courseName, grade):
        self.courses.append(courseName)
        self.grades.append(grade)
        self.coursesDict[courseName]=grade

    def getGrade(self, courseName):
        return self.coursesDict.get(courseName,None)

    def gpa(self):
        return computeGpa(self.grades)

class Transcript:
    def __init__(self):
        self.courses=[]
        self.grades=[]
        self.count=0

    def __repr__(self):
        if self.count==0:
            return '<empty transcript>'
        elif self.count==1:
            return '<Transcript, 1 semester>'
        else:
            return f'<Transcript, {self.count} semesters>'

    def addSemester(self, semester):
        self.courses+=semester.courses
        self.grades+=semester.grades
        self.count+=1

    def gpa(self):
        return computeGpa(self.grades)

def computeGpa(grades):
    count=0
    total=0
    for grade in grades:
        if grade=='A':
            total+=4
        if grade=='B':
            total+=3
        if grade=='C':
            total+=2
        if grade=='D':
            total+=1
        count+=1
    return total/count if count>0 else None

@testFunction
def testSemesterAndTranscriptClasses():
    semester1 = Semester()
    assert(str(semester1) == '<Semester, no grades>')

    semester1.addGrade('Intro to CS', 'A')
    assert(semester1.courses == ['Intro to CS'])
    assert(str([semester1]) == '[<Semester, grades: A>]')

    semester1.addGrade('Fun Reading', 'B')
    semester1.addGrade('Advanced Math', 'B')
    semester1.addGrade('History 101', 'A')
    assert(str(semester1) == '<Semester, grades: A, B, B, A>')
    assert(semester1.courses == ['Intro to CS', 'Fun Reading',
                                 'Advanced Math', 'History 101'])
    
    assert(semester1.getGrade('Intro to CS') == 'A')
    assert(semester1.getGrade('Fun Reading') == 'B')
    assert(semester1.getGrade('Advanced Math') == 'B')
    assert(semester1.getGrade('History 101') == 'A')
    assert(semester1.getGrade('English 202') == None) # not taken
    assert(almostEqual(semester1.gpa(), 3.5)) # (4 + 3 + 3 + 4) / 4

    semester2 = Semester()
    assert(str(semester2) == '<Semester, no grades>')
    assert(semester2.gpa() == None) # no courses yet this semester
    semester2.addGrade('English 202', 'D')
    assert(str(semester2) == '<Semester, grades: D>')
    assert(semester2.courses == ['English 202'])
    assert(semester2.getGrade('English 202') == 'D')
    assert(almostEqual(semester2.gpa(), 1)) # 1 / 1

    transcript1 = Transcript()
    assert(str(transcript1) == '<empty transcript>')
    assert(transcript1.gpa() == None)

    transcript1.addSemester(semester1)
    assert(str(transcript1) == '<Transcript, 1 semester>')
    assert(almostEqual(transcript1.gpa(), 3.5)) # (3 + 4 + 4 + 3) / 4

    transcript1.addSemester(semester2)
    assert(str(transcript1) == '<Transcript, 2 semesters>')
    assert(almostEqual(transcript1.gpa(), 3)) # (3 + 4 + 4 + 3 + 1) / 5

def main():
    testSemesterAndTranscriptClasses()

main()
