<html>
<body>
<link rel="stylesheet" href="styles.css">
    <div class="center">
        <p>Enter details:</p>
        <form action="estimated_price.php" method="get">
            <label for="adr">Address:</label><br>
            <input type="text" id="adr" name="adr"><br>
            <br />
            <label for="size">Size (in sqft):</label><br>
            <input type="text" id="size" name="size">
            <br />
            <br />
            <button type="submit">Submit</button>
          </form>
         <br />
        <?php
         $address = $_GET["adr"];
         $size = $_GET["size"];

         $server = "localhost" ;
         $username = "root";
         $password = "";
         $dbname = "house_name" ;

         $conn = mysqli_connect($server , $username , $password , $dbname) ;
         $query = "insert into form(Address,Size) values('$address' , '$size')" ;
         $run = mysqli_query($conn,$query) or die(mysqli_error());
         ?>
        <p><?php echo $result; ?></p>
    </div>
</body>
</html>