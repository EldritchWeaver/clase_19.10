/*
 * EJECICIO 3 
 * PROGRAMA QUE IMPRIMA LA TABLA DE MULTIPLICAR DE UN NÚMERO INGRESADO POR EL USUARIO
 */

var num = prompt("Introduzca un numero: ", 0);
num = parseInt(num);


document.write('<h1> Tabla de Multiplicar del ' + num + '</h1>');
console.log("Tabla de Multiplicar del " + num);


document.write('<ul>');

for (let i = 0; i <= 10; i++) {

    console.log(num + " x " + i + " = " + multiplicar(num, i));
    document.write('<li>' + num + ' x ' + i + ' = ' + multiplicar(num, i) + '</li>');
    
}

document.write('</ul>');


function multiplicar(num, i) {
    return num * i;
}