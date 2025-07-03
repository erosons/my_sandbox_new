from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from flask import Flask, render_template,request, jsonify
from flask_sqlalchemy import SQLAlchemy
from permissions import student_permission,Administrator,course_advisor_permission

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://careerpath:password@localhost:5432/careerpath_orm'
db = SQLAlchemy(app)

with app.app_context():
   db.create_all()

# Define the Student table with a schema
class Student(db.Model):
    __tablename__ = 'student'
    __table_args__ = {'schema': 'CareerPath'}  # Replace 'CareerPath' with your desired schema
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    programID = db.Column(db.String(150), nullable=False)

    # Define the permissions for Student
    #permissions = student_permission(view=True, create=True)


# Define the Student Advisor table with a schema
class StudentAdvisor(db.Model):
    __tablename__ = 'student_advisor'
    __table_args__ = {'schema': 'CareerPath'}  # Replace 'CareerPath' with your desired schema
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    
    # Define the permissions for Student
    #permissions = course_advisor_permission(search=True, view=True, create=True)

# Define the User Login table with a schema
class User(db.Model):
    __tablename__ = 'user_login'
    __table_args__ = {'schema': 'CareerPath'}  # Replace 'CareerPath' with your desired schema
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    student_id = db.Column(db.String(100), db.ForeignKey('CareerPath.student.id'))
    StudentAdvisor_id = db.Column(db.String(100), db.ForeignKey('CareerPath.advisor.id'))
    #Specific if is one to one relationship
    student = db.relationship('student', backref='user_login')
    advisor = db.relationship('student_advisor', backref='user_login')



# Define the Course Major table with a schema
class Program(db.Model):
    __tablename__ = 'Program'
    __table_args__ = {'schema': 'CareerPath'}  # Replace 'CareerPath' with your desired schema
    id = db.Column(db.String(150), primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    program_categories = db.Column(db.String(150), nullable=False)
    Desc = db.Column(db.String(300), nullable=False)
    student_id = db.Column(db.String(300), db.ForeignKey('CareerPath.student.id'))
    student = db.relationship('Student', backref='Program',uselist=False)


# Define the Elective table with a schema
class Elective(db.Model):
    __tablename__ = 'Electives'
    __table_args__ = {'schema': 'CareerPath'}  # Replace 'CareerPath' with your desired schema
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    Desc = db.Column(db.String(300), nullable=False)
    Unit = db.Column(db.Integer, nullable=False)
    course_major_id = db.Column(db.Integer, db.ForeignKey('CareerPath.course_major.id'))
    course_major = db.relationship('Program', backref='Electives')


# Define the CareerPath table with a schema
class CareePath(db.Model):
    __tablename__ = 'career_path'
    __table_args__ = {'schema': 'CareerPath'}  # Replace 'CareerPath' with your desired schema
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    desc = db.Column(db.String(300), nullable=False)
    course_major_id = db.Column(db.Integer, db.ForeignKey('CareerPath.course_major.id'))
    course_id = db.Column(db.String(300), db.ForeignKey('CareerPath.course.id'))
    course_major = db.relationship('Program', backref='career_path')
    course = db.relationship('courses', backref='career_path')


# Define the semester table with a schema
class Semester(db.Model):
    __tablename__ = 'semester'
    __table_args__ = {'schema': 'CareerPath'}  # Replace 'CareerPath' with your desired schema
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)


# Define the Courses table with a schema
class Course(db.Model):
    __tablename__ = 'courses'
    __table_args__ = {'schema': 'CareerPath'}  # Replace 'CareerPath' with your desired schema
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    desc = db.Column(db.String(300), nullable=False)
    Unit = db.Column(db.Integer, nullable=False)
    semesta_id = db.Column(db.Integer, db.ForeignKey('CareerPath.semester.id'))
    course_status_id = db.Column(db.String(300), db.ForeignKey('CareerPath.course_status.id'))
    course_major_id = db.Column(db.String(300), db.ForeignKey('CareerPath.course_major.id'))
    career_path_id = db.Column(db.String(300), db.ForeignKey('CareerPath.career_path.id'))
    semester = db.relationship('semester', backref='courses')
    course_major = db.relationship('program', backref='courses')
    course_path = db.relationship('career_path', backref='courses')
    course_status = db.relationship('course_status', backref='courses')



class CourseStatus(db.Model):
    __tablename__ = 'course_status'
    __table_args__ = {'schema': 'CareerPath'}  # Replace 'CareerPath' with your desired schema
    id = db.Column(db.String(100), primary_key=True)
    name = db.Column(db.String(100), nullable=False)


class Prerequisite(db.Model):
    __tablename__ = 'preRequisite'
    __table_args__ = {'schema': 'CareerPath'}  # Replace 'CareerPath' with your desired schema
    id = db.Column(db.String(100), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    desc = db.Column(db.String(300), nullable=False)
    unit = db.Column(db.Integer, nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('CareerPath.course.id'))
    status_id = db.Column(db.String(300), db.ForeignKey('CareerPath.course_status.id'))
    course = db.relationship('courses', backref='prerequisite')
    status = db.relationship('course_status', backref='prerequisite')


class preRequisiteWaiver(db.Model):
    __tablename__ = 'preRequisite_waiver'
    __table_args__ = {'schema': 'CareerPath'}  # Replace 'CareerPath' with your desired schema
    id = db.Column(db.String(100), primary_key=True)
    name_of_requester = db.Column(db.String(100), nullable=False)
    Prequisiste_status= db.Column(db.String(100), nullable=False)
    desc = db.Column(db.String(300), nullable=False)
    unit = db.Column(db.Integer, nullable=False)
    waiver_request= db.Column(db.String(100), nullable=False)


# class Student(db.Model):
#     __tablename__ = 'students'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(100))
    
#     # Define the permissions for Student
#     permissions = student_permission(search=True, view=True, create=True)
    
#     # Relationship with courses
#     courses = relationship('Course', backref='student')

# class Course(db.Model):
#     __tablename__ = 'courses'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(100))
#     student_id = Column(Integer, ForeignKey('students.id'))
    
