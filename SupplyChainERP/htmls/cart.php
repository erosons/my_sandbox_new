<?php
session_start();
$status="";
if (isset($_POST['action']) && $_POST['action']=="remove"){
if(!empty($_SESSION["shopping_cart"])) {
    foreach($_SESSION["shopping_cart"] as $key => $value) {
      if($_POST["ProductID"] == $key){
      unset($_SESSION["shopping_cart"][$key]);
      $status = "<div class='box' style='color:red;'>
      Product is removed from your cart!</div>";
      }
      if(empty($_SESSION["shopping_cart"]))
      unset($_SESSION["shopping_cart"]);
      }		
}
}

if (isset($_POST['action']) && $_POST['action']=="change"){
  foreach($_SESSION["shopping_cart"] as &$value){
    if($value['ProductID'] === $_POST["ProductID"]){
        $value['quantity'] = $_POST["quantity"];
        break; // Stop the loop after we've found the product
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
    <link rel="stylesheet"type="text/css" media="screen" href="css/cart.css" >
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    </head>

<body>

        <div class="cart">
        <?php
        if(isset($_SESSION["shopping_cart"])){
                $total_price = 0;
                ?>	
                <table class="table">
                    <tbody>
                    <tr>
                        <td></td>
                        <td>ITEM NAME</td>
                        <td>QUANTITY</td>
                        <td>UNIT PRICE</td>
                        <td>ITEMS TOTAL</td>
                    </tr>	
                    <?php		
                  foreach ($_SESSION["shopping_cart"] as $product){
                    ?>
                        <tr>
                            <td>
                            <img src='<?php echo $product["image"]; ?>' width="50" height="40" />
                            </td>
                            <td><?php echo $product["name"]; ?><br />
                            <form method='post' action=''>
                                <input type='hidden' name='ProductID' value="<?php echo $product["ProductID"]; ?>" />
                                <input type='hidden' name='action' value="remove" />
                                <button type='submit' class='remove'>Remove Item</button>
                            </form>
                            </td>
                            <td>
                            <form method='post' action=''>
                                <input type='hidden' name='ProductID' value="<?php echo $product["ProductID"]; ?>" />
                                <input type='hidden' name='action' value="change" />
                                <select name='quantity' class='quantity' onChange="this.form.submit()">
                                    <option <?php if($product["quantity"]==1) echo "selected";?>
                                    value="1">1</option>
                                    <option <?php if($product["quantity"]==2) echo "selected";?>
                                    value="2">2</option>
                                    <option <?php if($product["quantity"]==3) echo "selected";?>
                                    value="3">3</option>
                                    <option <?php if($product["quantity"]==4) echo "selected";?>
                                    value="4">4</option>
                                    <option <?php if($product["quantity"]==5) echo "selected";?>
                                    value="5">5</option>
                                </select>
                            </form>
                            </td>
                            <td><?php echo "$".$product["price"]; ?></td>
                            <td><?php echo "$".$product["price"]*$product["quantity"]; ?></td>
                        </tr>
                            <?php
                            $total_price += ($product["price"]*$product["quantity"]);
                    }
                    ?>
                    <tr>
                    <td colspan="5" align="right">
                    <strong>TOTAL: <?php echo "$".$total_price; ?></strong>
                    </td>
                    </tr>
                    </tbody>
                </table>		
                <?php
        }

        else{
            echo "<h3>Your cart is empty!</h3>";
            }
        ?>
        </div>

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
