'use strict';

if (typeof(Storage) !== 'undefined') {
    console.log('Local Storage esta disponible');
} else {
    console.log('Local Storage no esta disponible');
};

//Guardar datos
localStorage.setItem("titulo", "Curso de PHP");

//Guardar un elemento de local storage
localStorage.getItem("titulo");

//imprimir en consola de lo que obtuve del local storage
console.log(localStorage.getItem("titulo"));

//Para imprimir en }HTML lo que almacene del local storage
document.querySelector('#curso').innerHTML = localStorage.getItem('titulo');

//Guardar objetos json
var user = {
    nombre: "Gabriel Moreno",
    email: "moreno.gab58@gmail.com",
    web: "EldritchKaiser.org"
};
localStorage.setItem("user", JSON.stringify(user));

/* La forma correcta de almacenar datos en local storage es convirtiendo
 * los objetos en json-string porque no procesa el objeto con JavaScript
 * puro. La forma correcta de enviar informacion a un API se debe hacer
 * igual con json-string.
 */

//Recuperar objetos de local storage

var userjs = JSON.parse(localStorage.getItem("user"));
console.log(userjs);

//Ahora para imprimir en el html
document.querySelector("#alumno").append(" " + userjs.nombre + "  " + userjs.email);

//Vaciar el local storage
localStorage.removeItem("user");
localStorage.clearItem("user");