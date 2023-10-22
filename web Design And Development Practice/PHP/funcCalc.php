<?php
function add($a , $b){
    $add = $a + $b;
    return $add;
}

$a = readline("enter first number : ");
$b = readline("enter first number : ");
$sum = add($a , $b);
echo "The Sum of $a and $b is : $sum";
?>