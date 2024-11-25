export const getTotalPriceCart = () => {
    let totalPrice = 0
    document.querySelectorAll('#itemTotalPrice').forEach(field => {
        totalPrice += +field.textContent
    })
    document.querySelector('#totalPrice').textContent = totalPrice
    return totalPrice
}
export const getTotalQuantityCart = () => {
    let totalQuantity = 0
    document.querySelectorAll('#itemQuantity').forEach(field => {
        totalQuantity += +field.value
    })
    document.querySelector('#totalQuantity').textContent = totalQuantity

    if(totalQuantity === 0){
        document.querySelector('.cart__label').textContent = 'Корзина пуста'
        document.querySelector('#totalQuantityHeader').textContent = ''
        document.querySelector('.cart__info').textContent = 'Корзина пуста'
    }
    else{
        document.querySelector('#totalQuantityHeader').textContent = totalQuantity
    }

    return totalQuantity
}
export const clearCart = async(item) => {
    const response = await fetch('/cart/clear_cart/')
    const result = await response.json()
    if(result === 200){
        document.querySelector('.cart .cart__list').replaceChildren()
        getTotalPriceCart()
        getTotalQuantityCart()
    }
}
export const getItemPrice = (event) => {
    const row = event.target.parentNode.parentNode
    const itemPrice = row.querySelector('#itemPrice').textContent
    const itemTotalPrice = row.querySelector('#itemTotalPrice')
    itemTotalPrice.textContent = +itemPrice * +event.target.value
    getTotalPriceCart()
    getTotalQuantityCart()
}
export async function saveCartInSession(event){
    const cartObjects = {
        itemId: event.target.parentNode.parentNode.parentNode.id,
        itemQuantity: event.target.value
    }
    const response = await fetch('/cart/update_cart_session/', {
        method: 'post',
        headers: {
            'Content-Type': 'application/json;charset=urf-8'
        },
        body: JSON.stringify(cartObjects)
    })
}
export const removeItem = async(item) => {
    const response = await fetch(`/cart/remove_item/${item.id}/`)
    const result = await response.json()
    if(result === 200){
        item.remove()
        getTotalPriceCart()
        getTotalQuantityCart()
    }
}