"use strict"

let anchors = document.querySelectorAll('a[href*="#"]:not([href="#"])')


for (let anchor of anchors){
    anchor.addEventListener("click", function(event){
        event.preventDefault()
        const blockID = anchor.getAttribute('href').substr(1)
        
        document.getElementById(blockID).scrollIntoView({
            behavior: "smooth",
            block: "start",
        })
    })
}