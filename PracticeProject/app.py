from sqlalchemy import text,select,literal_column,func,update
from flask import render_template, request, jsonify, redirect, url_for, flash,session,Markup,send_file
from flask_login import LoginManager, login_user, login_required, logout_user
import pygraphviz as pgv
from werkzeug.utils import secure_filename
#from randnum_gen import randnum_gen
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo, Length
from flask_mail import Mail, Message
import sys
import json
import os
from sqlalchemy.orm import aliased
sys.path.insert(1, '/Users/prosper/my_sandbox/PracticeProject')
from model import *
import base64


app = app
# Configure Flask-Mail for sending password reset emails
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'awsengineerdevops@gmail.com'
app.config['MAIL_PASSWORD'] = 'brpncdvavxxobmvt'
app.config['MAIL_DEFAULT_SENDER'] = 'awsengineerdevops@gmail.com.com'
app.config['UPLOAD_FOLDER'] = '/Users/prosper/Downloads/CareerPath'
app.config['ALLOWED_EXTENSIONS'] = {'pdf', 'txt', 'png', 'jpg', 'jpeg', 'gif','csv'}

mail = Mail(app)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    # role = SelectField('Role', choices=[('student', 'Student'), ('advisor', 'Advisor')], validators=[DataRequired()])
    submit = SubmitField('Login')


class ComplainForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    compliant = StringField('compliant', validators=[DataRequired()],render_kw={"placeholder": "Enter your complaint here"})
    emailID = StringField('Email-ID', validators=[DataRequired()])
    # role = SelectField('Role', choices=[('student', 'Student'), ('advisor', 'Advisor')], validators=[DataRequired()])
    submit = SubmitField('Submit')

class PasswordResetForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Submit')


class PasswordRecoveryForm(FlaskForm):
    userid = StringField('UserID',  validators=[DataRequired()])
    password = PasswordField('New Password', validators=[
        DataRequired(),
        Length(min=8, message='Password must be at least 8 characters long'),
        EqualTo('confirm_password', message='Passwords must match')
    ])
    confirm_password = PasswordField(
        'Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Reset Password')


# ===================
# Login Manager
# ==================

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(id):
    # Load the User instance from the database based on user_id
    return User.query.get(int(id))



#Profile Validator
def profileValidator()-> jsonify:
    login_username= str(session.get('username'))
    stmt = (
     db.session.query(
        Student.careerpath_name.label("careerpath_name"),
        Student.program_ID.label("program_ID")
    )
        .select_from(Student)
        .join(User, Student.user_id == User.id)
        .filter(User.username == str(login_username))
        )
    
    result = stmt.all()
    
    # Serialize the query result to get only the "name" field
    careerPath = [{'careerpath_name': record[0],'program_ID': record[1]} for record in result]
    print('proilevalidatorCareer',careerPath)
    return careerPath


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
         username=form.username.data
         session['username'] = username
         # Check if the user exists in the database and the password entered matches the password in the database
         user = User.query.filter_by(username=form.username.data).first()
         if user and user.password == form.password.data and user.role == 'student':
                login_user(user)
                # Checks if the user has any exisiting profile 
                # If UserProfile is exists then user is routed backed to their profile      
                if profileValidator()[0]['careerpath_name'] != None:
                    selected_category = profileValidator()[0]['careerpath_name']
                    selected_subcategory = profileValidator()[0]['careerpath_name']
                    session['selected_category'] = selected_category
                    session['selected_subcategory'] = selected_subcategory
                    flash('Welcome back to your Profile {}'.format(str(session.get('username')))) 
                    return redirect(url_for('generate_view_profile_exists'))
                else:   
                   flash('Login was successful , please preview careerpath or Create careerPath') 
                   return redirect(url_for('careerSelection_page'))
         elif user and user.password == form.password.data and user.role == 'advisor':
                  # Login the user
                login_user(user)
                flash('Login successful', 'success')
                return redirect(url_for('adviserPage'))
         else:
               flash('Login failed. Check your username and password.')

    return render_template('login.html', form=form)


# =================================
# Password reset route
# =================================

@app.route('/password_reset', methods=['GET', 'POST'])
def password_reset():
    form_reset = PasswordResetForm()
    if form_reset.validate_on_submit():
        # Send a password reset email to the user
        user_email = form_reset.email.data
        # Implement your email sending logic here using Flask-Mail
        msg = Message(
            'Password Reset', sender='awsengineerdevops@gmail.com', recipients=[user_email])
        msg.body = 'Click the link below to reset your password.'
        msg.html = '<a href="{}">Reset Password</a>'.format(
            'http://127.0.0.1:5000/password_recovery')
        print(msg.html)
        print(mail.send(msg))
        mail.send(msg)

        flash('Password reset email sent. Check your email for instructions.', 'success')
        return redirect(url_for('login'))
    return render_template('password_reset.html', form_reset=form_reset)


