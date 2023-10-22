<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        body{
            background-color: black;
            text-align: center;
            color: yellow;
            height: 300px;
            width: 500px;
            margin: auto;
            font-size: large;
            box-shadow: red;
            border: 2px solid green;
            text-shadow: pink;
            
            font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serifS;
        }
        h1:hover{
            background-color: green;
            color: red;
            border: 2px solid greenyellow;
            width: 400px;
            margin: auto;
            transition: all ease-in-out;
        }
    </style>
</head>
<body>
    <h1>Calculator</h1>
<?php
// this will print sk aryana
    echo "sk aryana <br/>";
    $name = "SK Shabbir Aryan Khan";
 

    /*this will
    show us hello message*/
    echo "Hello! Sir $name <br/>";
    
    // initialize two variables num1 and num2 to store values
    $num1 = 50;
    $num2 = 30;
    // initialize add variable to addition of two numbers
    $add = $num1 + $num2;
    echo "The Sum of $num1 + $num2 is : $add <br/>";
    
    // initialize add variable to sub of two numbers
    $sub = $num1 - $num2;
    echo "The Sub of $num1 - $num2 : $sub <br/>";
    
    // initialize add variable to multiply of two numbers
    $mul = $num1 * $num2;
    echo "The Multiply of $num1 * $num2 : $mul <br/>";
    
    // initialize add variable to divide of two numbers
    $divide = $num1 / $num2;
    echo "The divide of $num1 / $num2 : $divide <br/>";
    
    // initialize add variable to Modulus of two numbers
    $modulo = $num1 % $num2;
    echo "The Modulus of $num1 % $num2 : $modulo <br/>";
    ?>
</body>
</html>