if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    num = list(student_marks[query_name])
    result = 0.00
    for i in range(len(num)):
        result = result + num[i]
    aver = float(result)/3
    float_number = "{:.2f}".format(aver)
    print(float_number)