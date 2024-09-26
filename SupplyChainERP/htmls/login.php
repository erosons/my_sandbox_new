<?php


  include("connection.php");
  include("functions.php");

  $user_data = validate_user_profile($conn);

  if ($_SERVER['REQUEST_METHOD']="post"){

     $user_name=$_POST["UserName"];
     $password=$_POST["password"];
     $staffID=$_POST["staffID"];

     if(!empty($user_name) && !empty($password) && !is_numeric($user_name) && empty($staffID)){

      // save user entry into the database
        $query="Select * from YapaDB.users where username='$user_name' and password='$password' and Staff is null  limit 1";
        $result= mysqli_query($conn,$query);

        if($result && mysqli_num_rows($result)>0){

      //redirect user to relogin with their credentials
        header("location: logout.php");
     }
    }
    elseif (!empty($user_name) && !empty($password) && !is_numeric($user_name) && !empty($staffID)) {
      // save user entry into the database
      $query="Select * from YapaDB.users where username='$user_name' and password='$password' and Staff is not null  limit 1";
      $result= mysqli_query($conn,$query);

      if($result && mysqli_num_rows($result)>0){

       //redirect  staff user to to admin page
        header("location: adminHome.php");
      }
      else{

        header("location: login.php");
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
    <title>Yapa | ShoppingVerse</title>
    <link rel="icon" href="images/yapa.png">
    <meta name="description"
        content="ShoppingVerse brings shopping to your doorstep">
    <link rel="stylesheet"type="text/css" media="screen" href="css/login.css" >
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
  </head>

  <body>
    <!-- id attribute can only be used once, while a class can be reused-->
    <div id="page">
      <!-- We use CSS to reposition  the nav in the header for large and Medium screen-->

   <section>
      <div id="id01" class="modal">
          <form class="modal-content" action="login.php" method="post">
                <div class="container">
                  <h1>Sign in </h1>
                  <p>Enter your credential to sign in to your account.</p>
                  <hr>
                  <label for="UserName"><b>UserName</b></label>
                  <input type="text" placeholder="UserName" name="UserName" required><br><br>

                  <label for="psw"><b>Password</b></label>
                  <input type="password" placeholder="Enter Password" name="password" required>


                  
                  <label>
                    <input type="checkbox" checked="checked" name="staffID" style="margin-bottom:15px"> Checkbox for Staff Only
                  </label>
                  
                  <p>By creating an account you agree to our <a href="#" style="color:dodgerblue">Terms & Privacy</a>.</p>

                    <button type="submit" class="signupbtn" onclick="myFunction()">Login</button>

                    <script>
                          function myFunction() {
                            alert("You have successfully signedIn!");
                          }
                    </script>
                    <div class="register"><h3><a href="signup.php"> SignUp an Account </a></h3></div>
                  </div>
                </div>
          </form>
      </div>

</section>

      <footer>
        &copy;Yapa Global E-Shopping 2022
        <div class="content">
          <a title="Privacy Policy" href="#">Privacy Policy</a>
          <a title="Terms of Services" href="#">Terms of Services</a>
        </div>
      </footer>
    </div>
  </body>
</html>
