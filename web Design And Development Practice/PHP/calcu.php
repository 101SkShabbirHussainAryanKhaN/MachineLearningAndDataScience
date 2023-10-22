<!DOCTYPE html>
<html>
<head>
    <title>Simple Calculator</title>
    <link rel="stylesheet" type="text/css" href="calcul.css">
</head>
<body>
    <div class="calculator">
        <h2>Result:</h2>
        <?php
        if(isset($_POST['calculate'])){
            $num1 = $_POST['num1'];
            $num2 = $_POST['num2'];
            $operator = $_POST['operator'];

            switch($operator){
                case "add":
                    $result = $num1 + $num2;
                    break;
                case "subtract":
                    $result = $num1 - $num2;
                    break;
                case "multiply":
                    $result = $num1 * $num2;
                    break;
                case "divide":
                    if ($num2 != 0) {
                        $result = $num1 / $num2;
                    } else {
                        $result = "Cannot divide by zero";
                    }
                    break;
                default:
                    $result = "Invalid operator";
            }

            echo "Result: " . $result;
        }
        ?>
    </div>
</body>
</html>
