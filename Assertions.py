
help('math')
def MySalary(salary):
    assert salary>0, 'Salary is negative value!'
    print(f"My salary is {salary}.\n")
taka = int(input("Enter amount : "))
MySalary(taka)


def avg(marks):
    assert len(marks) != 0
    return sum(marks)/len(marks)

mark1 = [int(input("Enter any number ="))]
print("Average of mark1:",avg(mark1))
txt = "hello"
txt1 = txt.replace()