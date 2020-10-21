import traceback

def RadixSort(M):
    M2=[]
    N=[]
    yy=CountingYear(M,M2,8)
    V=CountingHouse(yy,N,4)
    return V

def CountingYear(Y,Z,k):
    C=[0]*(k+1)
    for j in range(len(Y)):
        x=Y[j].year
        C[x]=C[x]+1
    for n in range(1,k+1):
        C[n]=C[n]+C[n-1]
    Z=[0]*len(Y)
    for m in range(len(Y)-1,-1,-1):
        key=Y[m].year
        index=C[key]-1
        Z[index]=Y[m]       #!!!!!!
        C[key]=C[key]-1
    return Z

def CountingHouse(U,V,k):
    dic={'Eagletalon':0, 'Lannister':1, 'Pufflehuff':2, 'SNAKES':3}
    C=[0]*(k+1)
    for j in range(len(U)):
        x=dic[U[j].house]
        C[x]=C[x]+1
    for n in range(1,k+1):
        C[n]=C[n]+C[n-1]
    V=[0]*len(U)
    for m in range(len(U)-1,-1,-1):
        key=dic[U[m].house]
        index=C[key]-1
        V[index]=U[m]
        C[key]=C[key]-1      
    return V

def SortStudents(A):
  
    V=RadixSort(A)
    return V


#Student class
#Each task has three instance variables:
#   self.name is a string representing the name of the student
#   self.house is a string representing which house the student is in
#   self.year is an integer representing what year the student is
class Student:
    def __init__(self,csvstring):
        csvdata = csvstring.split(",")
        self.name = csvdata[0]
        self.house = csvdata[1]
        self.year = int(csvdata[2])
    def __repr__(self):
        return "\n{:25}: {:12} {}".format(self.name,self.house,self.year)
    def __eq__(self,other):
        return type(self) == type(other) and \
               self.name == other.name and \
               self.house == other.house and \
               self.year == other.year

      



#Takes a string filename as an argument, and constructs a list
#  of Students from the information in the CSV file at filename
def getStudentList(filename):
    fp = open(filename)
    fp.readline()
    studentList = []
    for line in fp:
        studentList.append(Student(line))
    return studentList


tests = ['roster1.csv','roster2.csv','roster3.csv','roster4.csv',
         'roster5.csv','roster6.csv']
correct = ['roster1sorted.csv','roster2sorted.csv',
           'roster3sorted.csv','roster4sorted.csv',
           'roster5sorted.csv','roster6sorted.csv']


#Run test cases, check whether sorted list correct
count = 0

try:
    for i in range(len(tests)):
        print("\n---------------------------------------\n")
        print("TEST #",i+1)
        print("Reading student data from:",tests[i])
        roster = getStudentList(tests[i])
        print("Reading sorted student data from",correct[i])
        rosterSorted = getStudentList(correct[i])
        print("Running: SortStudents() on data list\n")
        output = SortStudents(roster)
        print("Expected:",rosterSorted,"\n\nGot:",output)
        assert len(output) == len(rosterSorted), "Output list length "\
               +str(len(output))+\
                  ", but should be "+str(len(rosterSorted))
        for j in range(len(output)):
            assert output[j] == rosterSorted[j],"Student #"\
                       +str(j+1)+" incorrect: "+\
                    str(output[j])+" \nshould be "+str(rosterSorted[j])
        print("Test Passed!\n")
        count += 1
except AssertionError as e:
    print("\nFAIL: ",e)

except Exception:
    print("\nFAIL: ",traceback.format_exc())

#Check for less than or greater than signs anywhere in the file
cursed = False
with open(__file__) as f:
    source = f.read()
    for ch in source:
        if ord(ch) == 60:
            print("Less than sign detected: Curse activated!")
            count = 0
            cursed = True
        if ord(ch) == 62:
            print("Greater than sign detected: Curse activated!")
            count = 0
            cursed = True

print()
if cursed:
    print("You are now a newt.  Don't worry, you'll get better.")
print(count,"out of",len(tests),"tests passed.")


