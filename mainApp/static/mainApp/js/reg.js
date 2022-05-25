"use strict"

let button_reg = document.querySelector(".button_submit_regForm");

let email_field = document.getElementById("id_email")
let username_field = document.getElementById("id_username")
let password1_field = document.getElementById("id_password1")
let password2_field = document.getElementById("id_password2")

email_field.placeholder = "email"
username_field.placeholder = "username"
password1_field.placeholder = "password"
password2_field.placeholder = "confirm password"



// button_reg.addEventListener('click', function(event){
//     let data = new FormData()
//     let email = email_field.value
//     let password1 = password1_field.value
//     let password2 = password2_field.value
//     let name = username_field.value
//     data.append("username", name)
//     data.append("email", email)
//     data.append("password1", password1)
//     data.append("password2", password2)
//     axios.post('/register', data)
//         .then(res => {

//         })
//         .catch(err => {
//             console.error(err); 
//         })
// })
