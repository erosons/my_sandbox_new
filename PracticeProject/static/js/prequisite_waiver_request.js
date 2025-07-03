$j(document).ready(function () {
    // Counter variable
    var clickCounter = 0;

    var prerequisiteButtons = document.querySelectorAll('.request-waiver-btn');

    prerequisiteButtons.forEach(function (button) {
        button.addEventListener('click', function (event) {
            // Increment the counter
            clickCounter++;

            // Remove the event listener to prevent further clicks
            button.removeEventListener('click', arguments.callee);

            // Prevent the default button click behavior
            event.preventDefault();

            // Get the table row
            var row = button.closest('tr');
            console.log('Row:', row);

            if (row) {
                // Access data from the table row
                var prerequisiteName = row.querySelector('td:first-child').innerText;
                console.log('Row:', prerequisiteName);
                var preUnit = row.querySelector('td:nth-child(2)').innerText;
                var prerequisiteStatus = row.querySelector('td:nth-child(3)').innerText;

                // Display the modal
                var modal = document.getElementById('waiverModal');
                modal.style.display = 'block';

                // Set the data in the form fields
                var prerequisiteNameInput = document.getElementById('prerequisiteName');
                prerequisiteNameInput.value = prerequisiteName;
                console.log('Value set for prerequisiteName:', prerequisiteNameInput.value);
    
                document.getElementById('preUnit').value = preUnit;
                document.getElementById('prerequisiteStatus').value = prerequisiteStatus;

            } else {
                console.error('Table row not found');
            }
        });
    });

    // Handle form submission
    var submitButton = document.getElementById('submitWaiverForm');
    submitButton.addEventListener('click', function () {
        // Get data from the form fields
        var reasonForWaiver = document.getElementById('reasonForWaiver').value;
        var attachment = new FormData();
        attachment.append('attachment', document.getElementById('attachment').files[0]);

        // Close the modal
        var modal = document.getElementById('waiverModal');
        modal.style.display = 'none';

        // Send data to the server using an AJAX request
        $j.ajax({
            url: "/preqiuiste_waiver_data",
            method: "POST",
            data: {
                prerequisiteName: document.getElementById('prerequisiteName').value,
                preUnit: document.getElementById('preUnit').value,
                prerequisiteStatus: document.getElementById('prerequisiteStatus').value,
                reasonForWaiver: reasonForWaiver,
                attachment: attachment
            },
            processData: false,
            contentType: false,
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

    // Log the click count
    console.log('Number of clicks:', clickCounter);
});
