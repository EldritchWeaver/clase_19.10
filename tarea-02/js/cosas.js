'user strict';
/*---------------DEFINITION_SECTION----------------*/

// Estructura basica de cada producto:
const productoBase = {
  id: 0,
  nombre: "",
  precio: 0.0,
  cantidad: 0,
  venta: 0.0,
  actualizarPrecio: function(nuevoPrecio, masItems) {

    this.precio = nuevoPrecio;
    this.cantidad = masItems;
  },
  calcularVenta: function() {

    this.venta = this.cantidad * this.precio;
    // console.log('venta: ' + this.venta);
  }
};
// Esteuctura del Carrito de compras:
const carritoDeCompras = {

  productos: [],
  totalArticulos: 0,
  montoTotal: 0.0,
  impuestos: 0.0,
  totalAPagar: 0.0,
  agregarProducto: function(idProducto, nombreProducto, precioUnitario, cantidadComprada) {

    const nuevoProducto = Object.create(productoBase);
    nuevoProducto.id = idProducto;
    nuevoProducto.nombre = nombreProducto;
    nuevoProducto.precio = precioUnitario;
    nuevoProducto.cantidad = cantidadComprada;
    nuevoProducto.calcularVenta();

    // console.log(nuevoProducto.venta);
    this.productos.push(nuevoProducto);
  },
  calcularTotalArticulosMontoTotal: function() {

    let size = this.productos.length;
    // console.log(size);

    for (let i = 0; i < size; i++) {

      const {cantidad, venta} = this.productos[i];
      // console.log(cantidad);
      this.totalArticulos += cantidad;
      this.montoTotal += venta;
    };

    // console.log('Items: ' + this.totalArticulos);
    // console.log(this.montoTotal);
  },
  calcularImpuestos: function(iva) {

    let impuesto = iva / 100;
    // console.log(impuesto)
    
    this.impuestos = this.montoTotal * impuesto;
    // console.log(this.impuestos);
  },
  calcularTotalAPagar: function() {

    this.totalAPagar = this.montoTotal + this.impuestos;
  },
  mostrarCompraPorConsola: function() {
    console.log( 'Carrito de Compras:' + '\n' +
          '---------------------------------------------' + '\n' +
          this.productosDetalles() +
          '---------------------------------------------' + '\n' +
          'Monto Total: ' + this.montoTotal + '\n' +
          'Iva 16%  ----  ' + this.impuestos + '\n' + 
          'Total a Pagar: ' + this.totalAPagar + '\n' +
          '---------------------------------------------' + '\n' +
          'Items: ' + this.totalArticulos + '\n' +
          '---------------------------------------------'
        );
  },
  mostrarCompraConAlert: function() {
    alert( 'Carrito de Compras:' + '\n' +
          '---------------------------------------------' + '\n' +
          this.productosDetalles() +
          '---------------------------------------------' + '\n' +
          'Monto Total: ' + this.montoTotal + '\n' +
          'Iva 16%  ----  ' + this.impuestos + '\n' + 
          'Total a Pagar: ' + this.totalAPagar + '\n' +
          '---------------------------------------------' + '\n' +
          'Items: ' + this.totalArticulos + '\n' +
          '---------------------------------------------'
        );
  },
  productosDetalles: function(){

    let size = this.productos.length;
    let productosDetalles = [];

    for (let i = 0; i < size; i++) {

      const { id, nombre, precio, cantidad, venta } = this.productos[i];
      productosDetalles.push(id + ' | ' + nombre + ' : ' + cantidad + ' | ' + precio + ' | ' + venta + '\n');

    };
    return productosDetalles;
  },
  removerProducto: function(idProducto) {

    // falta añadir casos de uso, tipo cuantos elementos va a quitar, y si son todos elimine el producto directamente
    this.productos = this.productos.filter(producto => producto.id !== idProducto)
  },
  vaciarCarrito: function() {
    this.productos = 0;
  }
};
let iva = 16;

let productos = [
  [1, "Laptop HP", 800],
  [2, "Smartphone Samsung", 600],
  [3, "Auriculares Sony", 100],
  [4, "Teclado Mecánico Razer", 120],
  [5, "Monitor LG 27''", 300],
  [6, "Disco Duro Externo 1TB", 80],
  [7, "Impresora Canon", 150],
  [8, "Webcam Logitech", 70],
  [9, "Proyector Epson", 400],
  [10, "Ratón Inalámbrico", 50]
];
// alert("Este es un mensaje con un salto de línea.\n¡Bienvenido!");
/*--------------INSTANTIATE_SECTION----------------*/

/* carritoDeCompras.agregarProducto(0, 'Papelon', 2.4, 10);
carritoDeCompras.agregarProducto(1, 'Yuca', 1.5, 5);
carritoDeCompras.agregarProducto(productos[1][0], productos[1][1], productos[1][2], 4); */
let count = 0;
for (let i = 0; i < productos.length; i++) {
  let cantidad = i * (productos.length / 2) +1;
  carritoDeCompras.agregarProducto(productos[i][count], productos[i][count+1], productos[i][count+2], cantidad);
}

// carritoDeCompras.vaciarCarrito();
/*
if (carritoDeCompras.productos.length > 0) {

  carritoDeCompras.productos[1].actualizarPrecio(5, 20)
  carritoDeCompras.productos[1].calcularVenta();

} else {

    console.log("No hay productos en el carrito.");

};
*/
carritoDeCompras.calcularTotalArticulosMontoTotal();
carritoDeCompras.calcularImpuestos(iva);
carritoDeCompras.calcularTotalAPagar();

//carritoDeCompras.removerProducto(0);
//carritoDeCompras.vaciarCarrito();

/*-----------------RENDER_SECTION------------------*/

if (carritoDeCompras.productos.length > 0) {

  carritoDeCompras.mostrarCompraPorConsola();
  carritoDeCompras.mostrarCompraConAlert();

} else {

    console.log("No hay productos en el carrito.");

};


