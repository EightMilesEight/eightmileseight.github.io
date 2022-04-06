<body>

<h1>browser</h1>
/* gets the data from a URL */

?>

<form action="/webb/browse.php" method="post">
url: <input type="text" name="url"><br>
<input type="submit">
</form>

url - https://<?php echo $_POST["url"]; ?><br>

<?php

$url = $_POST["url"];
$homepage = file_get_contents('h'.$url);
echo $homepage;

?>

</body>
