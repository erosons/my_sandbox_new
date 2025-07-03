
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
    <link rel="stylesheet"type="text/css" media="screen" href="css/main.css" >
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    </head>

<body>
         <!-- id attribute can only be used once, while a class can be reused-->
        <div id="page">
             <!-- We use CSS to reposition  the nav in the header for large and Medium screen-->
            <header>
             <a class="logo",title="Gopherwood Consulting" href="index.php"><span>Gopherwood Consulting</span></a>
            </header>
            <section>
               
                <div class="w3-content w3-section" style="max-width:500px">
                    <img class="mySlides" src="images/f1.png" width="1700px" height="600px">
                    <img class="mySlides" src="images/f2.png" width="1700px" height="600px">
                    <img class="mySlides" src="images/f3.png" width="1700px" height="600px">
                    <img class="mySlides" src="images/f4.png" width="1700px" height="600px">
                    <img class="mySlides" src="images/f5.png" width="1700px" height="600px">
                    <img class="mySlides" src="images/f6.png" width="1700px" height="600px">
                    <img class="mySlides" src="images/f7.png" width="1700px" height="600px">
                    <img class="mySlides" src="images/f8.png" width="1700px" height="600px">
                </div>
                
                <script>
                var myIndex = 0;
                carousel();
                
                function carousel() {
                    var i;
                    var x = document.getElementsByClassName("mySlides");
                    for (i = 0; i < x.length; i++) {
                    x[i].style.display = "none";  
                    }
                    myIndex++;
                    if (myIndex > x.length) {myIndex = 1}    
                    x[myIndex-1].style.display = "block";  
                    setTimeout(carousel, 3500); // Change image every 3 seconds
                }
                </script>
           <!-- Promo Section -->
            </section>
            <section class="main1">
                <aside>
                    <div class="content promo1">

                    </div>
                </aside>
                <aside>
                    <div class="content promo2">
                        
                    </div>
                </aside>
                <aside>
                    <div class="content promo3">

                </aside>
            </section>
            
            <section class="Text">
             <div> <h3><span>Shop by Department </span></h3></div>
             </section>

             <!-- We want to uniquely identify each section of the webpage with a stylesheet using Class
                  Though we can also use a id as well.-->
            <section class="main">
                <aside>
                    <div class="content open-source">
                        <h3><a title="Open Source Technology" href="Furnitures.php">Furniture</h3>
                    </div>
                </aside>
                <aside>
                    <div class="content cloud">
                        <h3><a title="Cloud Computing Infrastructure" href="Appliance.php" target="_self">Appliances</a></h3>
                        
                    </div>
                </aside>
                <aside>
                    <div class="content Analytics">
                        <h3><a title="BI and Analytics" href="Appliance.php">Electronics</a></h3>

                </aside>
                <aside>
                    <div class="content Lighting">
                        <h3><a title="BI and Analytics" href="lighting.php">Lightings</a></h3>

                </aside>
                <aside>
                    <div class="content Pillow">
                        <h3><a title="BI and Analytics" href="decorandpillows.php">Home Improvement</a></h3>

                </aside>
            </section>
            <section class="atmosphere">
                <article>
                    <div class="atm">
                    <h2>High Quality and Affordable prices</h2>
                    <p> Our brand stands for delivery high quality products with great value <br> We also strive to ensure our prices are not out range for our customers.<br>
                        Your trust is important to, and we do compromise and quality and prices.           
                    </p>
                   <a class="btn" title="Learn more about infrastructure approach" href="https://aws.amazon.com/solutions/?nc2=h_ql_sol">Shop more</a>
    
                 </div>
                </article>
            </section>
            <section class="membership">
                <aside>
                    <div class="content">
                        <h2>Membership On Us</h2>
                        <p> Our members join unlimited discounts and promotion throughout the year <br>
                            We provide upto date clearance Sales to inform members of new products arrival
                            Our members join free added services like home delivery, discount across multiples businss lines.</p>
                        <a class="btn" title="Cloud infrastructure with AWS" href="signup.php" target="_self">Sign Up</a>
                    </div>
                </aside>
            </section>

            <section class="Text">
                <div> <h3><span>Living Room Finds in Every Style </span></h3></div>
                </section>
            <!-- Living Style On Us Section -->
            <section class="main2">
                <aside>
                    <div class="content living1">
                        <h3><a title="Cloud Computing Infrastructure" href="https://www.businessnewsdaily.com/4427-cloud-computing-small-business.php" target="_self">Shop a Table</a></h3>
                        
                    </div>
                </aside>
                <aside>
                    <div class="content living2">
                        <h3><a title="Cloud Computing Infrastructure" href="https://www.businessnewsdaily.com/4427-cloud-computing-small-business.php" target="_self">Shop Living Room Sets</a></h3>
                        
                    </div>
                </aside>
                <aside>
                    <div class="content living3">
                        <h3><a title="Cloud Computing Infrastructure" href="https://www.businessnewsdaily.com/4427-cloud-computing-small-business.php" target="_self">Shop Accent Chairs</a></h3>
                        
                </aside>
                <aside>
                    <div class="content living4">
                        <h3><a title="Cloud Computing Infrastructure" href="https://www.businessnewsdaily.com/4427-cloud-computing-small-business.php" target="_self">Shop a Rug</a></h3>
                </aside>
            </section>      

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
                            <li><a title="Login" href="index.php" target="_self"><button style="padding:5px 30px"; type="button">Logout</button></a></li>
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
</html>

