def _profileCourseSelection() -> jsonify:
    selected_subcategory= str(session.get('selected_subcategory'))
    stmt = (
    select(
        Course.name.label("name"),
        CareerPaths.name.label("career_path_name"),
        CareerPaths.program_id.label("program_ID"),
        #Course.unit.label("Unit"),
        Semester.id.label("semester_id"),
        literal_column("''").label("Grade")  # Use literal_column for an empty string
    )
    .distinct()
    .select_from(Student)
    .join(Program, Student.program_ID == Program.name)
    .join(CareerPaths, Program.id == CareerPaths.program_id)
    .join(Course, CareerPaths.id == Course.career_path_id)
    .join(Semester, Course.semesta_id == Semester.id)
   ).where(CareerPaths.name == str(selected_subcategory))
    
    print(stmt)
    result = db.session.execute(stmt).all()
    print(result)
    # Serialize the query result to get only the "name" field
    course_profile_list = [{'coursename': record[0],'career_path_name':record[1],'program_ID':record[2],'semester_id':record[3],'Grade': record[4]} for record in result]
    print(course_profile_list)
    return course_profile_list