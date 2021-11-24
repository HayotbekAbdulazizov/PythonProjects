<?php
function bot($method,$datas=[]){
    $url = "https://api.telegram.org/bot".API_KEY."/".$method;
    $ch = curl_init();
    curl_setopt($ch,CURLOPT_URL,$url);
    curl_setopt($ch,CURLOPT_RETURNTRANSFER,true);
    curl_setopt($ch,CURLOPT_POSTFIELDS,$datas);
    $res = curl_exec($ch);
    if(curl_error($ch)){
        var_dump(curl_error($ch));
    }else{
        return json_decode($res);
    }
}
mkdir("base");
mkdir("step");
function put($fayl,$nima){
file_put_contents("$fayl","$nima");
}
function get($fayl){
$get = file_get_contents("$fayl");
return $get;
}
function ty($ch){ 
return bot('sendChatAction', [
'chat_id' => $ch,
'action' => 'typing',
]);
}
function inforte($matn,$id){
$ism = file_get_contents("base/$id.name.db");
$surname = file_get_contents("base/$id.surname.db");
$number = file_get_contents("base/$id.number.db");
$age = file_get_contents("base/$id.age.db");
$refuge = file_get_contents("base/$id.refuge.db");
bot('sendMessage',[
'chat_id'=>$id,
'message_id'=>$mid,
'parse_mode'=>"html",
'text'=>$matn,
'reply_to_message_id'=>$mid,
]);
}
function editMessageText(
        $chatId,
        $messageId,
        $text,
        $parseMode = null,
        $disablePreview = false,
        $replyMarkup = null,
        $inlineMessageId = null
    ) {
       return bot('editMessageText', [
            'chat_id' => $chatId,
            'message_id' => $messageId,
            'text' => $text,
            'inline_message_id' => $inlineMessageId,
            'parse_mode' => $parseMode,
            'disable_web_page_preview' => $disablePreview,
            'reply_markup' => $replyMarkup,
        ]);
    }
