/*Archivos importados*/
import {renderProduct} from './renderHTML.js';

/*Formulario*/
const productForm = document.querySelector("#productForm");

/*Pantalla de carga*/
window.addEventListener("DOMContentLoaded", () =>{
	deleteTag();
});

/*Crear nueva categoria*/
productForm.addEventListener("submit", async (e) =>{
	e.preventDefault();
	const name = productForm["name"].value;

	const response = await fetch("/api/product", {
		method : "POST",
		headers : {
			"Content-Type" : "Application/json"
		},
		body : JSON.stringify({
			name
		})
	})

	const data = await response.json();
	writeMessage(data["New product:"]);
	readProduct();
	deleteTag();
	productForm.reset();
});


/*Leer todas las categorias*/
async function readProduct() {
	const response = await fetch("/api/product");
	const data = await response.json();
	const product = data["Products:"];
	renderProduct(product);
}

/*Eliminar categoria*/
async function deleteTag(){
	await readProduct();
	const btnDelete = document.querySelectorAll(".table__action--delete");
	const rows = document.querySelectorAll(".table__row");
	btnDelete.forEach((btn, index) =>{
		btn.addEventListener("click", async (e) => {
			const id = rows[index].firstElementChild.textContent;
			const response = await fetch(`/api/product/${id}`, {method: "DELETE",});
			const data = await response.json();
			writeMessage(data["Message"]);
			deleteTag();
		})
	})
}