<?php

$servername="localhost";
$username="sammy";
$password="password";
$DB="YapaDB";


//Create a connection to your Datbase

$conn = mysqli_connect($servername,$username,$password,$DB) ;

//Test Connection

if(!$conn){

    die("Connection failed ". mysqli_error()) ;
}


?>