function ACL($callbackQueryId, $text = null, $showAlert = false)
{
     return bot('answerCallbackQuery', [
        'callback_query_id' => $callbackQueryId,
        'text' => $text,
        'show_alert'=>$showAlert,
    ]);
}
function delete($id){
bot('deleteMessage',[
'chat_id'=>$id,
'message_id'=>$mid,
]);
}
$update = json_decode(file_get_contents('php://input'));
$message = $update->message;
$mid = $message->message_id;
$name = $message->from->first_name;
$message_id=$message->message_id;
$cid = $message->chat->id;
$replytx = $message->reply_to_message->text;
$update = json_decode(file_get_contents('php://input'));
$message = $update->message;
$from_id = $message->from->id;
$user = $message->from->username;
$chat_id = $message->chat->id;
$text = $message->text;
$cid = $message->chat->id;
$uid= $message->from->id;
$cqid = $update->callback_query->id;
$ccid = $update->callback_query->message->chat->id;
$cuid = $update->callback_query->message->from->id;
$type = $message->chat->type;
$mid = $message->message_id;
$oyatillo = $message->from->message_id;
$oyatillo2 = $message->from->chat->message_id;
$oyatillo3 = $message->chat->message_id;
$chat_id2 = $update->callback_query->message->chat->id;
$message_id2 = $update->callback_query->message->message_id;
$cuseri = $update->callback_query->message->chat->username;
$message_id2 = $update->callback_query->message->message_id;
$data = $update->callback_query->data;
$ci = $message->username;
$fromid = $message->from->id;
$ctitle = $update->message->chat->title;
$cname = $update->message->chat->username;
$groupcid = $update->message->chat->id;
$chanel = $update->channel_post; 
$channeltext = $update->channel_post->text;
$channelmid = $update->channel_post->message_id; 
$channelid = $update->channel_post->chat->id; 
$channelcid = $update->channel_post->chat->id; 
$cid = $message->chat->id;
$mtext = $message->text;
$user = $message->chat->username;
$cidtyp = $message->chat->type;
$miid = $message->message_id;
$tx = $message->text;
$callback = $update->callback_query;
$mmid = $callback->inline_message_id;
$mes = $callback->message;
$mid = $mes->message_id;
$ctext = $mes->text;
$nol = "0";
$status = file_get_contents("base/$cid.status.dat");
$step = file_get_contents("step/$cid.step.dat");
$ism = get("base/$cid.name.dat");
$surname = get("base/$cid.surname.dat");
$number = get("base/$cid.number.dat");
$age = get("base/$cid.age.dat");
$refuge = get("base/$cid.refuge.dat");
function dm($id){
bot('deleteMessage',[
'chat_id'=>$id,
'message_id'=>$mid,
]);
}
$buttons = json_encode([
'inline_keyboard'=>[
[['text'=>"✅ To'g'ri",'callback_data'=> "true"]],
[['text'=>"🚫 Yo'q",'callback_data'=> "false"]],
]
]);
function true($idsi){
$message_id2 = $update->callback_query->message->message_id;
bot('AnswerCallbackQuery',[
'callback_query_id'=>$idsi,
'text'=>"😄 Siz ro'yxatdan muvaffaqiyatli o'tdingiz, tez orada siz bilan mutaxasislarimiz bog'lanishadi!",
'show_alert'=>true,
]);
bot('deleteMessage',[
'chat_id'=>$idsi,
'message_id'=>$message_id2,
]);
bot('deleteMessage',[
'chat_id'=>$idsi,
'message_id'=>$message_id2 - 1,
]);
bot('deleteMessage',[
'chat_id'=>$idsi,
'message_id'=>$message_id2 - 1,
]);
}
function false($idsi){
bot('AnswerCallbackQuery',[
'callback_query_id'=>$idsi,
'text'=>"😕 Afsus, hozir sizni qayta ro'yxatdan o'tish uchun yuboraman! Iltimos botga qayta /start buyrug'ini yuboring!",
'show_alert'=>true,
]);
file_put_contents("base/$idsi.status.dat","false");
bot('deleteMessage',[
'chat_id'=>$ccid,
'message_id'=>$message_id2,
]);
bot('deleteMessage',[
'chat_id'=>$cqid,
'message_id'=>$message_id2 - 1,
]);
delete($idsi);
}
function check($id){
$ism = file_get_contents("base/$id.name.db");
$surname = file_get_contents("base/$id.surname.db");
$number = file_get_contents("base/$id.number.db");
$age = file_get_contents("base/$id.age.db");
$refuge = file_get_contents("base/$id.refuge.db");
bot('sendMessage',[
'chat_id'=>$id,
'message_id'=>$mid,
'parse_mode'=>"html",
'text'=>"😊 Rahmat, <b>$ism </b> siz ro'yxatdan muvaffaqiyatli o'tdingiz barcha ma'lumot to'g'ri ekanini tasdiqlaysizmi?

ℹ️ Ismingiz: <b>$ism ✅</b>

ℹ️ Familyangiz: <b>$surname ✅</b>

ℹ️ Telefon raqamingiz: <b>$number ✅</b>

ℹ️ Yoshingiz: <b>$age ✅</b>

ℹ️ Manzilingiz: <b>$refuge ✅</b>
 
✅ Agar barchasi to'g'ri bo'lsa iltimos «✅ To'g'ri» tugmachasiga bosing. Aks holda «🚫 Yo'q» tugmachasiga bosib qaytadan ro'yxatdan o'tishingiz mumkin!",
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>"✅ To'g'ri",'callback_data'=> "true"]],
[['text'=>"🚫 Yo'q",'callback_data'=> "false"]],
]])
]);
}
if(file_exists("base/users.json")){
get("base/users.json");
} else {
put("base/users.json",$nol);
}
if(file_exists("base/$cid.dat")){
get("base/$cid.dat");
} else {
put("base/$cid.dat","active");
}
if(file_exists("base/$cid.status.dat")){
file_get_contents("base/$cid.status.dat");
} else {
file_put_contents("base/$cid.status.dat","false");
}
if($type=="group" or $type=="supergroup"){
$baza = file_get_contents("base/groups.json");
   if(mb_stripos($baza,$cid) !==false){
   }else{
   $txt="\n$cid";
   $file=fopen("base/groups.json","a+");
   fwrite($file,$txt);
   fclose($file);
   }
}
if($type=="private"){
$baza = file_get_contents("base/users.json");
   if(mb_stripos($baza,$cid) !==false){
   }else{
   $txt="\n$cid";
   $file=fopen("base/users.json","a+");
   fwrite($file,$txt);
   fclose($file);
   }
}
if($data == "true" and $status == "false"){
bot('AnswerCallbackQuery',[
'callback_query_id'=>$cqid,
'text'=>"😄 Siz ro'yxatdan muvaffaqiyatli o'tdingiz, tez orada siz bilan mutaxasislarimiz bog'lanishadi!",
'show_alert'=>true,
]);
bot('deleteMessage',[
'chat_id'=>$ccid,
'message_id'=>$message_id2,
]);
bot('deleteMessage',[
'chat_id'=>$ccid,
'message_id'=>$message_id2 - 1,
]);
bot('deleteMessage',[
'chat_id'=>$ccid,
'message_id'=>$message_id2 - 1,
]);
}
if($data == "false" and $status == "false"){
bot('AnswerCallbackQuery',[
'callback_query_id'=>$cqid,
'text'=>"😕 Afsus, hozir sizni qayta ro'yxatdan o'tish uchun yuboraman! Iltimos botga qayta /start buyrug'ini yuboring!",
'show_alert'=>true,
]);
file_put_contents("base/$idsi.status.dat","false");
bot('deleteMessage',[
'chat_id'=>$ccid,
'message_id'=>$message_id2,
]);
bot('deleteMessage',[
'chat_id'=>$cqid,
'message_id'=>$message_id2 - 1,
]);
delete($ccid);
}
?>