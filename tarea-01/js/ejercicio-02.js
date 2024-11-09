'user strict';
/*
 * EJERCICIO 2 
 * PROGRAMA QUE SOLICITE  DOS NÚMEROS E IMPIRMA LOS NúMEROS QUE SE ENCUENTRAN ENTRE
 * ESOS DOS NÚMEROS INTRODUCIDOS POR EL USUARIO CONCATENANDO LA FRASE "ED-"
 * EJEMPLO INGRESO 1, 5.. IMPRIMA 2,3,4 
 */

var numeroUno = prompt("Introduzca el primer numero: ", 0);
var numeroDos = prompt("Introduzca el segundo numero: ", 0);

/* -------------------------------------------------------------------------- */

if (parseInt(numeroDos) == parseInt(numeroUno) < 0 ) {

    alert("Los Numeros son iguales");

    var numeroUno = prompt("Introduzca el primer numero otra vez: ", 0);
    var numeroDos = prompt("Introduzca el segundo numero otra vez: ", 0);

    numeroUno = parseInt(numeroUno);
    numeroDos = parseInt(numeroDos);
    
} else if (parseInt(numeroUno) < 0) {

    alert("Numero menor a 0");

    var numeroUno = prompt("Introduzca el primer numero otra vez: ", 0);
    numeroUno = parseInt(numeroUno);

} else if (parseInt(numeroDos) < 0) {

    alert("Numero menor a 0");

    var numeroUno = prompt("Introduzca el segundo numero otra vez: ", 0);
    numeroDos = parseInt(numeroDos);
}

/* -------------------------------------------------------------------------- */

if (numeroUno > numeroDos) {

    let n = numeroUno;
    numeroUno = numeroDos;
    numeroDos = n;

}

document.write('<h1> Numeros Ingresados: ' + numeroUno + ', ' + numeroDos + '</h1>');
console.log("Numeros Ingresados: " + numeroUno + ", " + numeroDos);


document.write('<ul>');

for (let i = (numeroUno + 1); i < numeroDos; i++) {

    console.log("ED-" + i);
    document.write('<li>' + 'ED-' + i + '</li>');
    
}

document.write('</ul>');
