function comboFunction(object) {
    const elemet = document.getElementById("msg_for_user");
    if (elemet) {
        elemet.innerHTML = "";
    }
    const comboElement = document.getElementById('combo-div');
    const selcetOption = object.value;
    console.log(selcetOption)
    if (selcetOption === "בית עסק לפי מיקום") {
        // comboElement.innerHTML = '<form id="combo_box" onsubmit="preventDefault(); sendMyLocation(this);"> <p>הגדר טווח חיפוש רצוי:  </p> <input type="range" name=userRange min="1" max="20" class="slider" id="myRange" value="1" oninput="this.nextElementSibling.value = this.value"> Km <output> 1</output><p><input id="submit-range" type="submit" value="יאללה תמצאו לי"></input></p></form>'
        comboElement.innerHTML = '<form id="combo_box"  method="post" onsubmit="event.preventDefault(); return sendMyLocation(this);"> <p>הגדר טווח חיפוש רצוי:  </p> <input type="range" name=userRange min="1" max="20" class="slider" id="myRange" value="1" oninput="this.nextElementSibling.value = this.value"> Km <output> 1</output><p><button id="submit" type="submit">יאללה תמצאו לי</button></p></form>'
    } else if (selcetOption === "בית עסק להמשך היום") {
        comboElement.innerHTML = '<form id="combo_box" action="/profile/futureSearch" method="get"><p>בחר עיר לבילוי עתידי: </p><select name="combo1" id="combo1" required><option value="" selected disabled hidden>בחר עיר:</option><option value="באר שבע"> באר שבע</option></select><br><p>בחר שעה רצויה: </p><select name="combo2" id="combo2" required><option value="" selected disabled hidden>בחר שעה:</option><option value="17:00-18:00"> 17:00-18:00</option><option value="18:00-19:00"> 18:00-19:00</option><option value="19:00-20:00"> 19:00-20:00</option><option value="20:00-21:00"> 20:00-21:00</option><option value="21:00-22:00"> 21:00-22:00</option></select><br><br><button id="submit2" type="submit2">יאללה תמצאו לי</button></p></form>'
    } else {
        comboElement.innerHTML = '<form id="combo_box" action="/profile/searchInput" method="get"><button id="search" type="submit"></a>חפש</button> <input type="text" class="InputBox" placeholder="הכנס מקום בילוי רצוי..." id="searchInput" name="searchInput" autocomplete="on" required/></form>  <br>'
    }
}

const submitHome = (searchInput) => {
    console.log(searchInput)
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
            .then(response => response.text())
            .then(htmlFile => {
                // var parser = new DOMParser();
                // var doc = parser.parseFromString(htmlFile, "text/html");
                document.body.innerHTML = htmlFile;
            })
            .catch(err => console.log(err)
            )
    }
}