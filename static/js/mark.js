/*Archivos importados*/
import {renderTag} from './renderHTML.js';

/*Formulario*/
const markForm = document.querySelector("#markForm");

/*Pantalla de carga*/
window.addEventListener("DOMContentLoaded", () =>{
	deleteTag();
});

/*Crear nueva categoria*/
markForm.addEventListener("submit", async (e) =>{
	e.preventDefault();
	const name = markForm["name"].value;

	const response = await fetch("/api/mark", {
		method : "POST",
		headers : {
			"Content-Type" : "Application/json"
		},
		body : JSON.stringify({
			name
		})
	})

	const data = await response.json();
	writeMessage(data["New mark:"]);
	readMark();
	deleteTag();
	markForm.reset();
});


/*Leer todas las categorias*/
async function readMark() {
	const response = await fetch("/api/mark");
	const data = await response.json();
	const marks = data["Marks:"];
	renderTag(marks);
}

/*Eliminar categoria*/
async function deleteTag(){
	await readMark();
	const btnDelete = document.querySelectorAll(".table__action--delete");
	const rows = document.querySelectorAll(".table__row");
	btnDelete.forEach((btn, index) =>{
		btn.addEventListener("click", async (e) => {
			const id = rows[index].firstElementChild.textContent;
			const response = await fetch(`/api/mark/${id}`, {method: "DELETE",});
			const data = await response.json();
			writeMessage(data["Message"]);
			deleteTag();
		})
	})
}