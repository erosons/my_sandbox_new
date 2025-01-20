<?php
session_start();
   
   include "connection.php";
   include "functions.php";

   if ($_SERVER['REQUEST_METHOD']="post"){

      $user_name=$_POST["username"];
      $password=$_POST["Password"];
      $email=$_POST["Email"];
      $phoneNumber=$_POST["PhoneNumber"];
      $Staff=$_POST["StaffID"];
      $Name=$_POST["Name"];

      if(!empty($user_name) && !empty($password) && !is_numeric($user_name)){

       // save user entry into the database
       $user_id = random_num_gen(20);
       $query = "insert into YapaDB.users(user_id,username,password,email,phoneNumber,Name) values ('$user_id','$user_name','$password','$email','$phoneNumber','$Name')";
       mysqli_query($conn,$query);

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
    <link rel="stylesheet"type="text/css" media="screen" href="css/contact.css" >
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    </head>

  <body>
    <!-- id attribute can only be used once, while a class can be reused-->
    <div id="page">
      <!-- We use CSS to reposition  the nav in the header for large and Medium screen-->
      <header>
        <a class="logo" ,title="Gopherwood Consulting" href="index.php"><span>Gopherwood Consulting</span></a>
      </header>
          <section>
               <form class="modal-content" action="userprofile-mgt.php" method="post">
                    <div class="container">
                        <h1>Sign in </h1>
                        <p>Welcome to Users Profile Page <?php echo "$userID"; ?> </p>
                        <hr>

                        <label for="Name"><b>Name</b></label>
                        <input type="text" placeholder="Name" name="Name" required><br><br>

                        <label for="password"><b>Password</b></label>
                        <input type="text" placeholder="Password" name="Password" required><br><br>

                        <label for="PhoneNumber"><b>PhoneNumber</b></label>
                        <input type="text" placeholder="PhoneNumber" name="PhoneNumber" required><br><br>

                        <label for="Username"><b>Username</b></label>
                        <input type="text" placeholder="Username" name="username" required><br><br>

                        <label for="email"><b>Email</b></label>
                        <input type="text" placeholder="Email" name="Email" required><br><br>

                        <label for="Staff"><b>StaffID</b></label>
                        <input type="text" placeholder="StaffID" name="StaffID" ><br><br>

                        <button type="submit" class="signupbtn">Insert</button>
                        <button type="submit" class="signupbtn">Delete</button>
                        <button type="submit" class="signupbtn">Update</button>
                        <button type="submit" class="signupbtn">Generate Inventory Report</button>

                   </div>
                </form>
           </section>
      <nav class="dropList">
                  <ul>
                    <li><a title="Home" href="logout.php" target="_self">Home</a></li>
                     <li><a title="Home Inventory Management" href="InventoryMgt.php" target="_self" aria-haspopup="true">StockManagement</a>
                     <li><a title="AdminHome" href="adminHome.php" target="_self" aria-haspopup="true">Admin Home</a>
                  </ul> 
        </nav>
           <nav class="Search">
                <div class="search-container">
                    <form action="/page.php">
                    <input type="text" placeholder="Search.." name="search">
                    <button type="submit"><i class="fa fa-search"></i></button>
                </form>
                </div>
           </nav>
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