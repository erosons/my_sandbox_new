<?php
session_start();

?>


<!DOCTYPE html>
<html lang="en">
  <head>
    <meta http-equiv="Content-Type" content="text;charset=UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Yapa | ShoppingVerse</title>
    <link rel="icon" href="images/yapa.png" />
    <meta
      name="description"
      content="ShoppingVerse brings shopping to your doorstep"
    />
    <link
      rel="stylesheet"
      type="text/css"
      media="screen"
      href="css/shopping.css"
    />
    <link
      rel="stylesheet"
      href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"
    />
  </head>

  <body>
    <!-- id attribute can only be used once, while a class can be reused-->
    <div id="page">
      <!-- We use CSS to reposition  the nav in the header for large and Medium screen-->
      <header>
        <a class="logo" ,title="Gopherwood Consulting" href="index.php"
          ><span>Gopherwood Consulting</span></a
        >
      </header>
      <section>
        <div class="w3-content w3-section"></div>
        <section>
          <div class="container">
            <h1>Shopping Cart</h1>
            <div class="cart">
              <div class="products">
                <div class="product">
                  <img src="../images/lighting/30674447.jpg.jpeg" />
                  <div class="product-info">
                    <h3 class="product-name">Heart light</h3>
                    <h4 class="product-price">Price: $200.00</h4>
                    <h4 class="product-offer">Discount:25%</h4>
                    <p class="product-quantity">
                      Qty:<input value="1" name="" />
                    </p>
                    <p class="product-quantity-stock">Qty in Stock :100</p>
                    <p class="product-remove">
                      <i class="fa fa-trash"></i>
                      <span class="remove">Add to Cart</span>
                    </p>
                  </div>
                </div>
              </div>
            </div>

            <!--Item 2-->
            <div class="cart">
              <div class="products">
                <div class="product">
                  <img src="../images/lighting/light.jpeg" />
                  <div class="product-info">
                    <h3 class="product-name">Hat light</h3>
                    <h4 class="product-price">Price: $220.00</h4>
                    <h4 class="product-offer">Discount:25%</h4>
                    <p class="product-quantity">
                      Qty:<input value="1" name="" />
                    </p>
                    <p class="product-quantity-stock">Qty in Stock :100</p>
                    <p class="product-remove">
                      <i class="fa fa-trash"></i>
                      <span class="remove">Add to Cart</span>
                    </p>
                  </div>
                </div>
              </div>
            </div>
            <!--Item 3-->
            <div class="cart">
              <div class="products">
                <div class="product">
                  <img
                    src="../images/lighting/Screenshot 2022-10-22 at 10.24.35 PM.jpeg"
                  />
                  <div class="product-info">
                    <h3 class="product-name">Trio Bell light</h3>
                    <h4 class="product-price">Price: $250.00</h4>
                    <h4 class="product-offer">Discount:25%</h4>
                    <p class="product-quantity">
                      Qty:<input value="1" name="" />
                    </p>
                    <p class="product-quantity-stock">Qty in Stock :100</p>
                    <p class="product-remove">
                      <i class="fa fa-trash"></i>
                      <span class="remove">Add to Cart</span>
                    </p>
                  </div>
                </div>
              </div>
            </div>
            <!--Item 4-->
            <div class="cart">
              <div class="products">
                <div class="product">
                  <img
                    src="../images/lighting/Screenshot 2022-10-22 at 10.40.35 PM.jpeg" />
                  <div class="product-info">
                    <h3 class="product-name">Spiral light</h3>
                    <h4 class="product-price">Price: $200.00</h4>
                    <h4 class="product-offer">Discount:25%</h4>
                    <p class="product-quantity">
                      Qty:<input value="1" name="" />
                    </p>
                    <p class="product-quantity-stock">Qty in Stock :100</p>
                    <p class="product-remove">
                      <i class="fa fa-trash"></i>
                      <span class="remove">Add to Cart</span>
                    </p>
                  </div>
                </div>
              </div>
            </div>
            <!--Item 5-->
            <div class="cart">
              <div class="products">
                <div class="product">
                  <img src="../images/lighting/shopping copy 2.jpeg" />
                  <div class="product-info">
                    <h3 class="product-name">The Billy light</h3>
                    <h4 class="product-price">Price: $220.00</h4>
                    <h4 class="product-offer">Discount:25%</h4>
                    <p class="product-quantity">
                      Qty:<input value="1" name="" />
                    </p>
                    <p class="product-quantity-stock">Qty in Stock :100</p>
                    <p class="product-remove">
                      <i class="fa fa-trash"></i>
                      <span class="remove">Add to Cart</span>
                    </p>
                  </div>
                </div>
              </div>
            </div>
            <!--Item 6-->
            <div class="cart">
              <div class="products">
                <div class="product">
                  <img src="../images/lighting/shopping copy 3.jpeg" />
                  <div class="product-info">
                    <h3 class="product-name">Twin Light</h3>
                    <h4 class="product-price">Price: $150.00</h4>
                    <h4 class="product-offer">Discount:25%</h4>
                    <p class="product-quantity">
                      Qty:<input value="1" name="" />
                    </p>
                    <p class="product-quantity-stock">Qty in Stock :100</p>
                    <p class="product-remove">
                      <i class="fa fa-trash"></i>
                      <span class="remove">Add to Cart</span>
                    </p>
                  </div>
                </div>
              </div>
            </div>
            <!--Item 7-->
            <div class="cart">
              <div class="products">
                <div class="product">
                  <img src="../images/lighting/shopping-3.jpeg" />
                  <div class="product-info">
                    <h3 class="product-name">Rope torch light</h3>
                    <h4 class="product-price">Price: $210.00</h4>
                    <h4 class="product-offer">Discount:25%</h4>
                    <p class="product-quantity">
                      Qty:<input value="1" name="" />
                    </p>
                    <p class="product-quantity-stock">Qty in Stock :100</p>
                    <p class="product-remove">
                      <i class="fa fa-trash"></i>
                      <span class="remove">Add to Cart</span>
                    </p>
                  </div>
                </div>
              </div>
            </div>
            <!--Item 8-->
            <div class="cart">
              <div class="products">
                <div class="product">
                  <img src="../images/lighting/shopping-8.jpeg" />
                  <div class="product-info">
                    <h3 class="product-name">Round X light</h3>
                    <h4 class="product-price">Price: $150.00</h4>
                    <h4 class="product-offer">Discount:25%</h4>
                    <p class="product-quantity">
                      Qty:<input value="1" name="" />
                    </p>
                    <p class="product-quantity-stock">Qty in Stock :100</p>
                    <p class="product-remove">
                      <i class="fa fa-trash"></i>
                      <span class="remove">Add to Cart</span>
                    </p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>
        <!-- Promo Section -->
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
<>
