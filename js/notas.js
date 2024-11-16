let dato1 = 4;
let dato2 = 4;

console.log(dato1++); // si el contador esta despues del dato, este se muestra y despues se le suma uno
console.log(++dato2); // si el contador esta antes del dato, este suma uno al dato y luego se muestra el dato


const obj = {
    id: 1,
    nombre: 'ojas',
    descripcion: 'cebolla',
    precio: 15.5,
    iva: true
};
obj.disponible = true;
delete obj.disponible;
console.log(obj);

function sum(var1, var2, var3) {
    var suma = var1 + var2 + var3;
    return suma;
}
var result = sum(1, 3, 4);
console.log(result);

function user(nombre = "Homero", apellido = "Rojas") {
    console.log(`${nombre} es grande ${apellido}`);
    console.log(nombre + ' es grande ' + apellido);
}
user('David', 'McDonald');