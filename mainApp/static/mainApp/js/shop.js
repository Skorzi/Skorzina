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

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"

let forms = document.querySelectorAll(".product__price")
let basket_goods_all = document.getElementById("basket__goods_all")
let basket_delete_buttons = document.querySelectorAll(".basket__delete_good")

for (let form = 0; form < forms.length; form++) {
    forms[form].addEventListener("click", function (event) {
        event.preventDefault()
        let data = new FormData();
        // forms[form].querySelector('.add').value
        data.append("id", forms[form].parentNode.getAttribute("product_id"));
        data.append("add_item", "true");
        axios.post('basket_add', data)
            .then(res => {

                let new_data = res.data

                for (let id in new_data) {

                    let cost = new_data[id]['cost']
                    let photo = new_data[id]['photo']

                    if (!document.getElementById(id)) {
                        basket__goods_all.innerHTML += '<div class="basket__goods" id=' + id + '><div class="basket__image"><img src=' + '/media/' + photo + '></div>' + '<div class="basket__cost_of_good">' + cost + '</div><button class="basket__delete_good"><div class="delete_good_cross_1"></div><div class="delete_good_cross_2"></div><div class="delete_good_cross_3"></div></button></div>'
                        basket_delete_buttons = document.querySelectorAll('.basket__delete_good')
                        submitDelForm()
                    }

                }
                if (!wrapper__block_app_menus.classList.contains("_login")) {
                    wrapper__block_app_menus.classList.toggle("_basket")
                    header_blockout.classList.toggle("_active")
                    document.body.classList.toggle("_lock")
                    basket__block.classList.toggle("_active")
                }
            })
            .catch(err => {
                console.error(err);
            })

    })
}

function submitDelForm() {
    for (let i = 0; i < basket_delete_buttons.length; i++) {
        basket_delete_buttons[i].addEventListener('click', function (event) {
            event.preventDefault()
            let data = new FormData()
            let id = basket_delete_buttons[i].parentNode.getAttribute("id")
            data.append("id", id)
            data.append("remove_item", "true")
            axios.post("basket_remove", data)
            .then(res => {
                document.getElementById(id).remove()
            })
            .catch(err => {
                console.error(err); 
            })
        })
    }
}


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
    if (!wrapper__block_app_menus.classList.contains("_basket")) {
        wrapper__block_app_menus.classList.toggle("_login")
        header_blockout.classList.toggle("_active")
        document.body.classList.toggle("_lock")
    }

})
header__basket_logo.addEventListener("click", function (event) {
    if (!wrapper__block_app_menus.classList.contains("_login")) {
        wrapper__block_app_menus.classList.toggle("_basket")
        header_blockout.classList.toggle("_active")
        document.body.classList.toggle("_lock")
        basket__block.classList.toggle("_active")
    }

})


function getActive(event) {
    header_burger.classList.toggle("_active")
    document.body.classList.toggle("_lock")
    header__phone.classList.toggle("_lock")
    header_phone_menu.classList.toggle("_active")
    header_blockout.classList.toggle("_active")
    header__line.classList.toggle("_lock")
    header__body.classList.toggle("_lock")

}

submitDelForm();