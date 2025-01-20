var $j = jQuery.noConflict();
$j(document).ready(function () {
    var updateButtons = document.querySelectorAll('.update-btn');

    updateButtons.forEach(function (button) {
        button.addEventListener('click', function () {
            // Get the selected grade
            var selectedGrade = document.getElementById(button.dataset.gradeId).value;

            // Get the course checkbox
            var courseCheckbox = document.getElementById(button.dataset.courseId);
            
            // Check if the course is checked
            var isCourseChecked = courseCheckbox.checked;
            
            // Get the course ID
            var courseSelected = isCourseChecked ? courseCheckbox.value : null;

            // Send the data to the server using an AJAX request
            $j.ajax({
                url: "/get_course_grade_data",
                method: "POST",
                data: {
                    selected_course: courseSelected,
                    selected_Grade: selectedGrade
                },
                beforeSend: function(xhr, settings) {
                    // Log or inspect the data before sending
                    console.log('Inspecting data before sending:', settings.data);
                },
                success: function (data) {
                    // Handle the response from the server if needed
                    console.log(data);
                },
                error: function (error) {
                    console.log("Error:", error);
                }
            });
        });
    });
});
