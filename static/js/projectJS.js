const activePge = window.location.href;

const markCurrentPage = () => {
    document.querySelectorAll("nav a").forEach((currElement) => {
        if (currElement.href.includes(`${window.location.pathname}`)) {
            currElement.classList.add("active");
        }
    });
};





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
