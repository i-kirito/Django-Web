function bg_change(){
    bg=document.getElementById('header');
    if(bg.style.backgroundImage==""){
        bg.style.backgroundImage="url(../static/image/logo.png)";
    }else{
        bg.style.backgroundImage="";
    }
}