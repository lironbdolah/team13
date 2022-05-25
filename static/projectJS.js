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


