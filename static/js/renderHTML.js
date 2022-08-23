/*Renderizamos el archivo HTML*/
function renderTag(tags) {
  const table = document.querySelector("#table__body");
  table.innerHTML = "";
  tags.forEach((tag) => {
      const fila = document.createElement("tr");
      fila.classList.add("table__row");
      fila.innerHTML = `
      <td class="table__td--negrita">${tag.id}</td>
          <td>${tag.name}</td>
          <td class="table__td-actions" width="200">
            <ul class="table__actions">
            <button class="table__button">
              <li class="table__action table__action--delete">Delete</li>
            </button>
            </ul>
          </td>`;

  table.appendChild(fila);
    });
}


function renderProduct(tags) {
  const table = document.querySelector("#table__body");
  table.innerHTML = "";
  tags.forEach(async (tag) => {
      const fila = document.createElement("tr");
      fila.classList.add("table__row");

      const resMark = await fetch(`/api/mark/${tag.id_mark}`);
      let nameMark = await resMark.json();
      nameMark = nameMark["Mark:"]["name"];

      const resCategory = await fetch(`/api/category/${tag.id_category}`);
      let nameCategory = await resCategory.json();
      nameCategory = nameCategory["Category:"]["name"];

      fila.innerHTML = `
      <td class="table__td--negrita">${tag.id}</td>
          <td>${tag.name}</td>
          <td>${tag.price}</td>
          <td>${nameCategory}</td>
          <td>${nameMark}</td>
          <td class="table__td-actions" width="200">
            <ul class="table__actions">
            <button class="table__button">
              <li class="table__action table__action--delete">Delete</li>
            </button>
            </ul>
          </td>`;

  table.appendChild(fila);
    });
}


export { renderTag, renderProduct };