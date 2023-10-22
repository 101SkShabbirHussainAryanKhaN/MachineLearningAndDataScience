<?php
$x = 5;  //global variable
function mytext($x){
    
    echo "<p> Variable x inside function is : $x </p>";
}

mytext(10);

echo "<p> Variable x inside function is : $x </p>";

//  how to access global variable inside the function

$s = 15;
$y = 20;
function addition(){
    global $s , $y;
    $y = $s + $y;
    
    
}
addition();

echo "The $y is: $y <br>";





function myTxt(){
    $GLOBALS['y']  = $GLOBALS['s'] + $GLOBALS['y'] ;
}

myTxt();
echo $y;
?>