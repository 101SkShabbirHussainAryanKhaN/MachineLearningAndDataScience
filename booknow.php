<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Database connection details
    $db_host = "localhost";
    $db_user = "root";
    $db_password = "";
    $db_name = "hotel";

    // Create a database connection
    $conn = new mysqli($db_host, $db_user, $db_password, $db_name);

    // Check if the connection is successful
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }

    // Retrieve form data
    $fname = $_POST['fname'];
    $lname = $_POST['lname'];
    $cnic = $_POST['cnic'];
    $email = $_POST['email'];
    $nbr = $_POST['nbr'];
    $address = $_POST['address'];
    $checkin = $_POST['checkin'];
    $checkout = $_POST['checkout'];
    $adults = $_POST['adults'];
    $children = $_POST['children'];
    $rooms = $_POST['rooms'];
    $beds = $_POST['beds'];
    $creditcard = $_POST['creditcard'];
    $expiry = $_POST['expiry'];
    $cvv = $_POST['cvv'];
    $roomType = $_POST['roomType'];
    $numberOfDays = $_POST['numberOfDays'];

    // Calculate the total amount (you can reuse the JavaScript function or calculate it here)
    $totalAmount = $roomRates[$roomType] * $numberOfDays;

    // SQL query to insert data into the database
    $sql = "INSERT INTO bookings (fname, lname, cnic, email, nbr, address, checkin, checkout, adults, children, rooms, beds, creditcard, expiry, cvv, roomType, numberOfDays, totalAmount)
            VALUES ('$fname', '$lname', '$cnic', '$email', '$nbr', '$address', '$checkin', '$checkout', '$adults', '$children', '$rooms', '$beds', '$creditcard', '$expiry', '$cvv', '$roomType', '$numberOfDays', '$totalAmount')";

    if ($conn->query($sql) === TRUE) {
        // Booking data has been successfully inserted
        echo "Booking completed successfully.";
    } else {
        // Error occurred while inserting data
        echo "Error: " . $sql . "<br>" . $conn->error;
    }

    // Close the database connection
    $conn->close();
}
?>
