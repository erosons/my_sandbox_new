<?php
   
   include "connections.php";

  // $user_data=  validate_user_profile($conn);
?>


<!DOCTYPE html>
<html lang="en">

    <head>

        <meta http-equiv="Content-Type" content="text/html;charset=UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KK94CHFLLe+nY2dmCWGMq91rCGa5gtU4mk92HdvYe+M/SXH301p5ILy+dN9+nJOZ" crossorigin="anonymous">
        <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.7/dist/umd/popper.min.js" integrity="sha384-zYPOMqeu1DAVkHiLqWBUTcbYfZ8osu1Nd6Z89ify25QV9guujx43ITvfi12/QExE" crossorigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/js/bootstrap.min.js" integrity="sha384-Y4oOpwW3duJdCWv5ly8SCFYWqFDsfob/3GkgExXKV4idmbt98QcxXYs9UoXAB7BZ" crossorigin="anonymous"></script>    
    </head>

    <body style ="margin: 50px;background-color:#d0f5fc;">
    <div class="bg-success p-2 text-dark bg-opacity-75" >
         <ul class="nav justify-content-center">
               <li class="nav-item">
                   <a class="nav-link"  style ="color: White;font-size: 2.3em;font-family: Helvetica;"  href="#">Ecommerce Inventory Management Portal</a>
              </li>
               <li class="nav-item">
                   <a class="nav-link" style ="color: White;font-size: 1em;font-family: Helvetica;" href="index.php">Logout</a>
               </li>
          </ul>
     </div>   
        <hr>
   <br>
   <br>
   <!--- Ten SQL Queries  -->
       <p>
          <a class="btn btn-primary" data-bs-toggle="collapse" href="#multiCollapseExample1" role="button" aria-expanded="false" aria-controls="multiCollapseExample1">productBycategories</a>
            <button class="btn btn-primary" type="button" data-bs-toggle="collapse" data-bs-target="#multiCollapseExample2" aria-expanded="false" aria-controls="multiCollapseExample2">Toggle second element</button>
            <button class="btn btn-primary" type="button" data-bs-toggle="collapse" data-bs-target="#multiCollapseExample3" aria-expanded="false" aria-controls="multiCollapseExample2">Toggle second element</button>
            <button class="btn btn-primary" type="button" data-bs-toggle="collapse" data-bs-target="#multiCollapseExample4" aria-expanded="false" aria-controls="multiCollapseExample2">Toggle second element</button>
            <button class="btn btn-primary" type="button" data-bs-toggle="collapse" data-bs-target="#multiCollapseExample5" aria-expanded="false" aria-controls="multiCollapseExample2">Toggle second element</button>
            <button class="btn btn-primary" type="button" data-bs-toggle="collapse" data-bs-target="#multiCollapseExample6" aria-expanded="false" aria-controls="multiCollapseExample2">Toggle second element</button>
            <button class="btn btn-primary" type="button" data-bs-toggle="collapse" data-bs-target="#multiCollapseExample7" aria-expanded="false" aria-controls="multiCollapseExample2">Toggle second element</button>
            <button class="btn btn-primary" type="button" data-bs-toggle="collapse" data-bs-target="#multiCollapseExample8" aria-expanded="false" aria-controls="multiCollapseExample2">Toggle second element</button>
            <button class="btn btn-primary" type="button" data-bs-toggle="collapse" data-bs-target="#multiCollapseExample9" aria-expanded="false" aria-controls="multiCollapseExample2">Toggle second element</button>
            <button class="btn btn-primary" type="button" data-bs-toggle="collapse" data-bs-target="#multiCollapseExample10" aria-expanded="false" aria-controls="multiCollapseExample2">Toggle second element</button>
            <button class="btn btn-primary" type="button" data-bs-toggle="collapse" data-bs-target=".multi-collapse" aria-expanded="false" aria-controls="multiCollapseExample1 multiCollapseExample2">Show All Tables</button>
     </p>
     <!--BizQuestion1 -->
     <div class="row">
          <div class="col">
             <div class="collapse multi-collapse" id="multiCollapseExample1">
                <div class="card card-body">
                  <h3 >productBycategories Counts</h3>
                    <br>
                    <table class="table table-striped">
                        <thead>
                            <tr>
                                <th>catergoryName</th>
                                <th>ProductCount</th>
                            </tr>
                        </thead>
                         <tbody>
                                <?php

                                    $query="Select * from EIMS.bottom5products";
                                    $result= mysqli_query($conn,$query);
                                    if(mysqli_num_rows($result) > 0 ){
                                        while($row = mysqli_fetch_array($result)) {
                                            echo " <tr>
                                                <td>" .$row['product_name']."</td>
                                                <td>".$row['order_amount']. "</td>
                                                <td>
                                                <a class='btn btn-primary btn-sm' href='update'>Update</a>
                                                <a class='btn btn-danger btn-sm' href='delete'>Delete</a>
                                                </td>
                                        </tr>";

                                    }
                                    }
                                    else {
                                    echo "No record found";
                                    }

                                
                                ?>
                         </tbody>
                    
                        </table>
              </div>
         </div>
     </div>
     <!--BizQuestion2 -->
     <div class="row">
          <div class="col">
             <div class="collapse multi-collapse" id="multiCollapseExample2">
                <div class="card card-body">
                  <h3 >productBycategories Counts</h3>
                    <br>
                    <table class="table table-striped">
                        <thead>
                            <tr>
                                <th>catergoryName</th>
                                <th>ProductCount</th>
                            </tr>
                        </thead>
                         <tbody>
                                <?php

                                    $query="Select * from EIMS.bottom5products";
                                    $result= mysqli_query($conn,$query);
                                    if(mysqli_num_rows($result) > 0 ){
                                        while($row = mysqli_fetch_array($result)) {
                                            echo " <tr>
                                                <td>" .$row['product_name']."</td>
                                                <td>".$row['order_amount']. "</td>
                                                <td>
                                                <a class='btn btn-primary btn-sm' href='update'>Update</a>
                                                <a class='btn btn-danger btn-sm' href='delete'>Delete</a>
                                                </td>
                                        </tr>";

                                    }
                                    }
                                    else {
                                    echo "No record found";
                                    }

                                
                                ?>
                         </tbody>
                    
                        </table>
              </div>
         </div>
     </div>
     <!--BizQuestion3 -->
     <div class="row">
          <div class="col">
             <div class="collapse multi-collapse" id="multiCollapseExample3">
                <div class="card card-body">
                  <h3 >productBycategories Counts</h3>
                    <br>
                    <table class="table table-striped">
                        <thead>
                            <tr>
                                <th>catergoryName</th>
                                <th>ProductCount</th>
                            </tr>
                        </thead>
                         <tbody>
                                <?php

                                    $query="Select * from EIMS.bottom5products";
                                    $result= mysqli_query($conn,$query);
                                    if(mysqli_num_rows($result) > 0 ){
                                        while($row = mysqli_fetch_array($result)) {
                                            echo " <tr>
                                                <td>" .$row['product_name']."</td>
                                                <td>".$row['order_amount']. "</td>
                                                <td>
                                                <a class='btn btn-primary btn-sm' href='update'>Update</a>
                                                <a class='btn btn-danger btn-sm' href='delete'>Delete</a>
                                                </td>
                                        </tr>";

                                    }
                                    }
                                    else {
                                    echo "No record found";
                                    }

                                
                                ?>
                         </tbody>
                    
                        </table>
              </div>
         </div>
     </div>
     <!--BizQuestion4 -->
     <div class="row">
          <div class="col">
             <div class="collapse multi-collapse" id="multiCollapseExample4">
                <div class="card card-body">
                  <h3 >productBycategories Counts</h3>
                    <br>
                    <table class="table table-striped">
                        <thead>
                            <tr>
                                <th>catergoryName</th>
                                <th>ProductCount</th>
                            </tr>
                        </thead>
                         <tbody>
                                <?php

                                    $query="Select * from EIMS.bottom5products";
                                    $result= mysqli_query($conn,$query);
                                    if(mysqli_num_rows($result) > 0 ){
                                        while($row = mysqli_fetch_array($result)) {
                                            echo " <tr>
                                                <td>" .$row['product_name']."</td>
                                                <td>".$row['order_amount']. "</td>
                                                <td>
                                                <a class='btn btn-primary btn-sm' href='update'>Update</a>
                                                <a class='btn btn-danger btn-sm' href='delete'>Delete</a>
                                                </td>
                                        </tr>";

                                    }
                                    }
                                    else {
                                    echo "No record found";
                                    }

                                
                                ?>
                         </tbody>
                    
                        </table>
              </div>
         </div>
     </div>
      <!--BizQuestion5 -->
      <div class="row">
          <div class="col">
             <div class="collapse multi-collapse" id="multiCollapseExample5">
                <div class="card card-body">
                  <h3 >productBycategories Counts</h3>
                    <br>
                    <table class="table table-striped">
                        <thead>
                            <tr>
                                <th>catergoryName</th>
                                <th>ProductCount</th>
                            </tr>
                        </thead>
                         <tbody>
                                <?php

                                    $query="Select * from EIMS.bottom5products";
                                    $result= mysqli_query($conn,$query);
                                    if(mysqli_num_rows($result) > 0 ){
                                        while($row = mysqli_fetch_array($result)) {
                                            echo " <tr>
                                                <td>" .$row['product_name']."</td>
                                                <td>".$row['order_amount']. "</td>
                                                <td>
                                                <a class='btn btn-primary btn-sm' href='update'>Update</a>
                                                <a class='btn btn-danger btn-sm' href='delete'>Delete</a>
                                                </td>
                                        </tr>";

                                    }
                                    }
                                    else {
                                    echo "No record found";
                                    }

                                
                                ?>
                         </tbody>
                    
                        </table>
              </div>
         </div>
     </div>
      <!--BizQuestion6 -->
      <div class="row">
          <div class="col">
             <div class="collapse multi-collapse" id="multiCollapseExample6">
                <div class="card card-body">
                  <h3 >productBycategories Counts</h3>
                    <br>
                    <table class="table table-striped">
                        <thead>
                            <tr>
                                <th>catergoryName</th>
                                <th>ProductCount</th>
                            </tr>
                        </thead>
                         <tbody>
                                <?php

                                    $query="Select * from EIMS.bottom5products";
                                    $result= mysqli_query($conn,$query);
                                    if(mysqli_num_rows($result) > 0 ){
                                        while($row = mysqli_fetch_array($result)) {
                                            echo " <tr>
                                                <td>" .$row['product_name']."</td>
                                                <td>".$row['order_amount']. "</td>
                                                <td>
                                                <a class='btn btn-primary btn-sm' href='update'>Update</a>
                                                <a class='btn btn-danger btn-sm' href='delete'>Delete</a>
                                                </td>
                                        </tr>";

                                    }
                                    }
                                    else {
                                    echo "No record found";
                                    }

                                
                                ?>
                         </tbody>
                    
                        </table>
              </div>
         </div>
     </div>
      <!--BizQuestion7 -->
      <div class="row">
          <div class="col">
             <div class="collapse multi-collapse" id="multiCollapseExample7">
                <div class="card card-body">
                  <h3 >productBycategories Counts</h3>
                    <br>
                    <table class="table table-striped">
                        <thead>
                            <tr>
                                <th>catergoryName</th>
                                <th>ProductCount</th>
                            </tr>
                        </thead>
                         <tbody>
                                <?php

                                    $query="Select * from EIMS.bottom5products";
                                    $result= mysqli_query($conn,$query);
                                    if(mysqli_num_rows($result) > 0 ){
                                        while($row = mysqli_fetch_array($result)) {
                                            echo " <tr>
                                                <td>" .$row['product_name']."</td>
                                                <td>".$row['order_amount']. "</td>
                                                <td>
                                                <a class='btn btn-primary btn-sm' href='update'>Update</a>
                                                <a class='btn btn-danger btn-sm' href='delete'>Delete</a>
                                                </td>
                                        </tr>";

                                    }
                                    }
                                    else {
                                    echo "No record found";
                                    }

                                
                                ?>
                         </tbody>
                    
                        </table>
              </div>
         </div>
     </div>
      <!--BizQuestion8 -->
      <div class="row">
          <div class="col">
             <div class="collapse multi-collapse" id="multiCollapseExample8">
                <div class="card card-body">
                  <h3 >productBycategories Counts</h3>
                    <br>
                    <table class="table table-striped">
                        <thead>
                            <tr>
                                <th>catergoryName</th>
                                <th>ProductCount</th>
                            </tr>
                        </thead>
                         <tbody>
                                <?php

                                    $query="Select * from EIMS.bottom5products";
                                    $result= mysqli_query($conn,$query);
                                    if(mysqli_num_rows($result) > 0 ){
                                        while($row = mysqli_fetch_array($result)) {
                                            echo " <tr>
                                                <td>" .$row['product_name']."</td>
                                                <td>".$row['order_amount']. "</td>
                                                <td>
                                                <a class='btn btn-primary btn-sm' href='update'>Update</a>
                                                <a class='btn btn-danger btn-sm' href='delete'>Delete</a>
                                                </td>
                                        </tr>";

                                    }
                                    }
                                    else {
                                    echo "No record found";
                                    }

                                
                                ?>
                         </tbody>
                    
                        </table>
              </div>
         </div>
     </div>
      <!--BizQuestion9 -->
      <div class="row">
          <div class="col">
             <div class="collapse multi-collapse" id="multiCollapseExample9">
                <div class="card card-body">
                  <h3 >productBycategories Counts</h3>
                    <br>
                    <table class="table table-striped">
                        <thead>
                            <tr>
                                <th>catergoryName</th>
                                <th>ProductCount</th>
                            </tr>
                        </thead>
                         <tbody>
                                <?php

                                    $query="Select * from EIMS.bottom5products";
                                    $result= mysqli_query($conn,$query);
                                    if(mysqli_num_rows($result) > 0 ){
                                        while($row = mysqli_fetch_array($result)) {
                                            echo " <tr>
                                                <td>" .$row['product_name']."</td>
                                                <td>".$row['order_amount']. "</td>
                                                <td>
                                                <a class='btn btn-primary btn-sm' href='update'>Update</a>
                                                <a class='btn btn-danger btn-sm' href='delete'>Delete</a>
                                                </td>
                                        </tr>";

                                    }
                                    }
                                    else {
                                    echo "No record found";
                                    }

                                
                                ?>
                         </tbody>
                    
                        </table>
              </div>
         </div>
     </div>
      <!--BizQuestion10 -->
      <div class="row">
          <div class="col">
             <div class="collapse multi-collapse" id="multiCollapseExample10">
                <div class="card card-body">
                  <h3 >productBycategories Counts</h3>
                    <br>
                    <table class="table table-striped">
                        <thead>
                            <tr>
                                <th>catergoryName</th>
                                <th>ProductCount</th>
                            </tr>
                        </thead>
                         <tbody>
                                <?php

                                    $query="Select * from EIMS.bottom5products";
                                    $result= mysqli_query($conn,$query);
                                    if(mysqli_num_rows($result) > 0 ){
                                        while($row = mysqli_fetch_array($result)) {
                                            echo " <tr>
                                                <td>" .$row['product_name']."</td>
                                                <td>".$row['order_amount']. "</td>
                                                <td>
                                                <a class='btn btn-primary btn-sm' href='update'>Update</a>
                                                <a class='btn btn-danger btn-sm' href='delete'>Delete</a>
                                                </td>
                                        </tr>";

                                    }
                                    }
                                    else {
                                    echo "No record found";
                                    }

                                
                                ?>
                         </tbody>
                    
                        </table>
              </div>
         </div>
     </div>
    </body>
</html>
