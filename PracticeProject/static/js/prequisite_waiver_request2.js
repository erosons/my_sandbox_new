// script2.js
var $j = jQuery.noConflict();
$j(document).ready(function () {
    // Handle form display logic
    window.handleFormDisplay = function () {
        // Display the modal
        var modal = document.getElementById('waiverModal');
        modal.style.display = 'block';
         
        console.log("global variablescript2",rowData.prerequisiteName)
        // Set the data in the form fields
        // document.getElementById('prerequisiteName').value = 
        rowData.prerequisiteName;
        // document.getElementById('preUnit').value = 
        rowData.preUnit;
        //document.getElementById('prerequisiteStatus').value = 
        rowData.prerequisiteStatus;
    };
    
    var formData = new FormData();
    // Handle form submission
    var submitButton = document.getElementById('submitWaiverForm');
    submitButton.addEventListener('click', function () {
        // Get data from the form fields
        var reasonForWaiver = document.getElementById('reasonForWaiver').value;
        formData.append('attachment', document.getElementById('attachment').files[0]);
        //attachment.append('attachment', document.getElementById('attachment').files[0]);
        console.log('I am here', rowData.prerequisiteName);
        console.log('I am here', rowData.preUnit);
        console.log('I am here', rowData.prerequisiteStatus);
        // Close the modal
        formData.append('prerequisiteName', rowData.prerequisiteName);
        formData.append('preUnit', rowData.preUnit);
        formData.append('prerequisiteStatus', rowData.prerequisiteStatus);
        formData.append('reasonForWaiver', reasonForWaiver);
        formData.append('attachment', attachment);

        var modal = document.getElementById('waiverModal');
        modal.style.display = 'none';
        // Send data to the server using an AJAX request
        $j.ajax({
            url: "/preqiuiste_waiver_data",
            method: "POST",
            data: formData,
             processData: false,
             contentType: false,
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

    // Close the modal on cancel
    var cancelButton = document.getElementById('CloseWaiverForm');
    cancelButton.addEventListener('click', function () {
        console.log('Cancel button clicked');  // Add this line for debugging
        var modal = document.getElementById('waiverModal');
        modal.style.display = 'none';
    });
});
