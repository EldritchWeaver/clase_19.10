/*
 * EJERCICIO 1 
 * PROGRAMA MUESTRA TODOS LOS NÚMEROS IMPARES INTRODUCIDOS ENTRE DOS NÚMEROS POR EL USUARIO
 */


var numeroUno = prompt("Introduzca el primer numero: ", 0);
var numeroDos = prompt("Introduzca el segundo numero: ", 0);

numeroUno = parseInt(numeroUno);
numeroDos = parseInt(numeroDos);


if (numeroUno > numeroDos) {

    let n = numeroUno;
    numeroUno = numeroDos;
    numeroDos = n;

}

document.write('<ul>');

for (let i = numeroUno; i <= numeroDos; i++) {

    if (impar(i)) {

        console.log("El número " + i + " es impar.");
        document.write('<li>' + 'El número ' + i + ' es impar.' + '</li>');

    } /* else {

        console.log("El número " + i + " es par.");
        document.write('<li>' + 'El número ' + i + ' es par.' + '</li>');
        
    } */  // <-- eso no lo pidieron :> 
}

document.write('</ul>');

function impar(i) {
    return i % 2 !== 0;
}
