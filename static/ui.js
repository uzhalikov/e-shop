export class BaseDialog{
    constructor(text){
        let dialog = document.querySelector('dialog')
        dialog = dialog ? dialog.remove() : null
        this.element = document.createElement('dialog')
        this.element.innerHTML = `<div style="padding: 5px; text-align: center;">${text}</div><span id='dialog_close' title="Закрыть окно" style='color:red; cursor: pointer; position: absolute; right: 5px; top: 5px; font-family: Arial, sans-serif;' class="dialog_close">X</span>`
        this.text = text
        this.element.style.left = '50%'
        this.element.style.top = '50%'
        this.element.style.transform = 'translate(-50%, -50%)'
        this.element.style.borderRadius = '10px'
        this.element.style.left = '50%'
    }
    show(){
        document.body.appendChild(this.element)
        this.element.showModal()
    }
}

export class AcceptDialog extends BaseDialog{
    constructor(text, func, aim){
        super(text)
        this.aim = aim
        this.func = func
        this.element.innerHTML += `
        <style>
            .accept-dialog{
                padding: 10px; text-align: center;
            }
            .accept-dialog__text{
                padding: 5px 0;
            }
            .accept-dialog__actions{
                display: flex;
                justify-content: center;
                gap: 10px;
            }
            .accept-dialog__button{
                padding: 5px;
                border-radius: 5px;
                border: 1px solid;
                cursor: pointer;
                transition: 0.5s;
                width: 100px;
            }
            .accept-dialog__button:hover{
                transition: 0.5s;
                background: rgba(142, 179, 247, 0.541);
            }
        </style>
        <div class="accept-dialog">
            <div class="accept-dialog__actions">
                <span class="accept-dialog__button" id="accept">Подтвердить</span>
                <span class="accept-dialog__button" id="decline">Отмена</span>
            </div>
        </div>`

        
        this.element.querySelector('#accept').onclick = () => this.handleEnterClick()
        this.element.querySelector('#decline').onclick = () => this.handleDeclineClick()
    }
    handleEnterClick(){
        this.func(this.aim)
        this.handleDeclineClick()
    }
    handleDeclineClick(){
        this.element.remove()
    }
}