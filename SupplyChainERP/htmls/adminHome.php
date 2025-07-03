<?php
session_start();

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
                    <div class="container-admin">
                        <h1>Sign in </h1>
                        <p>Welcome to Admin Page <?php echo "$userID"; ?> </p>

                        <button type="submit" class="signupbtn"><a href="InventoryMgt.php">InventoryManagment</a></button>
                        <button type="submit" class="signupbtn"><a href="InventoryMgt.php">Userprofile Management</a></button>

                   </div>
                </form>
           </section>

           <nav class="dropList">
                  <ul>
                    <li><a title="Home" href="logout.php" target="_self">Home</a></li>
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