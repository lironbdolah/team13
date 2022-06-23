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
    console.log(selcetOption)
    if(selcetOption === "בית עסק לפי מיקום") {
        // comboElement.innerHTML = '<form id="combo_box" onsubmit="preventDefault(); sendMyLocation(this);"> <p>הגדר טווח חיפוש רצוי:  </p> <input type="range" name=userRange min="1" max="20" class="slider" id="myRange" value="1" oninput="this.nextElementSibling.value = this.value"> Km <output> 1</output><p><input id="submit-range" type="submit" value="יאללה תמצאו לי"></input></p></form>'
        comboElement.innerHTML = '<form id="combo_box"  method="post" onsubmit="event.preventDefault(); return sendMyLocation(this);"> <p>הגדר טווח חיפוש רצוי:  </p> <input type="range" name=userRange min="1" max="20" class="slider" id="myRange" value="1" oninput="this.nextElementSibling.value = this.value"> Km <output> 1</output><p><button id="submit" type="submit">יאללה תמצאו לי</button></p></form>'
    }
    else if(selcetOption === "בית עסק להמשך היום"){
        comboElement.innerHTML = '<form id="combo_box" action="/profile/futureSearch" method="get"><p>בחר עיר לבילוי עתידי: </p><select name="combo1" id="combo1"><option value="" selected disabled hidden>בחר עיר:</option><option value="באר שבע"> באר שבע</option></select><br><p>בחר שעה רצויה: </p><select name="combo2" id="combo2"><option value="" selected disabled hidden>בחר שעה:</option><option value="17:00-18:00"> 17:00-19:00</option><option value="17:00-18:00"> 19:00-21:00</option><option value="17:00-18:00"> 21:00-23:00</option></select><br><br><button id="submit2" type="submit2">יאללה תמצאו לי</button></p></form>'
    }
    else {
        comboElement.innerHTML = '<form id="combo_box" action="/profile/searchInput" method="get"><button id="search" type="submit"></a>חפש</button> <input type="text" class="InputBox" placeholder="הכנס מקום בילוי רצוי..." id="searchInput" name="searchInput" autocomplete="on" required/></form>  <br>'
    }
}

const sendMyLocation = (locationForm) => {
    let positionObject;

    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition);
    } else {
        console.log("Geolocation is not supported by this browser.")
    }

    function showPosition(position) {
        positionObject = {
            latitude: position.coords.latitude,
            longitude: position.coords.longitude,
            userRange: locationForm.userRange.value 
        }
        console.log("positionObject =>", positionObject);
        fetch('http://127.0.0.1:5000/profile/by-location',
            {
                method: "POST",
                headers: {"Content-Type": "application/json;charset=utf-8"},
                body: JSON.stringify(positionObject)
            })
            .then(response =>  console.log(response.data))
            .catch(err => console.log(err)
    )
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

const submitReview = () => {
    const textValue = document.getElementById("write")?.value;
    const numOfStars = getNumOfStars("stars-2");
    
    const submitObject = {
        textValue: textValue,
        numOfStars: numOfStars
    }

    fetch('http://127.0.0.1:5000/profile/rank',
        {
            method: "POST",
            headers: {"Content-Type": "application/json;charset=utf-8"},
            body: JSON.stringify(submitObject)
        })
        .then(res => console.log(res))
        .catch(e => console.log(e))
}

const getNumOfStars = (divId) => {
    let numOfStars = 0;
    const starsElement = document.getElementById(divId).getElementsByTagName("*");;

    for(var i = 0; i < starsElement.length; i++){
        if(starsElement[i]?.classList.contains("checked")){
            numOfStars++;
        }
    }

    return numOfStars;
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
        return(" שם המשתמש חייב להכיל אותיות באנגלית בלבד");
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
        alert('כתובת המייל אינה תקינה, עליה להיות בפורמט xxx@yyy.zzz, כאשר הסיומת יכולה להכיל 2 או 3 אותיות')
        return false;
    }

    var phoneno = /^\d{10}$/;
    if(!phone.value.match(phoneno)){
        alert("המספר טלפון צריך לכלול 10 ספרות ורק ספרות");
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
        alert('כתובת המייל אינה תקינה, עליה להיות בפורמט xxx@yyy.zzz, כאשר הסיומת יכולה להכיל 2 או 3 אותיות')
        return false;
    }
    var phoneno = /^\d{10}$/;
    if(!phone.value.match(phoneno)){
        alert("המספר טלפון צריך לכלול 10 ספרות ורק ספרות");
        return false;
    }
}
