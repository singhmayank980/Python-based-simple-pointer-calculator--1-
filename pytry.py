grade = {'A':10, 'AB': 9, 'B':8, 'BC': 7, 'C': 6,'D': 4,'F': 0}
print("Enter your number of subjects")
sub = int(input())
a = sub
sum=0
while sub > 0:
    i = a-sub+1
    print("Enter your ", i, "th" ,"subject grades in CAPS LOCK ")
    x= input()
    grade[x]
    sum = sum + grade[x]
    sub= sub-1
print("Accoring to the calculator your pointer will be : ",sum/a)

