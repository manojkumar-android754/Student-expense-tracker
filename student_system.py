print("--- Student Record Management System ---")

# This is the blueprint for creating a structured student profile object
class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

student_database = []

while True:
    print("\n===============================")
    print("1. Add a New Student")
    print("2. View All Student Records")
    print("3. Exit System")
    
    choice = input("Select an option (1-3): ")
    
    if choice == '1':
        print("\n--- Enter Student Details ---")
        name = input("Enter Name: ")
        roll = input("Enter Roll Number: ")
        grade = float(input("Enter CGPA: "))
        
        # Packaging fields together as a single data object block
        new_student = Student(name, roll, grade)
        student_database.append(new_student)
        print(f"✅ Record for {name} added successfully!")
        
    elif choice == '2':
        print("\n--- Current Registered Students ---")
        if len(student_database) == 0:
            print("No records found in the database.")
        else:
            for s in student_database:
                print(f"Name: {s.name} | Roll: {s.roll_number} | CGPA: {s.cgpa}")
                
    elif choice == '3' or choice.lower() == 'exit':
        print("Saving records and closing database management panel...")
        
        # Open a permanent text file to write student records
        with open("student_records.txt", "w") as file:
            file.write("--- REGISTERED STUDENT DATABASE CLOUD REPORT ---\n")
            for s in student_database:
                file.write(f"Name: {s.name} | Roll: {s.roll_number} | CGPA: {s.cgpa}\n")
                
        print("✅ 'student_records.txt' saved and backed up successfully!")
        break