<?php
// Database configuration
$servername = "localhost";
$username = "root";
$password = "db";
$dbname = "hotel";

// Create a database connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check the connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

// Check if the form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
  $name = $_POST["name"];
  $email = $_POST["email"];
  $country = $_POST["country"];
  $remarks = $_POST["remarks"];

  // Prepare and execute the SQL query to insert the form data into the database
  $sql = "INSERT INTO contact_form (name, email, country, remarks) VALUES (?, ?, ?, ?)";
  $stmt = $conn->prepare($sql);
  $stmt->bind_param("ssss", $name, $email, $country, $remarks);

  if ($stmt->execute()) {
    // Data inserted successfully


  } else {
    // Error in inserting data
    echo "Error: " . $sql . "<br>" . $conn->error;
  }

  // Close the database connection
  $stmt->close();
  $conn->close();
}
