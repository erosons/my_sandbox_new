<?php
   
   include "connection.php";
   include "functions.php";

   if ($_SERVER['REQUEST_METHOD']="post"){

      $user_name=$_POST["UserName"];
      $password=$_POST["password"];
      $email=$_POST["email"];
      $phoneNumber=$_POST["phoneNumber"];
      $Staff=' ';
      $Name=$_POST["Name"];

      if(!empty($user_name) && !empty($password) && !is_numeric($user_name)){

       // save user entry into the database
       $user_id = random_num_gen(20);
       $query = "insert into YapaDB.users(user_id,username,password,email,phoneNumber,Name) values ('$user_id','$user_name','$password','$email','$phoneNumber','$Name')";
       mysqli_query($conn,$query);

       //redirect user to relogin with their credentials
       header("location:login.php");
      }
      else

         echo " Please enter a correct UserName ";
      
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
    <link rel="stylesheet"type="text/css" media="screen" href="css/signup.css" >
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    </head>

  <body>
    <!-- id attribute can only be used once, while a class can be reused-->
    <div id="page">
      <!-- We use CSS to reposition  the nav in the header for large and Medium screen-->
   <section>
      <div id="id01" class="modal">
          <form class="modal-content" action="signup.php" method="POST">
              <div class="container">
                  <h1>Sign Up</h1>
                  <p>Please fill in this form to create an account.</p>
                  <hr>
                  <label for="UserName"><b>Name</b></label><br>
                  <input type="text" placeholder="Name" name="Name" required> <br>

                  <label for="UserName"><b>UserName</b></label><br>
                  <input type="text" placeholder="Enter UserName" name="UserName" required> <br>

                  <label for="email"><b>Email</b></label><br>
                  <input type="text" placeholder="Enter Email" name="email" required><br>

                  <label for="psw"><b>Password</b></label><br>
                  <input type="password" placeholder="Enter Password" name="password" required> <br>

                  <label for="psw-repeat"><b>Repeat Password</b></label> <br>
                  <input type="password" placeholder="Repeat Password" name="password-repeat" required> <br>

                  <label for="phoneNumber"><b>phoneNumber</b></label> <br>
                  <input type="text" placeholder="Enter phoneNumber" name="phoneNumber"><br>
                  
                  <hr>
                  <p>By creating an account you agree to our <a href="#" style="color:dodgerblue">Terms & Privacy</a>.</p>

                  <div class="clearfix">
                    <button type="submit" class="signupbtn" onclick="myFunction()">Sign Up</button>

                    <script>
                          function myFunction() {
                            alert("You have successfully signedUp!");
                          }
                    </script>

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