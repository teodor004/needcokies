<?php
$message = $_POST['message']; // Get the message from the form
$file = "D:/Git/HTML/note.txt"; // File to save the message to

// Open the file in append mode
$handle = fopen($file, 'a');

// Write the message to the file
fwrite($handle, $message . PHP_EOL); // PHP_EOL adds a newline after each message

// Close the file handle
fclose($handle);

// Redirect back to the page
header("Location: ".$_SERVER['HTTP_REFERER']);
exit;
?>
