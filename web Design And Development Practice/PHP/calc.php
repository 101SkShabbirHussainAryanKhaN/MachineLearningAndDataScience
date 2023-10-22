<!DOCTYPE html>
<?php
//echo 'Hello World.';
// This is a one-line c++ style comment
    /* This is a multi line comment
       yet another line of comment */
	   
//phpinfo();

//echo 'Hello World!!!/n Below is a basic calculator I made!';
echo '<span style="color:#196719;text-align:center;">Hello World!. Below is a basic calculator I made!</span>';
//echo  <span style="color:#AFA;text-align:center;">nl2br ("Hellow World! \n Below is a basic calculator I made!")</span>;

ini_set('display_errors',0);
	
	if(isset($_POST['submit']))
	{
		$num1=$_POST['number1'];
		$num2=$_POST['number2'];
		if(is_numeric['$num1'] && is_numeric['$num2'])
		{
			if(isset($_POST['g']))
			{
				$operation=$_POST['g'];
				
				switch($operation)
				{
					case '+' :
					$result=$num1+$num2;
					break;
					
					case '-' :
					$result=$num1-$num2;
					break;
					
					case '*' :
					$result=$num1*$num2;
					break;
					
					
					case '/' :
					$result=$num1/$num2;
					break;
					
					case '%' :
					$result=$num1%$num2;
					break;
				}
				
				
			}
			else
			{
				echo "Please select operation";
			}
			
		}
		else
		{
			echo "Please enter numeric values only";
		}
	}
?>

<html>
<head>
<style> 
#group {
	animation-fill-mode: forwards; /*animation will stop at last frame and won't reset to start!!!*/
    -webkit-animation: mymove 5s 1; /* Safari 4.0 - 8.0 */
    animation: mymove 5s 1;
	  position: absolute;
       left: 5px;
}

/*#get {
	
	 position: absolute;
     left: 5px;
}*/

div {
    width: 100px;
    height: 50px;
    background-color: red;
    font-weight: bold;
    position: relative;
	/*position: absolute;*/
    left: 5px;
}

/* Safari 4.0 - 8.0 */
#div1 {-webkit-animation-timing-function: linear;}
#div2 {-webkit-animation-timing-function: ease;}
#div3 {-webkit-animation-timing-function: ease-in;}
#div4 {-webkit-animation-timing-function: ease-out;}
#div5 {-webkit-animation-timing-function: ease-in-out;}

/* Standard syntax */
#div1 {animation-timing-function: linear;}
#div2 {animation-timing-function: ease;}
#div3 {animation-timing-function: ease-in;}
#div4 {animation-timing-function: ease-out;}
#div5 {animation-timing-function: ease-in-out;}

/* Safari 4.0 - 8.0 */
@-webkit-keyframes mymove {
    from {left: 0px;}
    to {left: 300px;}
}

/* Standard syntax */
@keyframes mymove {
    from {left: 0px;}
    to {left: 300px;}
}
</style>
</head>
<body>

<p><strong>Note:</strong> The animation-timing-funtion property is not supported in Internet Explorer 9 and earlier versions.</p>

<!--<div id="div1">linear</div>
<div id="div2">ease</div>
<div id="div3">ease-in</div>
<div id="div4">ease-out</div>
<div id="div5">ease-in-out</div>-->

<div id="get">
		<form method="post" action="BasicCalculator.php">
<div id="group">        
<div id="div1">Enter 1st number: <input type="text" name="number1" value="<?php if(isset($num1)) {echo $num1;} ?> " > </div></br> </br>
        <div id="div2">Enter 2nd number: <input type="text" name="number2"  value="<?php if(isset($num2)) {echo $num2;} ?> " ></div> </br> </br>
Select Operation: </br></br>
                        <div id="div3"><input type="radio" name="g" value="+"> Addition</div> <br/>
                        <div id="div4"><input type="radio" name="g" value="-"> Subtraction</div></br>
                        <div id="div1"><input type="radio" name="g" value="*">Multiplication</div> <br/>
                        <div id="div2"><input type="radio" name="g" value="/">Division</div> </br>
                        <div id="div3"><input type="radio" name="g" value="%">Modulo</div> <br/><br/>
                        <div id="div4"><input type="submit" name="submit"></div><br/><br/>
                        <div id="div5"><h2 style="color:blue"> Output: <?php echo $result; ?> </h2></div>
        </div>
</form>

</div>


<script>
//Your Javascript Code

for(let i =5; i < window.width(); i++)
{
    document.getElementById('YOURELEMENT').left = i + 'px';
}

</script



</body>
</html>
