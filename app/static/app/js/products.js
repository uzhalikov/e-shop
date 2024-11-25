const products = document.querySelector('.products')
let cartLabel = document.querySelector('.cart__label')
let cartLength = document.getElementById('totalQuantityHeader')

async function addProductToCart(productLink){
    const response = await fetch(productLink)
    return await response.json()
}

products.addEventListener('click', (event) => {
    if(event.target.classList.contains('product__buy')){
        event.preventDefault()
        const addProduct = addProductToCart(event.target.href)
        addProduct.then(result => {
            console.log(result)
            cartLength.textContent = Number(cartLength.textContent) + 1
            cartLabel.textContent = 'Корзина: '
            for(let [key, value] of Object.entries(result)){
                const product = document.getElementById(`${key}`)
                if(product){
                    document.getElementById(`${key}`).querySelector('.product__button').children[0].textContent = `Добавлено: ${value.quantity}`
                }
            }
        })
    }
})
