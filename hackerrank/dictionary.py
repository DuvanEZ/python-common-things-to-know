"""The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. Print the average of the marks array for the student name provided, showing 2 places after the decimal.

Example




The query_name is 'beta'. beta's average score is .

Input Format

The first line contains the integer , the number of students' records. The next  lines contain the names and marks obtained by a student, each value separated by a space. The final line contains query_name, the name of a student to query.

Constraints

Output Format

Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.

Sample Input 0

3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika
Sample Output 0

56.00
Explanation 0

Marks for Malika are  whose average is 

Sample Input 1

2
Harsh 25 26.5 28
Anurag 26 28 30
Harsh
Sample Output 1

26.50
"""
if __name__ == '__main__':
    n = int(input())  # Number of students' records
    student_marks = {}  # Dictionary to store name:[marks] pairs

    # Input marks for each student
    for _ in range(n):
        name, *marks_str = input().split()
        marks = list(map(float, marks_str))
        student_marks[name] = marks

    query_name = input()  # Name of the student to query

    # Calculate and print the average of the marks for the queried student
    average_marks = sum(student_marks[query_name]) / len(student_marks[query_name])
    print("{:.2f}".format(average_marks))

if __name__ == '__main__':
    n = int(input())  # Number of students' records
    student_marks = {}  # Dictionary to store name:[marks] pairs

    # Input marks for each student
    [student_marks.update({name: list(map(float, marks_str))}) for name, *marks_str in [input().split() for _ in range(n)]]

    query_name = input()  # Name of the student to query

    # Calculate and print the average of the marks for the queried student
    average_marks = sum(student_marks[query_name]) / len(student_marks[query_name])
    print("{:.2f}".format(average_marks))

