<?php
session_start();

function validate_user_profile($conn){

  if(isset($_SESSION['Trudy'])){
       $id=$_SESSION['Trudy'];

       $query="Select * from EIMS.customer where first_name='$id' and staff is not null limit 1";
       $result= mysqli_query($conn,$query);


       if($result && mysqli_num_rows($result)>0){

            $user_data= mysqli_fetch_assoc($result);
            return $user_data;
        

       }

  }

  // Basically is the user profile is not found in the DB we redirect to login
//   else

//     header("Location: login.php");
//     die;

}

