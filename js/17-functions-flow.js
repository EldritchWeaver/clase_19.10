function suma(a, b) {
    return a + b;
};
const result = suma(1, 2);
console.log(result);





// Ejemplo mas "avanzado" XD:

let total = 0;
function agregarCarrito(precio) {
    return total += precio;
};
function calcularImpuestos(total) {
    return 1.15 * total;
};
total = agregarCarrito(200);
total = agregarCarrito(300);
total = agregarCarrito(400);
console.log(total);

const totalAPagar = calcularImpuestos(total);
console.log(`El totaar a pagar es: ${totalAPagar}`);