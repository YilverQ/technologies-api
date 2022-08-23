const textMessage = document.querySelector("#message__text");
const message = document.querySelector("#message");
const close_message = document.querySelector("#message__close");


/*Mensajes desde Js*/
function writeMessage(text) {
	textMessage.innerHTML = text; 
	message.classList.remove("disabled");
}

close_message.addEventListener("click", ()=>{
	message.classList.add("disabled");
})