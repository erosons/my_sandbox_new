// script1.js

// Global variable to store row data
var rowData = {};

$j(document).ready(function () {
    var prerequisiteButtons = document.querySelectorAll('.request-waiver-btn');

    prerequisiteButtons.forEach(function (button) {
        button.addEventListener('click', function (event) {
            // Prevent the default button click behavior
            event.preventDefault();

            // Get the table row
            var row = button.closest('tr');
            console.log('Row:', row);
            if (row) {
                console.log('passing row records:', row);
                // Access data from the table row
                rowData.prerequisiteName = row.querySelector('td:first-child').innerText;
                rowData.preUnit = row.querySelector('td:nth-child(2)').innerText;
                rowData.prerequisiteStatus = row.querySelector('td:nth-child(3)').innerText;

                // Call a function in script2.js to handle the next steps
                console.log("Call a function in script2.js to handle the next steps:");
                handleFormDisplay();
            } else {
                console.error('Table row not found');
            }
        });
    });
});
