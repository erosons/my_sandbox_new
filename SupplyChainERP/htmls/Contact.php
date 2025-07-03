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
            <div class="contact">
              <div class="contactrep">
                  <h3>Contact Us </h3>
                  <p>Tel: 1-877-567-YAPA <br>
                      Office Opens : Monday -Friday 8:00am CST - 5pm CST <br>
                      Email: contactUs@yapa.com <br>
                  </p>
                  <div id="googleMap" style="width:90%;height:500px;top:100px;"></div>
                    
                  <script>
                      function myMap() {
                      var mapProp= {
                        center:new google.maps.LatLng(51.508742,-0.120850),
                        zoom:5,
                      };
                      var map = new google.maps.Map(document.getElementById("googleMap"),mapProp);
                      }
                      </script>
                      
                  <script src="https://maps.googleapis.com/maps/api/js?key=;=myMap"></script>
                       
              
              </div>
            </div>
      </section>
      <nav class="dropList">
                  <ul>
                    <li><a title="Home" href="index.php" target="_self">Home</a></li>
                     <li><a title="Home Improvment" href="Furnitures.php" target="_self" aria-haspopup="true">Furniture</a>
                     <li> <a title="Appliance" href="Appliance.php" target="_self">Appliances</a></li>
                     <li> <a title="Gallery" href="lighting.php" target="_self">Lights</a></li>
                     <li><a title="Decor" href="decorandpillows.php" target="_self">Home Improvement</a></li>
                     <li><a title="About Us" href="About_Us.php" target="_self">About Us</a></li>
                     <li><a title="Contact Us" href="Contact.php" target="_self">Contact Us</a></li>
                     <li ><a title="Account" href="#" target="_self">Account</a>
                        <ul style="padding:5px 80px float:left;" >
                            <li><a title="Profile" href="profile.php" target="_self">Profile</a></li>
                            <li><a title="Login" href="login.php" target="_self"><button style="padding:5px 30px"; type="button">Login</button></a></li>
                        </ul>
                    </li>
                    <li style="float:right;padding:5px 30px">
                    <a title="Cart" href="ShoppingCart.php" target="_self">Cart<img alt="Cart" src="images/shopping-cart.png" width="25" height="17" ></a></li> 
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