# ======================================
# Password recovery route
# ======================================

@app.route('/password_recovery', methods=['GET', 'POST'])
def password_recovery():
    form_recovery = PasswordRecoveryForm()
    if form_recovery.validate_on_submit():
        userid = form_recovery.userid.data
        query = User.query.filter_by(id=userid)
        new_password_value = form_recovery.password.data
        # Update records
        # Replace "some_column" and "new_value" with your actual update values
        query.update({"password": new_password_value})

        # Commit the changes to the database
        db.session.commit()
        # Update the user's password in the database (implement this logic)
        flash('Password reset successfully. You can now log in with your new password.', 'success')
        return redirect(url_for('login'))
    return render_template('password_recovery.html', form_recovery=form_recovery)



# ==============================
#Landing Page for our website
# ==============================

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/market')
def market_page():
    items = [
        {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
         {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
         {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
        ]
    return render_template('market.html', items=items)



# ==============================
# Complian form
# ==============================

with open("static/careerTrackerlogo.png", "rb") as image_file:
    encoded_image = base64.b64encode(image_file.read()).decode('utf-8')


@app.route('/complain', methods=['GET', 'POST'])
def complain():
    form_complain = ComplainForm()
    if form_complain.validate_on_submit():
        name = form_complain.name.data
        complaint=form_complain.compliant.data
        emailID=form_complain.emailID.data
        # Create a new student record and insert it into the database
        new_compliant = Complain(name=name, compliant=complaint,emailID=emailID)
        db.session.add(new_compliant )
        db.session.commit()
        # Update the user's password in the database (implement this logic)
        flash('Complaint was sent successfully')
        msg = Message(
            'Complaint Recieved', sender='awsengineerdevops@gmail.com', recipients=[emailID])
        msg.html = """
                <p>We sincerely appreciate you taking the time to bring the matter to our attention.</p>
                <p>Your feedback is valuable to us, and we take your concerns seriously.</p>
                <p>Our team is currently reviewing the details of your complaint thoroughly.</p>
                <p><a href="http://127.0.0.1:5000">Return to Homepage</a></p>
                <img src="data:image/png;base64,{encoded_image}" alt="Your Logo" style="max-width: 100%;">
                """
        # Attach the image to the email
        print(msg.html)
        print(mail.send(msg))
        mail.send(msg)
        return redirect(url_for('home_page'))
    return render_template('complain.html', form_complain=form_complain)



# ==============================
# Programs Selection Page
# ==============================


@app.route('/careerSelection', methods=['GET', 'POST'])
@login_required
def careerSelection_page():

    return render_template('career_selectionPage.html', programs=get_Program())

# Support function for Program Selection route


def get_Program():
    values_from_program_column = "name"
    query = db.session.query(getattr(Program, values_from_program_column))
    programs = query.all()
    result = Program_CareerPath__Serialized.dump(programs)
    return result



# =======================================================
#Route to get all Career Paths based on Program selected
# =======================================================


@app.route('/get_subcategories', methods=['POST'])
@login_required
def get_subcategories():
    selected_category = request.form['category']
    print("Selected Category:", selected_category)
    career_names = "name"
    query = db.session.query(getattr(CareerPaths,  career_names)).join(
        CareerPaths.program).filter(Program.name == str(selected_category))
    
    # Execute the query to get the result

    result = Program_CareerPath__Serialized.dump(query)
    return result




#Sending email

@app.route('/send_email')
def send_email():
    # Create and send an email
    msg = Message('Hello from Flask', sender='your_email@gmail.com',
                  recipients=['recipient@example.com'])
    msg.body = 'This is a test email sent from Flask using Gmail SMTP.'
    mail.send(msg)
    return 'Email sent successfully!'


# ====================================================
# A place holder for passing global session variables
# ====================================================

@app.route('/get_graph_data', methods=['GET', 'POST'])
@login_required
def generate_graph():
    selected_category = None
    selected_subcategory = None

    if request.method == 'POST':
        selected_category = request.form['category']
        selected_subcategory = request.form['subcategory']

        session['selected_category'] = selected_category
        session['selected_subcategory'] = selected_subcategory
        print("Selected Category:", selected_category, selected_subcategory)
        return selected_category, selected_subcategory


# ==================================================================================
# A place holder for getting frontend variables for course from student profile 
# which is then passed to  session variables to update student profile table
# ==================================================================================

@app.route('/get_course_grade_data', methods=['GET', 'POST'])
@login_required
def generate_grade_courses():

    student_id = numeric_userID_generator()
    selected_course = None
    selectedGrade   = None
    if request.method == 'POST':

        selected_course = request.form['selected_course']
        selectedGrade = request.form['selected_Grade']
        # session['selected_course'] = selected_course 
        # session['selectedGrade'] = selectedGrade
        print("Selected Category:",  selected_course, selectedGrade)
        update_course_grade(student_id, course_name=selected_course, new_grade_value=selectedGrade)
        return [selected_course , selectedGrade]
    
# ============================================
# Student profile grade update 
# ============================================

def update_course_grade(student_id, course_name, new_grade_value):
    stmt = (
        update(Student_Profile)
        .where(
            (Student_Profile.coursename == course_name) &
            (Student_Profile.student_id == student_id)
        )
        .values(course_grade=new_grade_value)
    )

    # Execute the update statement
    db.session.execute(stmt)
    db.session.commit()

# ==================================================================================
# A place holder for getting frontend variables for course from student profile 
# which is then passed to  session variables to update student profile table
# ==================================================================================

@app.route('/preqiuiste_waiver_data', methods=['GET', 'POST'])
@login_required
def preqiuiste_waiver_data2():
    try:
        student_id = numeric_userID_generator()
        prequisiteName = None
        prequisisteStatus = None
                    
        if request.method == 'POST':
            #Print the entire form data
            prequisiteName = request.form['prerequisiteName']
            preUnit = request.form['preUnit']
            prequisisteStatus = request.form['prerequisiteStatus']
            reasonForWaiver = request.form['reasonForWaiver']
            attachment= request.files['attachment']
            if attachment.filename == '':
                flash("Attach your requeat waiver form")
                return redirect(request.url)
            # Read the file content as binary data
            elif attachment and allowed_file(attachment.filename):
                # Save the file with a secure filename
                filename = secure_filename(attachment.filename)
                attachment.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            
            # Read the file content as binary data
                with open(os.path.join(app.config['UPLOAD_FOLDER'], filename), 'rb') as file:
                    file_content_binary = file.read()
            # # session['selected_course'] = selected_course 
            # # session['selectedGrade'] = selectedGrade
            print([prequisiteName,prequisisteStatus,preUnit,reasonForWaiver,attachment])
            prequisite_Status_update(student_id, course_name=prequisiteName,reasonForWaiver=reasonForWaiver,attachment=file_content_binary)
            return [prequisiteName,prequisisteStatus,preUnit,reasonForWaiver,attachment ]
    except Exception as e:
        # Log any exceptions that might occur during form processing
        app.logger.error(f"Error in preqiuiste_waiver_data: {e}")

        # Return an error response
        return jsonify({'result': 'error', 'message': str(e)}), 500


# ============================================
# Student profile grade update 
# ============================================


def sendmailNotification(recipientemail=None,msgBody=None)->str:
        msg = Message(
            'Prequisite Approval', sender='awsengineerdevops@gmail.com', recipients=[recipientemail])
        msg.html = msgBody
        # Attach the image to the email
        print(msg.html)
        print(mail.send(msg))
        mail.send(msg)
     


def get_student_name_email_advisor()-> str:
   user_numeric_id= numeric_userID_generator()
   stmt = (
    select(
        Student.email.label("student_email"),
        StudentAdvisor.email.label("studentAdvisor_email"),
        Student.name.label("student_name"),
    )
    .distinct()
    .select_from(Student)
    .join(StudentAdvisor, StudentAdvisor.id==Student.studentadvisor_id)
   ).where(Student.user_id == user_numeric_id)
    
   result = db.session.execute(stmt).all()
    # Serialize the query result to get only the "name" field
   course_profile_list = [{'student_email': record[0],'studentAdvisor_email':record[1],'student_name':record[2]} for record in result]
   print(course_profile_list)
   return course_profile_list



def prequisite_Status_update(student_id, course_name,new_Status_value=None,reasonForWaiver=None,attachment=None):
    new_Status_value="Pending"
    stmt = (
        update(preRequisiteWaiver)
        .where(
            (preRequisiteWaiver.prequisite_name == course_name) &
            (preRequisiteWaiver.student_id == student_id)
        )
        .values(Prequisiste_status=new_Status_value,waiver_request_details=reasonForWaiver,attachment=attachment)
    )

    # Execute the update statement
    db.session.execute(stmt)
    db.session.commit()
    
    student_email = get_student_name_email_advisor()[0]["student_email"]
    msgBody = """
                 <p>Your prerequisite waiver request has been sent to your Adviser </p>
                 <p>You will recieve a notification when your request approved by your course adviser</p>
                 <p><a href="http://127.0.0.1:5000">Return to Homepage</a></p>
              """
    sendmailNotification(recipientemail=student_email,msgBody=msgBody) # notification to student

    
    student_advisor_email = get_student_name_email_advisor()[0]["studentAdvisor_email"]
    msg_body = """
                 <p> You have pending prerequisite waiver request from {} </p>
                 <p><a href="http://127.0.0.1:5000">Return to Homepage</a></p>
               """.format(get_student_name_email_advisor()[0]["student_name"])
    sendmailNotification(recipientemail = student_advisor_email ,msgBody= msg_body) # notification to Career Advisor

    
# ============================================
# Rendering Preview Careerpath View Page
# ============================================

def graphAttributes():
    return  pgv.AGraph(strict=False, directed=True, bgcolor='#212121')
        

def node_creator(node,Semester_id,selected_subcategory_lower):
    G = graphAttributes()
    G.graph_attr['size'] = '20,20'
    G.add_node(node, shape='ellipse', strict=False, directed=True,beautify=True,color="Olive",fontcolor='white',style='filled')

    column_name1 = "Unit"
    print(Semester_id, selected_subcategory_lower)
    query = db.session.query(Course.name, text('"CareerPath".courses."{}"'.format(column_name1)))
    query = query.join(Course.course_path).filter(Course.semesta_id == Semester_id,CareerPaths.name == str(selected_subcategory_lower))

    # Serialize the query result to get only the "name" field
    course_list = [{'name': record[0], 'record': '{}&#92;n{}'.format(record[0], record[1])} for record in query.all()]
    print(course_list)

    # Add the courses to the graph and create edges dynamically
    for course in course_list:
        G.add_node(course['name'], label=course['record'], shape='record', width='0.5', height="0.5" ,color="Teal",
        rank='same', strict=False, directed=True,beautify=True,bgcolor='lightyellow',
                        filledcolor="red", fontcolor='white', style='filled',fontsize="8")
        G.add_edge(node, course['name'], color="blue")

    graph_svg = G.draw(format='svg', prog='dot').decode('utf-8')
    graph_html = Markup(graph_svg)
    return graph_html


# ===========================================================================================
# This route will be used to generate a prwview page where a student can review their profile
# Before deciding whether create a profile From the Career Selection page
# ===========================================================================================

@app.route('/generate_graph')
@login_required
def get_graph(html_to_render='graph.html'):

        selected_category = str(session.get('selected_category')).upper()
        selected_subcategory_lower = str(session.get('selected_subcategory'))
        selected_subcategory = str(session.get('selected_subcategory')).upper()

        # First Semester Graph

        node = '1stSemester'
        Semester_id = 1
        graph_html=node_creator(node,Semester_id,selected_subcategory_lower)
        
        node = '2nd Semester'
        Semester_id = 2
        graph_html2=node_creator(node,Semester_id,selected_subcategory_lower)

        node = '3rd Semester'
        Semester_id = 3
        graph_html3=node_creator(node,Semester_id,selected_subcategory_lower)

        node = '4th Semester'
        Semester_id = 4
        graph_html4=node_creator(node,Semester_id,selected_subcategory_lower)

        node = '5th Semester'
        Semester_id = 5
        graph_html5=node_creator(node,Semester_id,selected_subcategory_lower)

        node = '6th Semester'
        Semester_id = 6
        graph_html6=node_creator(node,Semester_id,selected_subcategory_lower)

        node = '7th Semester'
        Semester_id = 7
        graph_html7=node_creator(node,Semester_id,selected_subcategory_lower)

        node = '8th Semester'
        Semester_id = 8
        graph_html8=node_creator(node,Semester_id,selected_subcategory_lower)

        return render_template(html_to_render, graph_html=graph_html, graph_html2=graph_html2, graph_html3=graph_html3, graph_html4=graph_html4, graph_html5=graph_html5, graph_html6=graph_html6, graph_html7=graph_html7, graph_html8=graph_html8, selected_category=selected_category, selected_subcategory=selected_subcategory)


#  ========================================================================
#  This route will be used to generate a new profile when a student click on
#  Create profile from profile selection page,
#  Context when a Student want to create profile, the genrate Update 
#  the Student table before calling the generate_view_profile_exists 
#  =======================================================================
#Profile Validator
def student_existing_courseRecords_Validator()-> list('jsonify'):
    login_username= str(session.get('username'))
    stmt = (
     db.session.query(
        Student.id.label("studentID")
    )
        .select_from(Student)
        .join(User, Student.user_id == User.id)
        .join(Student_Profile, Student_Profile.student_id == Student.id)
        .filter(User.username == str(login_username))
        )
    
    result = stmt.all()
      # Serialize the query result to get only the "name" field
    profile_result = [{'name': record[0]} for record in result]
    return profile_result

# ===================================
  #Numeric ID generation based userID login
# ===================================

def numeric_userID_generator():
    userid = db.session.query(User.id).filter(User.username==str(session.get('username')))
    # Use .scalar_subquery() to produce a scalar subquery
    user_id_values = userid.scalar()
    return user_id_values



@app.route('/ref_generate_profile',methods=['GET', 'POST'])
@login_required
def ref_generate_view_for_new_profile():
    posted_student_id = None

    if request.method == 'POST':
        posted_student_id = request.form['student_id']




@app.route('/generate_profile',methods=['GET', 'POST'])
@login_required
def generate_view_for_new_profile(override_numeric_userID_generator=None):
    selected_category = str(session.get('selected_category'))
    selected_subcategory_lower = str(session.get('selected_subcategory'))
    # Your conditional statement
    # print(str(session.get('username')))
    column_name1='careerpath_name'
    column_name2='program_ID'
    if override_numeric_userID_generator != None:
        pass
    else:
        override_numeric_userID_generator = numeric_userID_generator()

    query = Student.query.filter(Student.user_id == override_numeric_userID_generator )
    print(query.all())
    # Once the Student Table is pre-loaded and
    query.update({column_name2: selected_category,column_name1: selected_subcategory_lower})
    
    if student_existing_courseRecords_Validator():
        flash("User has an existing profile, Please delete current profile,to create a new one")
        return redirect(url_for('generate_view_profile_exists'))
    else:
        # List of JSON objects
        json_list = _profileCourseSelection()
        print(json_list)
        # Create instances for each record
        records = [Student_Profile(**json_obj) for json_obj in json_list]

        # Add records to the session
        db.session.add_all(records)     
        
        db.session.commit()
        # Redirect to a different route
        flash("Your Career profile has been created")
        return redirect(url_for('generate_view_profile_exists'))
    
    
    
# ================================================================================================
# Support function  for Courses selection Courses Grade update Dropdown on the profile page section
# ==============================================================================================

def _profileCourseSelection() -> jsonify:

    """
    Support function support the profile generation creation
    The validation function checks using Studentexisting_corse_validation function cheks is student profile 
    Have been prepopulated with coureses if not, then this function called to do the job
    And where Student coures profile exixt in Student_profile, Table there is no action

    """

    selected_subcategory= str(session.get('selected_subcategory'))
    column_name1 = "Unit"
    user_numeric_id=numeric_userID_generator()
    stmt = (
    select(
        Course.name.label("name"),
        literal_column("''").label("Grade"),  # Use literal_column for an empty string
        literal_column('"CareerPath".courses."{}"'.format(column_name1)).label("Unit"),
        literal_column("''").label("course_status"),  # Use literal_column for an empty string
        User.id.label("user_id"),
        Semester.id.label("semester_id"),
        CareerPaths.name.label("career_path_name")
    )
    .distinct()
    .select_from(Student)
    .join(User, User.id == Student.user_id)
    .join(Program, Student.program_ID == Program.name)
    .join(CareerPaths, Program.id == CareerPaths.program_id)
    .join(Course, CareerPaths.id == Course.career_path_id)
    .join(Semester, Course.semesta_id == Semester.id)
   ).where(CareerPaths.name == str(selected_subcategory) , Student.user_id == user_numeric_id)
    
    result = db.session.execute(stmt).all()
    # Serialize the query result to get only the "name" field
    course_profile_list = [{'coursename': record[0],'course_grade':record[1],'courseUnit':record[2],'course_status':record[3],\
                                'student_id':record[4],'semester_id':record[5],'career_path_name': record[6]} for record in result]
    return course_profile_list



# ==========================
# Course Selection funtion
# ==========================


def _profileCourse_Status_updater() -> jsonify:
    """
    This selection is used to fillUp the courses portion for grade update.
    """
    selected_subcategory= str(session.get('selected_subcategory'))
    # Assuming you have the necessary model classes defined (Student, Program, CareerPaths, Course, Semester)
    # and the appropriate relationships are established

    # Alias for Program table to avoid ambiguity in the query
    program_alias = aliased(Program)

    stmt = (
        select(
            Course.name.label("name")
        )
        .distinct()
        .select_from(Student)
        .join(Program, Student.program_ID == Program.name)
        .join(CareerPaths, Program.id == CareerPaths.program_id)
        .join(Course, CareerPaths.id == Course.career_path_id)
        .join(Semester, Course.semesta_id == Semester.id)
        .filter(CareerPaths.name == str(selected_subcategory))
        )
    result = db.session.execute(stmt).all()
    # Serialize the query result to get only the "name" field
    course_list_with_grades_selection = [{'name': '{}'.format(record[0])} for record in result]
    return course_list_with_grades_selection



def node_profile_creator(node,Semester_id):
    G = graphAttributes()
    G.graph_attr['size'] = '20,20'
    G.add_node(node, shape='ellipse', strict=False, directed=True,beautify=True,color="Olive",fontcolor='white',style='filled',fontsize="8")
    
    """
    This section queries the Student_profile base on prepoulation by _profileCourseSelection function
    """
    query = db.session.query(Student_Profile.coursename, Student_Profile.course_grade,Student_Profile.courseUnit)
    query = query.filter(Student_Profile.student_id == numeric_userID_generator(),Student_Profile.semester_id==Semester_id)
    print(query)
    # Execute the query to get the result
    query.all()

    # Serialize the query result to get only the "name" field
    course_list = [{'name': record[0], 'record': '{}&#92;n{}&#92;n{}'.format(record[0], record[2],record[1])} for record in query.all()]

    # Add the courses to the graph and create edges dynamically
    for course in course_list:
        G.add_node(course['name'], label=course['record'], shape='record', width='0.5', height="0.5" ,color="Teal",rank='same',\
                    strict=False, directed=True,beautify=True, fontcolor='white', style='filled',fontsize="8")
        G.add_edge(node, course['name'], color="blue")

    graph_svg = G.draw(format='svg', prog='dot').decode('utf-8')
    graph_html = Markup(graph_svg)
    return graph_html

# =========================================================================================
# This function is called when the student profile already exisits
# =========================================================================================


@app.route('/generate_view_profile_exists')
@login_required
def generate_view_profile_exists(html_to_render = 'student_profilepage.html'):

        selected_category = str(session.get('selected_category')).upper()
        selected_subcategory_lower = str(session.get('selected_subcategory'))
        selected_subcategory = str(session.get('selected_subcategory')).upper()
        trigger_prequisite_table_population = _prequisiteLoader_and_selector()
        print(trigger_prequisite_table_population )
       
        # First Semester Graph

        node = '1stSemester'
        Semester_id = 1
        #if records already exists:
        #      func(" That select from the studentProfile")
        # else:
        #      func("query Session that update student profile")
        graph_html= node_profile_creator(node,Semester_id)
        
        # semester Presequisiste
        first_semester_prequisiste = _node_profile_prequiste_selector(Semester_id)
        #print(first_semester_prequisiste)
        test =_prequisteSelection()
        print(test)
        
        node = '2nd Semester'
        Semester_id = 2
        graph_html2= node_profile_creator(node,Semester_id)
        # semester Presequisiste
        second_semester_prequisiste = _node_profile_prequiste_selector(Semester_id)

        node = '3rd Semester'
        Semester_id = 3
        graph_html3= node_profile_creator(node,Semester_id)
        # semester Presequisiste
        third_semester_prequisiste = _node_profile_prequiste_selector(Semester_id)

        node = '4th Semester'
        Semester_id = 4
        graph_html4= node_profile_creator(node,Semester_id)
        # semester Presequisiste
        fouth_semester_prequisiste = _node_profile_prequiste_selector(Semester_id)

        node = '5th Semester'
        Semester_id = 5
        graph_html5=  node_profile_creator(node,Semester_id)
        # semester Presequisiste 
        fifth_semester_prequisiste = _node_profile_prequiste_selector(Semester_id)

        node = '6th Semester'
        Semester_id = 6
        graph_html6= node_profile_creator(node,Semester_id)
        # semester Presequisiste
        sixth_semester_prequisiste = _node_profile_prequiste_selector(Semester_id)

        node = '7th Semester'
        Semester_id = 7
        graph_html7= node_profile_creator(node,Semester_id)
         # semester Presequisiste
        seventh_semester_prequisiste = _node_profile_prequiste_selector(Semester_id)

        node = '8th Semester'
        Semester_id = 8
        graph_html8= node_profile_creator(node,Semester_id)
         # semester Presequisiste
        eigth_semester_prequisiste = _node_profile_prequiste_selector(Semester_id)

        return render_template(html_to_render, graph_html = graph_html, graph_html2 = graph_html2, graph_html3 = graph_html3, 
                                               graph_html4 = graph_html4, graph_html5 = graph_html5, graph_html6 = graph_html6, 
                                               graph_html7 = graph_html7, graph_html8=graph_html8, selected_category = selected_category, 
                                               selected_subcategory = selected_subcategory,
                                               first_semester_prequisiste=first_semester_prequisiste,
                                               second_semester_prequisiste = second_semester_prequisiste,
                                               third_semester_prequisiste  = third_semester_prequisiste, 
                                               fouth_semester_prequisiste  = fouth_semester_prequisiste,
                                               fifth_semester_prequisiste  = fifth_semester_prequisiste,
                                               sixth_semester_prequisiste = sixth_semester_prequisiste,
                                               seventh_semester_prequisiste = seventh_semester_prequisiste,
                                               eigth_semester_prequisiste = eigth_semester_prequisiste ,
                                               list_of_courses = _profileCourse_Status_updater(),
                                               tota_course_unit=totalCourseUnit())




# Support function for prequiste requiremnents selection

def _prequisteSelection() -> jsonify:
    """
    params- > Semester_id : this semester id to extract all the prequisite for particualar semester
    Base on STudent careerPath Selection, prequisite are loaded into prequisite_waiver_table 
     which is then used to select prequisite  based on matching conditions
     However, the prequisite_waiver_table is first validated by _prequisiteLoader_and_selector function 
     if student prequisite already exists in the prequisiste_waiver Table no action is required else 
     this function popuplates the prequisite_waiver_table
    """
    selected_subcategory= str(session.get('selected_subcategory'))
    user_numeric_id = numeric_userID_generator()
    column_name1 = "Unit"
    stmt = (
    select(
        Student.name.label("name_of_requester"),
        CourseStatus.name.label("Prequisite_status"),
        literal_column("''").label("waiver_request_details"),
        Prerequisite.unit.label("pre_unit"),
        literal_column("''").label("attachment"),
        Prerequisite.name.label("prequisite_name"),
        Prerequisite.semester_id.label("semester_id"),
        Student.id.label("StudentID"),
        CareerPaths.name.label("CareerPath"),
        #literal_column('"CareerPath".courses."{}"'.format(column_name1)).label("Unit")
    )
    .distinct()
    .select_from(Prerequisite)
    .join(Course, Course.id == Prerequisite.course_id)
    .join(CourseStatus, CourseStatus.id == Prerequisite.status_id)
    .join(CareerPaths, CareerPaths.id == Course.career_path_id)
    .join(Program, CareerPaths.program_id == Program.id)
    .join(Student, Student.program_ID == Program.name)
    ).where(CareerPaths.name == str(selected_subcategory), Student.id==user_numeric_id)
    
    result = db.session.execute(stmt).all()
    print(result)
    # Serialize the query result to get only the "name" field
    prequisite_profile_list = [{'name_of_requester': record[0],'Prequisiste_status':record[1],\
                                    'waiver_request_details':record[2],'pre_unit':record[3],'attachment':record[4],\
                                         'prequisite_name':record[5],'semester_id':record[6],'student_id':record[7],'career_path_name':record[8]} for record in result]
    print(prequisite_profile_list)
    return prequisite_profile_list


# ==========================================
# Prequisite_waive table loader and selector
#===========================================

def _prequisiteLoader_and_selector()-> json:
    user_numeric_id = numeric_userID_generator()
    stmt = (
    select(
    
        preRequisiteWaiver.student_id.label("StudentID")
    )
    .distinct()
    .select_from(preRequisiteWaiver)
   ).where(preRequisiteWaiver.student_id == user_numeric_id)
    
    result = db.session.execute(stmt).all()
    # Serialize the query result to get only the "name" field
    prequisite_list = [{'name': '{}'.format(record[0])} for record in result]
    if prequisite_list :
        pass
    else :

        pre_popluate_prequisite_table_list = _prequisteSelection()
        # List of JSON objects
        print(pre_popluate_prequisite_table_list)
       
        #Selecting default binary object as attachment

        default_attachment_value = b'default_binary_data'
        # Modify each JSON object to include the default value for the attachment column
        for json_obj in pre_popluate_prequisite_table_list:
             json_obj['attachment'] = default_attachment_value

        # Create instances for each record
        records = [preRequisiteWaiver(**json_obj) for json_obj in pre_popluate_prequisite_table_list]

        # Add records to the session
        db.session.add_all(records)     
        
        db.session.commit()

        return "Operation Succesful"
    
# =========================================
#  Prequisite selected from created profile
# =========================================

def _node_profile_prequiste_selector(semester:int) -> json:

    stmt=(
      select(
    
        preRequisiteWaiver.prequisite_name,
        preRequisiteWaiver.pre_unit,
        preRequisiteWaiver.Prequisiste_status,

    )
    .distinct()
    .select_from(Student_Profile)
   ).where(preRequisiteWaiver.semester_id == semester)
    
    result = db.session.execute(stmt).all()
    print(result)
    prequisite_profile_list = [{'prequisite_name':record[0],'pre_unit':record[1],'Prequisiste_status':record[2]} for record in result]
   
    return prequisite_profile_list


# =========================================
#  Total Unit courses for careerPath
# =========================================

def totalCourseUnit() -> json:

    selected_subcategory= str(session.get('selected_subcategory'))
    user_numeric_id = numeric_userID_generator()
    column_name1 = "Unit"
    stmt = (
   
    select(func.sum(literal_column('"CareerPath".courses."{}"'.format(column_name1))).label("Total_Unit"))
    .select_from(Student)
    .join(Program, Student.program_ID == Program.name)
    .join(CareerPaths, CareerPaths.program_id==Program.id)
    .join(Course, Course.career_path_id==CareerPaths.id)
    ).where(CareerPaths.name == str(selected_subcategory), Student.user_id==user_numeric_id)
    
    result = db.session.execute(stmt).all()
    print(result)
    # Check if there are results before accessing the first element
    if result:
        total_Course_unit = result[0][0]
        print(total_Course_unit)
        return total_Course_unit
    else:
        return 0  




#===================================
# Course Advisor Display Dashboard
#==================================

# Support function
def _getStudentMapped_to_advisor():
    user_numeric_id = numeric_userID_generator()

    stmt=(
      select(
      StudentAdvisor.user_id,
      Student.name,
      Student.program_ID
    )
    .distinct()
    .select_from(Student)
    .join(StudentAdvisor,StudentAdvisor.id==Student.studentadvisor_id)
   ).where(StudentAdvisor.user_id==user_numeric_id)
    print(stmt)
    result = db.session.execute(stmt).all()
    prequisite_profile_list = [{'Student_ID':record[0],'Name':record[1],'Major':record[2]} for record in result]
    print(prequisite_profile_list)
    return prequisite_profile_list



@app.route('/Adviser_dasboard')
@login_required
def adviserPage():

    return render_template('course_Advice_view.html',studentlist=_getStudentMapped_to_advisor() ,prerequisitelist=_prerequisiste_approvaladvisor())





# =====================================================
# Student Prerequisite list retrieval mapped to Adbisor
#========================================================

def _prerequisiste_approvaladvisor():
    user_numeric_id = numeric_userID_generator()

    stmt=(
      select(
      preRequisiteWaiver.prequisite_name,
      preRequisiteWaiver.waiver_request_details,
      preRequisiteWaiver.pre_unit,
      preRequisiteWaiver.attachment,
      preRequisiteWaiver.student_id
    )
    .distinct()
    .select_from(preRequisiteWaiver)
    .join(Student, Student.id == preRequisiteWaiver.student_id)
    ).where(preRequisiteWaiver.Prequisiste_status=='Pending',Student.studentadvisor_id==user_numeric_id)
    print(stmt)
    print(user_numeric_id)
    result = db.session.execute(stmt).all()
    print(result)
    prequisite_profile_list = [{'prequisite_name':record[0],'waiver_request_details':record[1],'pre_unit':record[2],'attachment':record[3].decode('latin-1'),'student_id':record[4]} for record in result]
    print(prequisite_profile_list)
    return prequisite_profile_list


#====================
# Display Helppage
#====================


@app.route("/help")
def help_page():
   return render_template('help.html')



@app.route("/download_complaint_form")
def download_complaint_form():
    complaint_form_path = "/Users/prosper/my_sandbox/PracticeProject/static/CourseRegistration.pdf"  # Replace with the actual path to your PDF file
    return send_file(complaint_form_path, as_attachment=True)


#====================
# Logout
#====================

@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'success')

    # Clear the session cookie
    session.clear()

    return redirect(url_for('login'))


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        # manually run
        # flask db migrate -m "Initial migration."
        app.run(debug=True)
