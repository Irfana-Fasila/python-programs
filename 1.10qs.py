def find_student_with_highest_marks(students):
    highest_marks = -1
    top_student = None
    
    for student in students:
        if students[student]['total_marks'] > highest_marks:
            highest_marks = students[student]['total_marks']
            top_student = student
    
    return top_student, highest_marks

def main():
    students = {}
    
    n = int(input("Enter the number of students: "))
    
    for i in range(1, n + 1):
        print(f"Student {i}:")
        name = input("Enter student's name: ")
        roll_no = input("Enter student's roll number: ")
        total_marks = float(input("Enter student's total marks: "))
        
        students[name] = {'roll_no': roll_no, 'total_marks': total_marks}
    top_student, highest_marks = find_student_with_highest_marks(students)
    print(f"\nStudent with the highest total marks:")
    print(f"Name: {top_student}")
    print(f"Roll Number: {students[top_student]['roll_no']}")
    print(f"Total Marks: {students[top_student]['total_marks']}")

if __name__ == "__main__":
    main()
