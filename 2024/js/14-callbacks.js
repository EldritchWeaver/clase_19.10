'user strict';

function sumar(num1, num2, mostrarSuma, sumaPorDos) {
    
    var suma = num1 + num2;

    mostrarSuma(suma);
    sumaPorDos(suma);

    return suma;
}

sumar(25, 50, function(dato){

    console.log("la suma es: " + dato);

}, function(dato){

    console.log("La suma por dos es: " + (dato*2));

});
