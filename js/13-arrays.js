var nombre = "Jenny";
var profesores = ['Juan', 'Pedro', 'María', 'Pedro', 'Rosita'];
var materias = ['Matemáticas', 'Lengua', 'Íngles'];

console.log(profesores[2]);
console.log(profesores.length); //Muestra el numero de elementos o "longitud" del array

//Metodos para trabajar con texto:
console.log(nombre.toUpperCase());
console.log(nombre.toLowerCase());

/* ------------------------------------------------------------ */

document.write('<h1  class="lol"> Ejercicios de Arrays </h1>');

/* ------------------------------------------------------------ */

document.write('<ul>');

materias.forEach((element, indice, arr) => {

    document.write('<li>' + indice + ' ' + element + '</li>');

});

document.write('</ul>');

/* ------------------------------------------------------------ */

document.write('<hr>');

/* ------------------------------------------------------------ */

document.write('<ul>');

profesores.forEach((element, indice, arr) => {

    document.write('<li>' + indice + ' ' + element + '</li>');

});

document.write('</ul>');

/* ----------------------------------------------------------- */