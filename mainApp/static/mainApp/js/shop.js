"use strict"

let header_burger = document.querySelector(".header__burger");
let header_phone_menu = document.querySelector(".header__phone_menu")
let header__phone = document.querySelector(".header__phone")
let header__cross = document.querySelector(".header__cross")
let header_blockout = document.querySelector(".header__blockout")
let header__line = document.querySelector(".header__line")
let header__body = document.querySelector(".header__body")
let header_login = document.querySelector(".header__login")
let header_login_logo = document.querySelector(".header__login_logo")

let wrapper__block_app_menus = document.querySelector(".wrapper__block_app_menus")
let blockout__app_menus = document.querySelector(".blockout__app_menus")
let login__block = document.querySelector(".login__block")
let header__basket_logo = document.querySelector(".header__basket_logo")
let basket__block = document.querySelector(".basket__block")

header_burger.addEventListener("click", function (event) {
    getActive(event)
})

header__cross.addEventListener("click", function (event) {
    getActive(event)
})

header_blockout.addEventListener("click", function (event) {

    if (wrapper__block_app_menus.classList.contains("_login")) {
        wrapper__block_app_menus.classList.toggle("_login")
        document.body.classList.toggle("_lock")
        header_blockout.classList.toggle("_active")


    } else if (wrapper__block_app_menus.classList.contains("_basket")) {
        wrapper__block_app_menus.classList.toggle("_basket")
        document.body.classList.toggle("_lock")
        header_blockout.classList.toggle("_active")
        basket__block.classList.toggle("_active")


    } else {
        getActive(event)
    }

})



header_login_logo.addEventListener("click", function (event) {
    if(!wrapper__block_app_menus.classList.contains("_basket")){
        wrapper__block_app_menus.classList.toggle("_login")
        header_blockout.classList.toggle("_active")
        document.body.classList.toggle("_lock")
    }

})
header__basket_logo.addEventListener("click", function (event) {
    if(!wrapper__block_app_menus.classList.contains("_login")){
        wrapper__block_app_menus.classList.toggle("_basket")
        header_blockout.classList.toggle("_active")
        document.body.classList.toggle("_lock")
        basket__block.classList.toggle("_active")
    }

})


// blockout__app_menus.addEventListener("click", function (event) {
//     if (wrapper__block_app_menus.classList.contains("_login")) {
//         wrapper__block_app_menus.classList.toggle("_login")
//         document.body.classList.toggle("_lock")

//     }
//     if(wrapper__block_app_menus.classList.contains("_basket")){
//         wrapper__block_app_menus.classList.toggle("_basket")
//         document.body.classList.toggle("_lock")

//     }
// })

function getActive(event) {
    header_burger.classList.toggle("_active")
    document.body.classList.toggle("_lock")
    header__phone.classList.toggle("_lock")
    header_phone_menu.classList.toggle("_active")
    header_blockout.classList.toggle("_active")
    header__line.classList.toggle("_lock")
    header__body.classList.toggle("_lock")

}

