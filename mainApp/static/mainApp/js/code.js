
let page_code = document.querySelector(".page__code")
let code_submit = document.querySelector(".code__submit")
let page = document.querySelector(".page__title")

code_submit.addEventListener('click', function(event){
    let code = page_code.value
    let data = new FormData();
    data.append('inputCode', code)

    axios.post('/activate', data)
        .then(res => {
            console.log(res)
            let new_data = res.data
            if (new_data['OK'] == 'true'){
                userForm = new_data['userForm']
                let dataLogin = new FormData();
                dataLogin.append('loginUser', "true")

                axios.post('/confirmReg', dataLogin)
                .then(res => {
                    window.location.href = '/'
                })
                .catch(err => {
                    console.error(err);
                })
            

            }
            if(new_data['OK'] == 'false'){
                let errorDiv = document.createElement('div')
                error = 'invalid Code'
                errorDiv.innerHTML = '<div class="code__errors">' + error + '</div>'
                if(!document.querySelectorAll('.code__error')){
                    page.appendChild(errorDiv)
                }
                
            }
            
        })
        .catch(err => {
            console.error(err);
        })
    
})

