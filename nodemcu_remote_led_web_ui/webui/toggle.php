<?
date_default_timezone_set('America/New_York');

# Retrieve current state of light:
if(isset($_GET['current'])){

  $file = "data.txt";
  $fp = fopen($file, "r") or die("Unable to open file!");
  echo fgets($fp);
  fclose($fp);

}

# Retrieve log data:
if(isset($_GET['log'])){

  $file = "log.txt";
  $fp = fopen($file, "r") or die("Unable to open file!");
  echo fread($fp,filesize("log.txt"));
  fclose($fp);

}

# Button was clicked:
if (isset($_GET['state'])){

  // Write the new light state:
  $fp = fopen("data.txt", "w") or die("Unable to open file!");
  fwrite($fp, $_GET['state']);
  fclose($fp);
  echo $_GET['state']; // Echo state.

  $fp = fopen("log.txt", "a") or die("Unable to open file!");

  $state = ($_GET['state'] === '1')?'ON':'OFF';
  $ip = $_SERVER['REMOTE_ADDR'];
  $now = date("F j, Y, g:i a");

  // IP Info API:
  $data = file_get_contents('https://ipinfo.io/'.$ip.'/json');
  $json = json_decode($data,1);

  $message = $state.'-'.$json['city'].', '.$json['region'].'-'.$now."\r\n";
  fwrite($fp, $message);
  fclose($fp);

}
?>
