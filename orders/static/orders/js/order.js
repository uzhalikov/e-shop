const orderTotalQuantity = document.querySelector('#order_total_quantity')
const orderTotalPrice = document.querySelector('#order_total_price')

const table = Array.from(document.querySelector('.order table').rows).slice(1)

table.pop()
table.forEach(row => {
    orderTotalQuantity.textContent = +row.cells[1].textContent + +orderTotalQuantity.textContent
    orderTotalPrice.textContent = +row.cells[2].textContent + +orderTotalPrice.textContent
})