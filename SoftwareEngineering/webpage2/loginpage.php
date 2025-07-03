<?php


include("connections.php");
include("functions.php");

  $user_data = validate_user_profile($conn);


  if ($_SERVER['REQUEST_METHOD']="post"){

        $first_name=$_POST["UserName"];
        $last_name=$_POST["password"];

        if (!empty($first_name) && !empty($last_name) && !is_numeric($first_name)) {
        // save user entry into the database
        $query="Select * from EIMS.customer where first_name='$first_name' and last_name='$last_name' and Staff is not null  limit 1";
        $result= mysqli_query($conn,$query);

        if($result && mysqli_num_rows($result)>0){

        //redirect  staff user to to admin page
            header("location: inventoryPage.php");
        }
        else{

            header("location: index.php");
        }
        }

     
    }

?>


<!DOCTYPE html>
<html lang="en">
  <head>
    <meta http-equiv="Content-Type" content="text/html;charset=UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>EIMS | IMS</title>
    <link rel="icon" href="images/yapa.png">
    <meta name="description"
        content="Inventory analysis and oversight">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KK94CHFLLe+nY2dmCWGMq91rCGa5gtU4mk92HdvYe+M/SXH301p5ILy+dN9+nJOZ" crossorigin="anonymous">
    <link rel="stylesheet"type="text/css" media="screen" href="css/login.css" >
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
  </head>

  <body>
    <!-- id attribute can only be used once, while a class can be reused-->
    <div id="page">
      <!-- We use CSS to reposition  the nav in the header for large and Medium screen-->

   <section>
      <div >
      <form class="modal-content" action="loginPage.php" method="post">
                <div class="container">
                  <h1>Sign in </h1>
                  <p>Enter your credential to sign in to your account.</p>
                  <hr>
                  <label for="UserName"><b>UserName</b></label>
                  <input type="text" placeholder="UserName" name="UserName" required><br><br>

                  <label for="psw"><b>Password</b></label>
                  <input type="password" placeholder="Enter Password" name="password" required>
                  
                  <p>By Login in you agree to our <a href="#" style="color:dodgerblue">Terms & Privacy</a>.</p>
 
                  <br>

                  <button type="submit" class="signupbtn" onclick="myFunction()">Login</button>

                    <script>
                          function myFunction() {
                            alert("You have successfully signedIn!");
                          }
                    </script>
                  </div>
                </div>
          </form>
      </div>

</section>

      <footer>
        &copy;EIMS (c)2023
        <div class="content">
          <a title="Privacy Policy" href="#">Privacy Policy</a>
          <a title="Terms of Services" href="#">Terms of Services</a>
        </div>
      </footer>
    </div>
  </body>
</html>
