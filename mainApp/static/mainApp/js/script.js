"use strict"

let header_burger = document.querySelector(".header__burger");
let header_phone_menu = document.querySelector(".header__phone_menu")
// let header__phone_menu_trasplate = document.querySelector(".header__phone_menu_trasplate")
let header__phone = document.querySelector(".header__phone")
let header__cross = document.querySelector(".header__cross")



header_burger.addEventListener("click", function(event){
    header_burger.classList.toggle("_active")
    // header_phone_menu.classList.toggle("_active")
    // header__phone_menu_trasplate.classList.toggle("_active")
    document.body.classList.toggle("_lock")
    header__phone.classList.toggle("_lock")
    header_phone_menu.classList.toggle("_active")
})

header__cross.addEventListener("click", function(event){
    header_burger.classList.toggle("_active")
    // header_phone_menu.classList.toggle("_active")
    // header__phone_menu_trasplate.classList.toggle("_active")
    document.body.classList.toggle("_lock")
    header__phone.classList.toggle("_lock")
    header_phone_menu.classList.toggle("_active")
})