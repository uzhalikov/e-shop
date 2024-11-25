import { BaseDialog } from "./ui.js"
import { getCookie } from "./utils.js"
import { clearCart } from "/static/cart/js/actions.js"
import { successOrder, createQuickOrderForm } from "/static/cart/js/ui.js"
import { createUserRegForm, createUserAuthForm } from "/static/users/js/ui.js"

document.addEventListener('click', (event) => {
    let dialog;
    if(event.target.id === 'dialog_close'){
        document.querySelector('dialog').remove()
    }
    else if(event.target.id === 'enter'){
        dialog = new BaseDialog(createUserAuthForm(userAuthForm))
        dialog.show()
    }
    else if(event.target.id === 'order_one_click'){
        dialog = new BaseDialog(createQuickOrderForm(quickOrderForm))
        dialog.show()
    }
    else if(event.target.id === 'register'){
        document.querySelector('dialog').children[0].innerHTML = createUserRegForm(userRegForm)
    }
})
document.addEventListener('submit', (event) => {
    if(['auth', 'quick_order', 'user_reg', 'base_order', 'user_auth'].includes(event.target.id)){
        event.preventDefault()
        const data = new FormData(event.target)
        data.append('csrfmiddlewaretoken', getCookie('csrftoken'))

        const urls = {
            'user_auth': '/users/login/',
            'quick_order': '/orders/create/?&quick=True/',
            'user_reg': '/users/register/',
            'base_order': '/orders/create/',
        }

        fetch(urls[event.target.id], {body: data, method: 'post'})
        .then(response => response.json())
        .then(result => {
            switch(event.target.id){
                case 'auth':
                    switch(result){
                        case 200: location.reload()
                        break
                        default: event.target.querySelector('.form__error').textContent = 'Неверный логин или пароль'
                    }
                    break
                case 'quick_order':
                case 'base_order':
                    switch(result){
                        case 200:
                            event.target.outerHTML = successOrder()
                            clearCart()
                            break
                        default: console.log('Ошибка')
                    }
                    break
                default: location.reload()
            }
        })
    }
})