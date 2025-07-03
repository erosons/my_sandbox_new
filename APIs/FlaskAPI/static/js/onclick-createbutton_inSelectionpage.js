
 var $j = jQuery.noConflict();
   $j(document).ready(function () {
   // Reference the loading overlay
   var loadingOverlay = $j("#loading-overlay");
    // ...
   $j("#create-profile-button").on("click", function () {
       var selectedCategory = $j("#category").val();
       var selectedSubcategory = $j("#subcategory").val();

       // Show the loading overlay before making the AJAX request
       loadingOverlay.show();

           $j.ajax({
               url: "/get_graph_data",
               method: "POST",
               data: { category: selectedCategory, subcategory: selectedSubcategory },
               success: function () {
                  // Reference the loading overlay
                  var loadingOverlay = $j("#loading-overlay");
                   // Redirect to the new graph page
                   window.location.href = "/generate_profile";
               },
               error: function (error) {
                   console.log("Error:", error);
               },
               complete: function () {
               // Hide the loading overlay when the request is complete
               loadingOverlay.hide();
           }
           });
       });
   });
