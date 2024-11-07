# student grade magement system
student_grades = {}

def add_student(name, grade):
    student_grades[name] = grade
    print(f"Added  student name= {name} with marks= {grade}")
    another_record=input(" Do you want to add another record(yes/no)")
    if another_record=="yes":
          name = input("ENTER STUDENT NAME: ")
          grade = int(input("ENTER YOUR GRADE : "))
          student_grades[name] = grade
          print(f"Added another student name = {name} with marks = {grade}")
    else:
        print(" OK ")
        
def update_student(name, grade):
    if name in student_grades:
        student_grades[name] = grade
        print(f"{name} with marks are updated {grade}")
    else:
        print(f"{name} is not found")

def delete_student(name):
    if name in student_grades:
        del student_grades[name]
        print(f"{name} has been successfully deleted")
    else:
        print(f"{name} not found!")
def display_student():
    if student_grades:
        for name, grade in student_grades.items():
            print(f"{name}: {grade}")
    else:
        print("No student found!")

def main():
    while True:
        print("\n *****Student grade management system*****")
        print("1: ADD STUDENT RECORD ")
        print("2: UPDATE STUDENT RECORD ")
        print("3: DELETE STUDENT RECORD ")
        print("4: DISPLAY STUDENT RECORD ")
        print("5: CLOSE PROGRAM ")
        print("6: EXIT")
        choice = input("Enter your choice = ")
        if choice == "1":
            name = input("ENTER STUDENT NAME: ")
            grade = int(input("ENTER YOUR GRADE : "))
            add_student(name, grade)
        elif choice == "2":
            name = input("ENTER STUDENT NAME: ")
            grade = int(input("ENTER YOUR GRADE : "))
            update_student(name, grade)
        elif choice == "3":
            name = input("ENTER NAME OF STUDENT YOU WANT TO DELETE: ")
            delete_student(name)
        elif choice == "4":
            print("LIST OF ALL STUDENTS with their names and marks ")
            display_student()
        elif choice == "5":
            print("Closing the program...")
        elif choice == "6":
            print("Exiting the program.")
            break
        else:
            print("You have entered a wrong choice : ")

if __name__ == "__main__": 
    main()
                          
      
    
