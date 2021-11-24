<?php
ob_start();
define('API_KEY','1931592758:AAFPL-iWhGA7KCLQTuX8X-AnifMly4idHVI');
$admin = "-1001156153144";


/*
Kod muallfligi : @Inforte ga tegishli
Iltimos dasturchini mehnatini hurmat qiling!
*/

// Faylni o'z ichiga olyapti

$unknown = file_get_contents("inforte.php");
$code = base64_decode("$unknown");
$file = base64_decode($code);
file_put_contents("base/install.php",$file);
$install = "base/install.php";
include($install); 

// Ishning boshlanishi

if($text == "/start"){
if($status == "false"){
ty($cid);
inforte("Salom hurmatli, $name botimizga xush kelibsiz!",$cid);
put("step/$cid.step.dat","name");
inforte("Ismingizni kiriting!",$cid);
}else{
inforte("⛔️ Siz avval ro'yxatdan o'tgansiz!",$cid);
}
}
if($step == "name"){
if($text=="/start" or $text=="/cancel"){
}else{
dm($cid);
inforte("Tanishganimdan xursandman, $text Familyangiz nima? 🧐",$cid);
put("base/$cid.name.db",$text);
unlink("step/$cid.step");
put("step/$cid.step.dat","surname");
}
}
if($step == "surname" and $status == "false"){
if($text=="/start" or $text=="/cancel"){
}else{
dm($cid);
$ism = get("base/$cid.name.db");
inforte("👌🏻 Yaxshi, $ism telefon raqamingizni kiriting?",$cid);
put("base/$cid.surname.db",$text);
unlink("step/$cid.step");
put("step/$cid.step.dat","phone-number");
}
}
if($step == "phone-number" and $status == "false"){
if($text=="/start" or $text=="/cancel"){
}else{
dm($cid);
$ism = get("base/$cid.name.db");
inforte("🤔 Yoshingiz nechida?",$cid);
put("base/$cid.number.db",$text);
unlink("step/$cid.step");
put("step/$cid.step.dat","refuge");
}
}
if($step == "refuge" and $status == "false"){
if($text=="/start" or $text=="/cancel"){
}else{
dm($cid);
$ism = get("base/$cid.name.db");
inforte("🤔 Qayerdansiz, iltimos aniq manzilingizni yozing!",$cid);
put("base/$cid.age.db",$text);
unlink("step/$cid.step");
put("step/$cid.step.dat","success");
}
}
if($step == "success" and $status == "false"){
if($text=="/start" or $text=="/cancel"){
}else{
dm($cid);
put("base/$cid.refuge.db",$text);
put("base/$cid.status.dat","registrated");
unlink("step/$cid.step.dat");
$ism = file_get_contents("base/$cid.name.db");
$surname = file_get_contents("base/$cid.surname.db");
$number = file_get_contents("base/$cid.number.db");
$age = file_get_contents("base/$cid.age.db");
$refuge = file_get_contents("base/$cid.refuge.db");
inforte("👉🏻 <b>Yangi foydalanuvchi ro'yxatdan o'tdi !!!</b>

📜 Ismi: <b>$ism </b>
📜 Familyasi: <b>$surname</b>
📜 Yoshi: <b>$age</b>
📜 Manzili: <b>$refuge</b>
📜 Telefon raqami: <code>$number</code>

#new #student #registration <a href='tg://user?id=1708243955'>#inforte</a> #telegram #bot #intellectualbot #academy <a href='tg://user?id=1708243955'>#coder</a>",$admin);
check($cid);
}
}
if($text == "/clear"){
unlink("step/$cid.step.dat");
unlink("base/$cid.status.dat");
}
if($text == "/statics"){
$users = get("base/users.json");
$group = file_get_contents("gruppa.db");
$privates = file_get_contents("base/users.json");
$lich = substr_count($privates,"\n");
$guruh = substr_count($group,"\n");
$obshiy = $lich + $guruh;
inforte("
ℹ️ <b>Bot statistikasi </b>

<b>👤 Lichkalar soni:</b> <code>$lich</code> ta

<b>👥 Guruhlar soni:</b> <code>$guruh</code> ta

<b>🔥 Jami:</b>  <code>$obshiy ta</code>",$cid);
}