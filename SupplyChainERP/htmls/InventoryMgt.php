<?php
  session_start();

   include "connection.php";
   include "functions.php";

   if ($_SERVER['REQUEST_METHOD']="post"){

      $ProductID=$_POST["ProductID"];
      $Name=$_POST["ProductName"];
      $Price=$_POST["Price"];
      $SKUID=$_POST["ProductSKU"];
      $user_id=$_POST["user_id"];

      if(!empty($user_name) && !empty($password) && !is_numeric($user_name)){

       // save user entry into the database
       $query = "insert into YapaDB.Product(ProductID,Name,Price,SKUID,user_id) values ('$ProductID','$Name','$Price','$SKUID','$user_id')";
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
               <form class="modal-content" action="InventoryMgt.php" method="post">
                    <div class="container">
                        <h1>Sign in </h1>
                        <p>Welcome to Inventory Management Page <?php echo "$userID"; ?> </p>
                        <hr>
                        <label for="SKU"><b>SKU</b></label>
                        <input type="text" placeholder="SKU" name="ProductSKU" required><br><br>

                        <label for="ProductName"><b>ProductName</b></label>
                        <input type="text" placeholder="ProductName" name="ProductName" required><br><br>

                        <label for="ProductID"><b>ProductID</b></label>
                        <input type="text" placeholder="ProductID" name="ProductID" required><br><br>

                        <label for="ProductPrice"><b>ProductPrice</b></label>
                        <input type="text" placeholder="ProductPrice" name="Price" required><br><br>

                        <label for="userID"><b>UserID</b></label>
                        <input type="text" placeholder="user_id" name="user_id" required><br><br>

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
                     <li><a title="AdminHome" href="adminHome.php" target="_self" aria-haspopup="true">Admin Home</a>
                     <li> <a title="User" href="userprofile-mgt.php" target="_self">User Profile Mgt</a></li>
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