'user strict';

//funciones de declaracion o funciones de expresion

//funcion de declaracion
suma1(15, 20); // <- Puede invocarse primero

function suma1(a, b) {
    //Instrucciones de la funcion
    console.log(a + b);
}


// funcion de expresion
const suma2 = function(a, b){
    console.log(a + b);
}

suma2(25, 45);

// Plantillas de Texto

function ingresarAlSustema(nombre='', apellido='') {
    console.log(`Bienvenida ${nombre} ${apellido} puedes ingresar al sistema`);
}

ingresarAlSustema('Jenny', 'Rojas');


// Diferencia entre Metodos y Funciones

let n1 = 15;
let n2 = 20;

console.log(parseInt(n1)); // Funcion
console.log(n2.toString());// Metodo