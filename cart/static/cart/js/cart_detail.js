import { AcceptDialog, BaseDialog } from "/static/ui.js"
import { createOrderForm, selectTypeOrder } from "./ui.js"
import { clearCart, saveCartInSession, removeItem, getItemPrice } from "./actions.js"

const cart = document.querySelector('.cart')

cart.addEventListener('change', getItemPrice)
cart.addEventListener('change', saveCartInSession)
cart.addEventListener('click', ({target}) => {
    const dialogText = {
        'remove_item': ['Удалить товар из корзины?', removeItem],
        'clear_cart': ['Очистить корзину?', clearCart]
    }
    if(['remove_item', 'clear_cart'].includes(target.dataset.id)){
        const dialog = new AcceptDialog(dialogText[target.dataset.id][0], dialogText[target.dataset.id][1], target.parentNode)
        dialog.show()
    }
    else if(target.dataset.id === 'place_order'){
        let dialog;
        switch(user){
            case 'AnonymousUser':
                dialog = new BaseDialog(selectTypeOrder())
                break
            default:
                dialog = new BaseDialog(createOrderForm(orderForm))
        }
        dialog.show()
    }
})