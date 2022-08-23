/*Archivos importados*/
import {renderTag} from './renderHTML.js';

/*Formulario*/
const categoryForm = document.querySelector("#categoryForm");

/*Pantalla de carga*/
window.addEventListener("DOMContentLoaded", () =>{
	deleteTag();
});

/*Crear nueva categoria*/
categoryForm.addEventListener("submit", async (e) =>{
	e.preventDefault();
	const name = categoryForm["name"].value;

	const response = await fetch("/api/category", {
		method : "POST",
		headers : {
			"Content-Type" : "Application/json"
		},
		body : JSON.stringify({
			name
		})
	})

	const data = await response.json();
	writeMessage(data["New category:"]);
	readCategories();
	deleteTag(); //Cargar la tabla.
	categoryForm.reset();
});


/*Leer todas las categorias*/
async function readCategories() {
	const response = await fetch("/api/category");
	const data = await response.json();
	const categories = data["Categories:"];
	renderTag(categories);
}

/*Eliminar categoria*/
async function deleteTag(){
	await readCategories();
	const btnDelete = document.querySelectorAll(".table__action--delete");
	const rows = document.querySelectorAll(".table__row");
	btnDelete.forEach((btn, index) =>{
		btn.addEventListener("click", async (e) => {
			const id = rows[index].firstElementChild.textContent;
			const response = await fetch(`/api/category/${id}`, {method: "DELETE",});
			const data = await response.json();
			writeMessage(data["Message"]);
			deleteTag();
		})
	})
}