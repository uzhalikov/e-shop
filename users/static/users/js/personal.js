const personal = document.querySelector('#personal')
const orders = document.querySelector('#orders')
const personalData = document.querySelector('.personal__data')
const ordersData = document.querySelector('.user-orders')

personal.addEventListener('click', () => {
    personalData.classList.remove('hidden')
    ordersData.classList.add('hidden')
})

orders.addEventListener('click', () => {
    personalData.classList.add('hidden')
    ordersData.classList.remove('hidden')
    
})