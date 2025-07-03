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
    <link rel="stylesheet"type="text/css" media="screen" href="css/About.css" >
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    </head>

  <body>
    <!-- id attribute can only be used once, while a class can be reused-->
    <div id="page">
      <!-- We use CSS to reposition  the nav in the header for large and Medium screen-->
      <header>
        <a class="logo" ,title="Gopherwood Consulting" href="index.php"><span>Gopherwood Consulting</span></a>
      </header>

            <div class="aboutmember">
               <img src="images/abtUs.png " width=1600px height=600px>
                <h4><strong>About Us</strong> </h4>
                <h5><strong> Company Overview </strong> </h5>
                  <p><strong> COMPANY NEWS,  SUSTAINABILITY </strong><br><br>
                   Yapa Makes it Easy to Shop Sustainably with Largest Selection <br> 
                    of Sustainability Certifications for Home
                    Leader in Home showcases more than 50 third-party certifications <br>
                    to help customers shop sustainably<br><br>
                  </p>


                  <p><strong>GA Global Brand</strong><br><br>
                  With global headquarters and an extensive network of logistics hubs <br>
                   and customer service centers, we’re here to create that feeling of <br>
                  home for everyone, anywhere.<br><br>

                  <strong>Corporate Offices</strong><br>
                  Our corporate headquarters in Boston and Berlin are surrounded by <br> 
                  world-class technology and educational institutions, providing access <br>
                  to top talent.<br><br>

                  <strong>Fulfillment & Home Delivery Network</strong><br>
                  We operate 18 fulfillment and 38 delivery centers representing millions <br>
                  of square feet across the U.S., Germany, Canada, and the U.K.<br><br>

                  <strong> Sales & Service Centers</strong><br><br>
                  Our Sales & Service teams in the U.S., Germany, Ireland, Canada, <br>
                   and the U.K. along with our virtual team allow us to meet the needs of our global
                  </p>

            </div>

      <!-- We use CSS to reposition  the nav in the header for large and Medium screen-->
      <nav class="dropList">
                  <ul>
                    <li><a title="Home" href="index.php" target="_self">Home</a></li>
                     <li><a title="Home Improvment" href="Furnitures.php" target="_self" aria-haspopup="true">Furniture</a>
                     <li> <a title="Appliance" href="Appliance.php" target="_self">Appliances</a></li>
                     <li> <a title="Gallery" href="lighting.php" target="_self">Lights</a></li>
                     <li><a title="Decor" href="decorandpillows.php" target="_self">Home Improvement</a></li>
                     <li><a title="About Us" href="About_Us.php" target="_self">About Us</a></li>
                     <li><a title="Contact Us" href="Contact.php" target="_self">Contact Us</a></li>
                     <li style="float:right;padding:5px 80px"><a title="Account" href="#" target="_self">Account</a>
                        <ul style="padding:5px 80px float:left;" >
                            <li><a title="Orders" href="shoppingCart.php" target="_self" >Orders</a></li>
                            <li><a title="Profile" href="profile.php" target="_self">Profile</a></li>
                            <li><a title="Login" href="login.php" target="_self"><button style="padding:5px 30px"; type="button">Login</button></a></li>
                        </ul>
                    </li>
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
<>
