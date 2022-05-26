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
        comboElement.innerHTML = '<p>הגדר טווח חיפוש רצוי:  </p> <input type="range" min="1" max="20" class="slider" id="myRange" value="1" oninput="this.nextElementSibling.value = this.value"> Km <output> 1</output><p><button id="submit" type="submit">יאללה תמצאו לי</button></p>'
    }
    else {
        comboElement.innerHTML = '<button id="search" type="submit">חפש</button> <input type="text" class="InputBox" placeholder="הכנס מקום בילוי רצוי..." id="searchInput" name="searchInput" autocomplete="on" required/>  <br>'
    }
}

