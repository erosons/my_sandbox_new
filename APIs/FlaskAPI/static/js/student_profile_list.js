// JavaScript to handle navigation click actions
const contentContainer = document.getElementById("content-container");
const courseAdvisorLink = document.getElementById("course-advisor-link");
const link1 = document.getElementById("link1");
const link2 = document.getElementById("link2");
const link3 = document.getElementById("link3");
const link4 = document.getElementById("link4");
const link5 = document.getElementById("link5");
const link6 = document.getElementById("link6");

courseAdvisorLink.addEventListener("click", (event) => {
    // Prevent the default behavior of the link (preventing navigation)
    event.preventDefault();
    // Optionally, you can add an active class to highlight the selected link
    // Remove the active class from all links
    document.querySelectorAll(".nav-link").forEach((link) => {
        link.classList.remove("active");
    });
    // Add an active class to the clicked link
    courseAdvisorLink.classList.add("active");
});

link1.addEventListener("click", () => {
    console.log("Link 1 clicked");
    // Load content for Link 1 by calling the function
    const StudentListData = JSON.parse(jinja_data.dataset.studentlist);
    console.log("Student List Data:", StudentListData);

    // Check if  StudentListData is an object before proceeding
    if (typeof StudentListData === 'object' && StudentListData !== null) {
        const tableHTML = createStudentProfileListTable(StudentListData).outerHTML;
        console.log(tableHTML)
        contentContainer.innerHTML = tableHTML;
    } else {
        console.error("Invalid student list data:", StudentListData);
        // Handle the error accordingly, for example, display a message or create an empty table
    }
});

// Add event listeners for other links...

// Function to create the table for Student Profile List
function createStudentProfileListTable(StudentListData) {
    // You can customize this table as needed
    const table = document.createElement("table");
    table.className = "table table-dark";
    const thead = document.createElement("thead");
    const tbody = document.createElement("tbody");

    // Create table headers
    const headers = ["Student_ID", "Name", "Major"];
    const headerRow = document.createElement("tr");
    headers.forEach((headerText) => {
        const th = document.createElement("th");
        th.textContent = headerText;
        headerRow.appendChild(th);
    });
    thead.appendChild(headerRow);
    table.appendChild(thead);

    // Create table rows with data
    StudentListData.forEach((student) => {
        const row = document.createElement("tr");
        headers.forEach((header) => {
            const cell = document.createElement("td");
            cell.textContent = student[header]; // Assuming keys in the object are lowercase versions of headers
            row.appendChild(cell);
        });
        // Add "View" button
        const approveCell = document.createElement("td");
        const approveButton = document.createElement("button");
        approveButton.textContent = "View";
        approveButton.addEventListener("click", () => {
            // Handle the approve action
            // Prepare the data to send
            const postData = {
                student_id: student["student_id"],
                // Add other data properties as needed
            };

            // Make a POST request to the Flask backend
            fetch("/generate_profile", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(postData),
            })
                .then(response => response.json())
                .then(data => {
                    // Handle the response from the server if needed
                    console.log("Server response:", data);
                })
                .catch(error => {
                    // Handle errors
                    console.error("Error:", error);
                });
        });
        approveCell.appendChild(approveButton);
        row.appendChild(approveCell);


        tbody.appendChild(row);
    });
    table.appendChild(tbody);

    return table;
}



link2.addEventListener("click", () => {
    console.log("Link 1 clicked");
    // Load content for Link 1 by calling the function
    const prerequisitetListData = JSON.parse(jinja_prerequisite.dataset.prerequistelist);
    console.log("Prerequisite List Data:", prerequisitetListData);

    // Check if prerequisitetListData is an object before proceeding
    if (typeof prerequisitetListData === 'object' && prerequisitetListData !== null) {
        const tableHTML = createStudentPrerequiste_waiverTable(prerequisitetListData).outerHTML;
        console.log(tableHTML);
        contentContainer.innerHTML = tableHTML;
    } else {
        console.error("Invalid Prerequisite list data:", prerequisitetListData);
        // Handle the error accordingly, for example, display a message or create an empty table
    }
});

// Function to create the table for Student Profile List
function createStudentPrerequiste_waiverTable(prerequisitetListData) {
    // You can customize this table as needed
    const table = document.createElement("table");
    table.className = "table table-dark";
    const thead = document.createElement("thead");
    const tbody = document.createElement("tbody");

    // Create table headers
    const headers = ["prequisite_name", "waiver_request_details", "pre_unit", "attachment", "student_id"];
    const headerRow = document.createElement("tr");
    headers.forEach((headerText) => {
        const th = document.createElement("th");
        th.textContent = headerText;
        headerRow.appendChild(th);
    });
    thead.appendChild(headerRow);
    table.appendChild(thead);

    // Create table rows with data, including an "Approve" button in each row
    prerequisitetListData.forEach((student) => {
        const row = document.createElement("tr");

        // Loop through headers to create cells for each column
        headers.forEach((header) => {
            const cell = document.createElement("td");
            cell.textContent = student[header]; // Assuming keys in the object are lowercase versions of headers
            row.appendChild(cell);
        });

        // Add "Approve" button
        const approveCell = document.createElement("td");
        const approveButton = document.createElement("button");
        approveButton.textContent = "Approve";
        approveButton.addEventListener("click", () => {
            // Handle the approve action
            console.log("Approve button clicked for student ID:", student["student_id"]);
        });
        approveCell.appendChild(approveButton);
        row.appendChild(approveCell);

        // Append the row to the table body
        tbody.appendChild(row);
    });

    table.appendChild(tbody);

    return table;
}
