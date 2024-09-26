from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin
from randnum_gen import randnum_gen
from flask_marshmallow import Marshmallow
from marshmallow import fields
from flask_migrate import Migrate
from flask import Flask
from sqlalchemy import LargeBinary,text, func


app = Flask(__name__, static_folder='static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://careerpath:password@localhost:5432/careerPath'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '1234567'


db = SQLAlchemy(app)
ma = Marshmallow(app)

migrate = Migrate(app, db, compare_type=True ,render_as_batch=True)



# Define the User Login table with a schema
class User(db.Model,UserMixin):
     __tablename__ = 'User'
     __table_args__ = {'schema': 'CareerPath'}  # Replace 'CareerPath' with your desired schema
     id = db.Column(db.Integer(), primary_key=True)
     username = db.Column(db.String(80), unique=True, nullable=False)
     password = db.Column(db.String(100), nullable=False)
     role = db.Column(db.String(100), nullable=False)
     #date=db.Columns(db.DateTime,default-datetime.datetime.now)
#   Define the Student table with a schema
     def __init__(self,id,username,password,role) -> None:
          self.password=password,
          self.id=id,
          self.username=username,
          self.role=role


class UserSchema(ma.Schema):
     class Meta:
          fields=('id','username','password','role')

User_serialized =UserSchema()
Users_serialized =UserSchema(many=True)


# Define the Student Advisor table with a schema
class StudentAdvisor(db.Model):
     __tablename__ = 'student_advisor'
     __table_args__ = {'schema': 'CareerPath'}  # Replace 'CareerPath' with your desired schema
     id = db.Column(db.Integer(), primary_key=True)
     name = db.Column(db.String(80), nullable=False)
     email = db.Column(db.String(80), nullable=False)
     user_id = db.Column(db.Integer(), db.ForeignKey('CareerPath.User.id'))
     userID= db.relationship('User', backref='student_advisor',uselist=False)
     
     # Define the permissions for Student
     #permissions = course_advisor_permission(search=True, view=True, create=True)
 
class Student(db.Model):
     __tablename__ = 'student'
     __table_args__ = {'schema': 'CareerPath'}  # Replace 'CareerPath' with your desired schema
     id = db.Column(db.Integer(), primary_key=True)
     name = db.Column(db.String(80), nullable=False)
     email = db.Column(db.String(150), nullable=False)
     program_ID = db.Column(db.String(150), nullable=True)
     careerpath_name=db.Column(db.String(150), nullable=True)
     user_id = db.Column(db.Integer(), db.ForeignKey('CareerPath.User.id'))
     userID= db.relationship('User', backref='Student',uselist=True)
     studentadvisor_id = db.Column(db.Integer(), db.ForeignKey('CareerPath.student_advisor.id'))
     student_AdviserID= db.relationship('StudentAdvisor', backref='Student',uselist=True)

     # Define the permissions for Student
     #permissions = student_permission(view=True, create=True)

class StudentSchema(ma.Schema):
     class Meta:
          fields=('id','username','email','programID','user_id','studentAdvisor_id')

student_Serialized =StudentSchema()
students_Serialized =StudentSchema(many=True)


class Complain(db.Model):
     __tablename__ = 'complains'
     __table_args__ = {'schema': 'CareerPath'}  # Replace 'CareerPath' with your desired schema
     id = db.Column(db.Integer(), primary_key=True)
     name = db.Column(db.String(80), nullable=False)
     compliant= db.Column(db.String(1000), nullable=True)
     user_id = db.Column(db.Integer(), db.ForeignKey('CareerPath.User.id'))
     userID= db.relationship('User', backref='Complain',uselist=True)
     emailID= db.Column(db.String(1000), nullable=True)



# Define the Course Major table with a schema
class Program(db.Model):
     __tablename__ = 'Program'
     __table_args__ = {'schema': 'CareerPath'}  # Replace 'CareerPath' with your desired schema
     id = db.Column(db.Integer(), primary_key=True)
     name = db.Column(db.String(150), nullable=False)
     program_categories = db.Column(db.String(150), nullable=False)
     Desc = db.Column(db.String(300), nullable=False)
     student_id = db.Column(db.Integer(), db.ForeignKey('CareerPath.student.id'))
     student = db.relationship('Student', backref='Program',uselist=False)



# Define the Elective table with a schema
class Elective(db.Model):
     __tablename__ = 'Electives'
     __table_args__ = {'schema': 'CareerPath'}  # Replace 'CareerPath' with your desired schema
     id = db.Column(db.Integer(), primary_key=True)
     name = db.Column(db.String(100), nullable=False)
     Desc = db.Column(db.String(300), nullable=False)
     Unit = db.Column(db.Integer(), nullable=False)
     program_id = db.Column(db.Integer(), db.ForeignKey('CareerPath.Program.id'))
     program = db.relationship('Program', backref='Electives')

# Define the semester table with a schema


# Define the CareerPath table with a schema
class CareerPaths(db.Model):
     __tablename__ = 'career_Path'
     __table_args__ = {'schema': 'CareerPath'}  # Replace 'CareerPath' with your desired schema
     id = db.Column(db.Integer(), primary_key=True)
     name = db.Column(db.String(100), nullable=False)
     desc = db.Column(db.String(300), nullable=False)
     program_id = db.Column(db.Integer(), db.ForeignKey('CareerPath.Program.id'))
     program = db.relationship('Program', backref='career_Path')

#Schema Serialization into Json.

class CareerPathsSchema(ma.Schema):
     class Meta:
          fields=('id','name','Desc')


class ProgramSchema(ma.Schema):
    id = fields.Integer()
    name = fields.Str()
    program_categories=fields.Str()
    Desc=fields.Str()
    careerPath = fields.Nested("CareerPathsSchema", many=True) #exclude=("program")) #The property name is the same as in bakcref


CareerPath_Serialize=CareerPathsSchema()
CareerPaths_Serialize=CareerPathsSchema(many=True)
Program_CareerPath__Serialized=ProgramSchema(many=True)


class CourseStatus(db.Model):
     __tablename__ = 'course_status'
     __table_args__ = {'schema': 'CareerPath'}  # Replace 'CareerPath' with your desired schema
     id = db.Column(db.Integer(), primary_key=True)
     name = db.Column(db.String(100), nullable=False)


class Student_Profile(db.Model):
     __tablename__ = 'student_profile'
     __table_args__ = {'schema': 'CareerPath'}  # Replace 'CareerPath' with your desired schema
     id = db.Column(db.Integer(), primary_key=True)
     coursename = db.Column(db.String(80), nullable=True)
     course_grade = db.Column(db.String(80), nullable=True)
     courseUnit = db.Column(db.Integer(), nullable=True)
     course_status = db.Column(db.String(80), nullable=True)
     semester_id = db.Column(db.Integer(), nullable=True)
     career_path_name = db.Column(db.String(80), nullable=True)
     student_id = db.Column(db.Integer(), db.ForeignKey('CareerPath.student.id'))
     student = db.relationship('Student', backref='student_profile',uselist=True)

     # Define the permissions for Student
     #permissions = student_permission(view=True, create=True)

class Student_ProfileSchema(ma.Schema):
     class Meta:
          fields=('id','coursename','courseUnit','course_grade','course_status','student_id','course_status_id', 'semester_id','career_path_name')

student_Serialized = Student_ProfileSchema()
students_Serialized = Student_ProfileSchema(many=True)



class Semester(db.Model):
     __tablename__ = 'semesters'
     __table_args__ = {'schema': 'CareerPath'}  # Replace 'CareerPath' with your desired schema
     id = db.Column(db.Integer(), primary_key=True)
     name = db.Column(db.String(100), nullable=False)


# Define the Courses table with a schema
class Course(db.Model):
     __tablename__ = 'courses'
     __table_args__ = {'schema': 'CareerPath'}  # Replace 'CareerPath' with your desired schema
     id = db.Column(db.Integer(), primary_key=True)
     name = db.Column(db.String(100), nullable=False)
     desc = db.Column(db.String(300), nullable=False)
     unit = db.Column(db.Integer(), nullable=False)
     semesta_id = db.Column(db.Integer(), db.ForeignKey('CareerPath.semesters.id'))
     course_status_id = db.Column(db.Integer(), db.ForeignKey('CareerPath.course_status.id'))
     program_id = db.Column(db.Integer(), db.ForeignKey('CareerPath.Program.id'))
     career_path_id = db.Column(db.Integer(), db.ForeignKey('CareerPath.career_Path.id'))
     semester = db.relationship('Semester', backref='courses')
     program = db.relationship('Program', backref='courses')
     course_path = db.relationship('CareerPaths', backref='courses')
     course_status = db.relationship('CourseStatus', backref='courses')


class CourseSchema(ma.Schema):
     class Meta:
          fields=('id','name','unit','desc','semesta_id','course_status_id','program_id','career_path_id')

course_Serialized =StudentSchema()
course_many_Serialized =StudentSchema(many=True)


class CareerPath(ma.Schema):
    id = fields.Integer()
    name=fields.Str()
    Desc=fields.Str()
    careerPath = fields.Nested("CourseSchema", many=True) 

course_CareerPath_Serialized = CareerPathsSchema(many=True)


class Prerequisite(db.Model):
     __tablename__ = 'prerequisite'
     __table_args__ = {'schema': 'CareerPath'}  # Replace 'CareerPath' with your desired schema
     id = db.Column(db.String(100), primary_key=True)
     name = db.Column(db.String(100), nullable=False)
     desc = db.Column(db.String(300), nullable=False)
     unit = db.Column(db.Integer(), nullable=False)
     course_id = db.Column(db.Integer(), db.ForeignKey('CareerPath.courses.id'))
     status_id = db.Column(db.String(300), db.ForeignKey('CareerPath.course_status.id'))
     semester_id = db.Column(db.Integer(), db.ForeignKey('CareerPath.semesters.id'))
     course = db.relationship('Course', backref='prerequisite')
     status = db.relationship('CourseStatus', backref='prerequisite')
     semester = db.relationship('Semester', backref='prerequisite')


class PrerequisiteSchema(ma.Schema):
     class Meta:
          fields=('id','name','unit','desc','semester_id','course_id','status_id')

prequisite_Serialized =PrerequisiteSchema()
prequisite_many_Serialized =PrerequisiteSchema(many=True)



def default_attachment():
        # You can implement logic here to generate the default value
        return b'default_binary_data'


class preRequisiteWaiver(db.Model):
     __tablename__  = 'prerequisite_waiver'
     __table_args__ = {'schema': 'CareerPath'}  # Replace 'CareerPath' with your desired schema
     id = db.Column(db.String(100), primary_key=True)
     name_of_requester = db.Column(db.String(100), nullable=False)
     Prequisiste_status= db.Column(db.String(100), nullable=False)
     waiver_request_details = db.Column(db.String(1000), nullable=False)
     pre_unit = db.Column(db.Integer(), nullable=False)
     prequisite_name = db.Column(db.String(100), nullable=False)
     semester_id = db.Column(db.Integer(), primary_key=True)
     student_id = db.Column(db.Integer(), primary_key=True)
     career_path_name =  db.Column(db.Integer(), db.ForeignKey('CareerPath.semesters.id'))
     attachment    = db.Column(LargeBinary,server_default=func.default_attachment())  # Blob column for attachments
     Prerequisite  = db.relationship('Semester', backref='prerequisite_waiver')