class Permission:
    def __init__(self, search=False, view=False, delete=False, create=False):
        self.search = search
        self.view = view
        self.delete = delete
        self.create = create

class Student_permission(Permission):
    def __init__(self):
        super().__init__(view=True, create=True)

class CourseAdvisor(Permission):
    def __init__(self):
        super().__init__(search=True, view=True, create=True)

class Administrator(Permission):
    def __init__(self):
        super().__init__(search=True, view=True, delete=True, create=True)

# Example usage:
student_permission = Student_permission()
course_advisor_permission = CourseAdvisor()
admin_permission = Administrator()

print("Student Permissions: ", student_permission.__dict__)
print("Course Advisor Permissions: ", course_advisor_permission.__dict__)
print("Administrator Permissions: ", admin_permission.__dict__)
