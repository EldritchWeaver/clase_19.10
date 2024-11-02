

alert("Hola, Mundo!");

var n1 = prompt("Introduzca numero 1: ", 0);
var n2 = prompt("Introduzca numero 2: ", 0);

//pedir dos numeros al usiuaro e imprimir cual de los dos numeros es mayor y cual es menor
//si los dos son iguales, imprime los dos numeros

n1 = parseInt(n1);
n2 = parseInt(n2);

if (n1 > n2){

    console.log(n1, "es mayor que:", n2);

} else if (n1 < n2){

    console.log(n2, "es mayor que:", n1);
    
} else {

    console.log("Los numeros", n1, "y", n2, "son iguales.");

}