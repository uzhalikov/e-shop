export const createUserRegForm = (formData) => {
    return `
    <form id="user_reg" class="form unselect">
        <h3>Регистрация</h3>
        ${formData}
        <button type="submit">Зарегистрироваться</button>
    </form>`
}

export const createUserAuthForm = (formData) => {
    return `
    <form id="user_auth" class="form unselect">
        <h3>Авторизация</h3>
        ${formData}
        <button type="submit">Войти</button>
    </form>`
}