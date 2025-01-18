const carrito = [
    {nombre: 'Monitor 20 Pulgadas', precio: 500},
    {nombre: 'Monitor 50 Pulgadas', precio: 700},
    {nombre: 'Tablet', precio: 300},
    {nombre: 'Audifonos', precio: 200},
    {nombre: 'Teclado', precio: 50},
    {nombre: 'Celular', precio: 500},
]

// Similar al .forEach existe el metodo llamado .map, con la diferencia de que .map crea un array nuevo

const newArray = carrito.map( function(producto) {
    return `Articulo: ${producto.nombre} Precio ${producto.precio}`;
});


const newArray2 = carrito.forEach( function(producto) {
    // return `Articulo: ${producto.nombre} Precio ${producto.precio}`;
    console.log(`Articulo: ${producto.nombre} Precio ${producto.precio}`);
});

console.log(newArray);
// console.log(newArray2);

for (let index = 0; index < carrito.length; index++) {
    console.log(`Articulo: ${carrito[index].nombre} Precio ${carrito[index].precio}`);
}