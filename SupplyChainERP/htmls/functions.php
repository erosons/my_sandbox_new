<?php
session_start();

function validate_user_profile($conn){

  if(isset($_SESSION['user_id'])){
       $id=$_SESSION['user_id'];

       $query="Select * from YapaDB.users where user_id='$id' limit 1";
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


function random_num_gen($length){

   for($i=0;$i<$length;$i++){

     $text .= rand(2,$length);

    return $text;
   }
}
?>
