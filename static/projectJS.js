const activePge = window.location.href;

const navList = document.querySelectorAll('nav a').
forEach(link => {
    if(link.href == activePge){
        link.classList.add('active');
    }
});

function comboFunction(object) {
    const comboElement = document.getElementById('combo-div');
    const selcetOption = object.value;
    if(selcetOption === 'בית עסק לפי מיקום') {
        comboElement.innerHTML = '<p>הגדר טווח חיפוש רצוי:  </p> <input type="range" min="1" max="20" class="slider" id="myRange" value="1" oninput="this.nextElementSibling.value = this.value"> Km <output> 1</output><p><button id="submit" type="submit">יאללה תמצאו לי</button></p> '
    }
    else {
        comboElement.innerHTML = '<button id="search" type="submit">חפש</button> <input type="text" class="InputBox" placeholder="הכנס מקום בילוי רצוי..." id="searchInput" name="searchInput" autocomplete="on" required/>  <br>'
    }
}


// ################## ProfileHTML page ################## //
let deleteOnlyOne = true;

const blinkingStars = (starElement) => {
if(deleteOnlyOne===true){
 deleteAllStars();
 deleteOnlyOne=false;   
}
const element = document.getElementById(starElement)
element.classList.add("checked");
if(starElement=== "star1"){
    deleteOnlyOne= true;
    return;
}
if(starElement=== "star2") {
  blinkingStars("star1");  
}
if(starElement=== "star3"){
  blinkingStars("star2"); 
}
if(starElement=== "star4"){
   blinkingStars("star3"); 
}
if(starElement=== "star5"){
   blinkingStars("star4");
 }
}

const deleteAllStars = () => {
    const star1 = document.getElementById("star1")
    const star2 = document.getElementById("star2")
    const star3 = document.getElementById("star3")
    const star4 = document.getElementById("star4")
    const star5 = document.getElementById("star5")
    star1.classList.remove("checked");
    star2.classList.remove("checked");
    star3.classList.remove("checked");
    star4.classList.remove("checked");
    star5.classList.remove("checked");
}


// ################## BS in beer sheva page ################## //
const setImgBorderOnHover = (img) => {
    img.style = "border-style: groove; border-color: #ffcf66; border-width: 7px; border-radius: 20px;";
}

const setImgBorderOffHover = (img) => {
    img.style = "border-width: 0px;";
}






// ################## connect_page_validation ################## //

//check failed password reason
function checkPwd(str) {
    if (str.length < 6) {
        return("סיסמה קצרה מדי");
    } else if (str.length > 20) {
        return("סיסמה ארוכה מדי");
    } else if (str.search(/\d/) == -1) {
        return("צריך לפחות ספרה אחת בסיסמה");
    } else if (str.search(/[A-Z]/) == -1) {
        return("צריך אות גדולה בסיסמה");
    }else if (str.search(/[a-z]/) == -1) {
        return("צריך אות קטנה בסיסמה");
    } else if (str.search(/[^a-zA-Z0-9\!\@\#\$\%\^\&\*\(\)\_\+]/) != -1) {
        return("אסור סימנים מיוחדים בסיסמה");
    }
}

function checkuser(str) {
    if (str.length < 6) {
        return("שם משתמש קצר מדי");
    } else if (str.length > 20) {
        return("שם משתמש ארוך מדי");
    } else if (str.search(/[a-zA-Z]/) == -1) {
        return("שם המשתמש חייב להכיל אותיות");
    } else if (str.search(/[^a-zA-Z0-9\!\@\#\$\%\^\&\*\(\)\_\+]/) != -1) {
        return("אסור סימנים מיוחדים בשם משתמש");
    }
    return('good user')
}


function checkmail(mail){
    {
        if (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(mail))
         {
           return (true)
         }
        return("bad email")
       }
}


function connect_validation(pass,name)
{ 
    //check password
    var passw = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,20}$/;
    if(!pass.value.match(passw)) 
        { 
            alert(checkPwd(pass.value))
            return false;
        }
    
    if(checkuser(name.value)!='good user'){
        alert(checkuser(name.value))
        return false;
    }
}




// ################## sign_up_page_validation ################## //

function signup_validation(pass,name,mail,phone,age)
{
    var passw = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,20}$/;
    if(!pass.value.match(passw)) 
        { 
        alert(checkPwd(pass.value))
        return false;
        }
    
    if(checkuser(name.value)!='good user'){
        alert(checkuser(name.value))
        return false;
        }
    
    if (checkmail(mail.value)=='bad email')
    {
        alert('כתובת המילל אינה תקינה')
        return false;
    }

    var phoneno = /^\d{10}$/;
    if(!phone.value.match(phoneno)){
        alert("המספר צריך לכלול 10 ספרות ורק ספרות");
        return false;
    }
    if(age.value < 18){
        alert("ההרשמה היא מגיל 18 ומעלה");
        return false;
    }
}

// ################## contact_HTML_page_validation ################## //
function contact_validation(mail,phone){
    if (checkmail(mail.value)=='bad email')
    {
        alert('כתובת המילל אינה תקינה')
        return false;
    }
    var phoneno = /^\d{10}$/;
    if(!phone.value.match(phoneno)){
        alert("המספר צריך לכלול 10 ספרות ורק ספרות");
        return false;
    }
}
