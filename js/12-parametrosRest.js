function listadoFrutas(fruta1, fruta2, ...todasLasFrutas) {
    console.log("La Fruta 1 es: " + fruta1);
    console.log("La Fruta 2 es: " + fruta2);
    console.log(todasLasFrutas);
};

listadoFrutas('Cambur', 'Lechoza', 'Patilla', "Melón", "Guayaba");

var frutas = ['Fresas', 'Limon', 'Parchita'];

listadoFrutas(...frutas, 'Cambur', 'Lechoza', 'Guayaba', 'Melón y Jamón')