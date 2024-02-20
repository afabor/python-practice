class Student():
    
    def __init__(self, name, gender, student_ID, subject):
        self.name = name
        self.gender = gender
        self.student_ID = student_ID
        self.subject = subject
        
    def show_details(self):
        print(f'Student Name: {self.name} - Student Gender: {self.gender}')
        print(f'Student ID: {self.student_ID} Subject - {self.subject}')

    def submission(self, score):
        self.grade = score
        print(f'Grade Book has been updated: Current Grade- {self.grade}')

    def attendance(self, attendance):
        self.register = attendance
        print(f'Attendance Percentage: - {self.register}%')
    
Michael = Student('Michael', 'Male', '56789', 'Software Engineering')
Michael.show_details()
Michael.attendance(100)
Michael.submission(93)