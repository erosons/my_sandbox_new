
        var $j = jQuery.noConflict();
        $j(document).ready(function () {
            // When the "Category" dropdown changes
            $j("#category").on("change", function () {
                var selectedCategory = $(this).val();
                if (selectedCategory) {
                    // Make an AJAX request to get subcategories
                    $j.ajax({
                        url: "/get_subcategories",
                        method: "POST",
                        data: { category: selectedCategory },
                        success: function (data) {
                            // Populate the "Subcategory" dropdown with received data
                            // data =JSON.parse(data);
                            console.log(data)
                            var subcategoryDropdown = $("#subcategory");
                            subcategoryDropdown.empty();
                            subcategoryDropdown.append('<option value="">Select a Subcategory</option>');
                            // for (var i = 0; i < data.length; i++)
                            data.forEach((obj) => {
                                 subcategoryDropdown.append('<option value="' + obj.name + '">' + obj.name + '</option>');
                                // subcategoryDropdown.append('<option value="' + data[i][0] + '">' + data[i][1] + '</option>');
                            });
                        },
                        error: function (error) {
                            console.log("Error:", error);
                        }     
                    });
                }
            });
        });
