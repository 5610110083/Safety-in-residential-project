<html>
<head>
<?php 
if (isset($_POST['on']))
{
exec('sudo python /var/www/on.py');
echo "ON";
}
if (isset($_POST['off']))
{
exec('sudo python /var/www/off.py');
echo "OFF";
}
?>

  <title></title>
</head>
<body>
<form method="post">
  <table
 style="width: 75%; text-align: left; margin-left: auto; margin-right: auto;"
 border="0" cellpadding="2" cellspacing="2">
    <tbody>
      <tr>
        <td style="text-align: center;">Turn LED on</td>
        <td style="text-align: center;">Turn LED off</td>
      </tr>
      <tr>
        <td style="text-align: center;"><button name="on">On</button></td>
        <td style="text-align: center;"><button name="off">Off</button></td>
      </tr>
    </tbody>
  </table>
</form>
</body>
</html>

