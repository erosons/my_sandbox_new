<!-- This Line of code Add product to your Cart--->
<?php

session_start();
include "connection.php";
include "functions.php";

$status="";
if (isset($_POST['code']) && $_POST['code']!=""){
$code = $_POST['code'];

$query="Select * from YapaDB.Product where ProductID='$code' ";
$result= mysqli_query($conn,$query);
$row = mysqli_fetch_assoc($result);
$name = $row['Name'];
$code = $row['ProductID'];
$price = $row['Price'];


$cartArray = array(
	$code=>array(
	'name'=>$name,
	'code'=>$code,
	'price'=>$price,
	'quantity'=>1
    )
);

if(empty($_SESSION["shopping_cart"])) {
    $_SESSION["shopping_cart"] = $cartArray;
    $status = "<div class='box'>Product is added to your cart!</div>";
}
else{
    $array_keys = array_keys($_SESSION["shopping_cart"]);
    if(in_array($code,$array_keys)) {
	$status = "<div class='box' style='color:red;'> Product is already added to your cart!</div>";	
     } 
else {
    $_SESSION["shopping_cart"] = array_merge($_SESSION["shopping_cart"],$cartArray);
     $status = "<div class='box'>Product is added to your cart!</div>";
	}

	}
}
?>

<?php
if(!empty($_SESSION["shopping_cart"])) {
$cart_count = count(array_keys($_SESSION["shopping_cart"]));
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
    <link rel="stylesheet"type="text/css" media="screen" href="css/main.css" >
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    </head>

<body>

        <div class="cart_div">
        <a href="cart.php"><img src="cart-icon.png" /> Cart<span>
        <?php echo $cart_count; ?></span></a>
        </div>
        <?php
        }
        ?>

        <!-- This Line of code this product from the database--->
        <?php
        $query2="Select * from YapaDB.Product";
        $result = mysqli_query($con,$query2);
        while($row = mysqli_fetch_assoc($result)){
            echo "<div class='product_wrapper'>
            <form method='post' action=''>
            <input type='hidden' name='code' value=".$row['ProductID']." />
            <div class='image'><img src='".$row['image']."' /></div>
            <div class='name'>".$row['Name']."</div>
            <div class='price'>$".$row['Price']."</div>
            <button type='submit' class='buy'>Buy Now</button>
            </form>
            </div>";
                }
        mysqli_close($conn);
        ?>

        <div style="clear:both;"></div>

        <div class="message_box" style="margin:10px 0px;">
        <?php echo $status; ?>
        </div>

            <footer>
                &copy;Yapa Global E-Shopping 2022
                <div class="content">
                    <a title="Privacy Policy" href="#">Privacy Policy</a>
                    <a title="Terms of Services" href="#">Terms of Services</a>
                        </div>
                    </footer>
</body>
</html>
