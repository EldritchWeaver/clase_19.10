/*
 * EJECICIO 3 
 * PROGRAMA QUE IMPRIMA LA TABLA DE MULTIPLICAR DE UN NÚMERO INGRESADO POR EL USUARIO
 */

var numero = prompt("Introduzca un numero: ", 0);
numero = parseInt(numero);


document.write('<h1> Tabla de Multiplicar del ' + numero + '</h1>');
console.log("Tabla de Multiplicar del " + numero);


document.write('<ul>');

for (let i = 0; i <= 10; i++) {

    console.log(numero + " x " + i + " = " + multiplicar(numero, i));
    document.write('<li>' + numero + ' x ' + i + ' = ' + multiplicar(numero, i) + '</li>');
    
}

document.write('</ul>');


function multiplicar(numero, i) {
    return numero * i;
}