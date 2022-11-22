
console.log("alo");

let btn = document.getElementsByClassName("formulario")
for (let i = 0; i < btn[0].length; i++) {
    btn[0][i].addEventListener("keyup",(e) =>{
        if(e.target.value != "")e.target.parentElement.children[0].style.opacity = "50%";
        if(e.target.value == "")e.target.parentElement.children[0].style.opacity = "100%";
    })
}

