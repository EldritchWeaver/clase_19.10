
function porPantalla() {
    console.log("La suma es: ", n1 + n2);
    console.log("La resta es: ", n1 - n2);
    console.log("La multiplicacion es: ", n1 * n2);
    console.log("La division es: ", n1 / n2);
};

function porConsola() {
    document.write("La suma es: " + (n1 + n2) + "</br>");
    document.write("La resta es: " + (n1 - n2) + "</br>");
    document.write("La multiplicacion es: " + (n1 * n2) + "</br>");
    document.write("La division es: " + (n1 / n2) + "</br>");
};




function calc(n1, n2, mostrar) {
        
        if (mostrar != 0) {
            porPantalla(n1, n2);
        } else {
            porConsola(n1, n2);
        }

};


var n1 = prompt("Introduzca numero 1: ", 0);
var n2 = prompt("Introduzca numero 2: ", 0);

var mostrar = prompt("Mostrar? true/false");

n1 = parseInt(n1);
n2 = parseInt(n2);

console.log(mostrar);

calc(n1, n2, mostrar);
