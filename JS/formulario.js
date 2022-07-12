const nombre = document.getElementById("nombre");
const apellido = document.getElementById("apellido");
const email = document.getElementById("email");
const telefono = document.getElementById("telefono");
const comentarios = document.getElementById("comentarios");
const file = document.getElementById("file");
const form = document.getElementById("form");
const parrafo = document.getElementById("warnings");

form.addEventListener("submit", (e) => {
  e.preventDefault();
  let warnings = "";
  let entrar = false;
  let regexEmail = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+$/;
  parrafo.innerHTML = "";
  if (nombre.value.length < 4) {
    warnings += `El nombre no es válido <br>`;
    entrar = true;
  }
  if (apellido.value.length < 4) {
    warnings += `El apellido no es válido <br>`;
    entrar = true;
  }
  if (comentarios.value.length < 4) {
    warnings += `La descripción no es válido <br>`;
    entrar = true;
  }
  if (telefono.value.length < 10) {
    warnings += `El teléfono no es válido <br>`;
    entrar = true;
  }
  // console.log(regexEmail.test(email.value));
  if (!regexEmail.test(email.value)) {
    warnings += `El email no es válido <br>`;
    entrar = true;
  }
  if (entrar) {
    parrafo.innerHTML = warnings;
  } else {
    parrafo.innerHTML =
      "Sus datos con su consulta han sido enviadas <br> Le contestaremos a la brevedad";
  }
});
