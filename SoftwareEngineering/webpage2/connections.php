<?php

$servername="localhost";
$username="s";
$password=";
$DB="test2_db";


//Create a connection to your Datbase

$conn = mysqli_connect($servername,$username,$password,$DB) ;

//Test Connection

if(!$conn){

    die("Connection failed ". mysqli_error()) ;
}

//echo "Connected successfully";


?>