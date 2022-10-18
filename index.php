<!DOCTYPE html>
<html>
<head>
  <link rel="stylesheet" href="styles.css">
    <div class="center">
        <p>Enter details:</p>
        <form action="/estimate_home_price/" method="post">
            <label for="adr">Address:</label><br>
            <input type="text" id="adr" name="adr"><br>
            <br />
            <label for="size">Size (in sqft):</label><br>
            <input type="text" id="size" name="size">
            <br />
            <br />
            <button type="submit">Submit</button>
          </form>
    </div>
</head>
</html>
