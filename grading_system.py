print("Welcome to the student grading system")
print('Get the grade and total marks of the student of their 5 subjects')
print('')
input('NAME OF THE STUDENT:')
input('ROLL NO.:')
print('')
print('Enter the marks of the student')
a=int(input("English="))
b=int(input("Hindi="))
c=int(input("Physics="))
d=int(input("Maths="))
e=int(input("Chemistry="))
f=a+b+c+d+e
print(' ')
print('TOTAL MARKS =',f,'/500')
g= (f/500)*100
print('PERCENTAGE=',g)
if g>100:
    print('Wrongs marks entered')
elif g>=90:
    print('GRADE: A')
elif g>=80:
    print('GRADE: B')
elif g>=70:
    print('GRADE: C')
elif g>=60:
    print('GRADE: D')
elif g>=50:
    print('GRADE: E')
else:
    print('GRADE: F')
print('  ')
print('Meanings of the grades')
print('Grade = A : Outstanding')
print('Grade = B : Excellent')
print('Grade = C : Very Good')
print('Grade = D : Good')
print('Grade = E : Need improvement')
print('Grade = F : Fail')

