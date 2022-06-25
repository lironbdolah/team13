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
        .then(response => response.text())
        .then(htmlFile => {
            document.body.innerHTML = htmlFile;
        })
        .catch(err => console.log(err)
    )
}

const getNumOfStars = (divId) => {
    let numOfStars = 0;
    const starsElement = document.getElementById(divId).getElementsByTagName("*");

    for(var i = 0; i < starsElement.length; i++){
        if(starsElement[i]?.classList.contains("checked")){
            numOfStars++;
        }
    }

    return numOfStars;
}



