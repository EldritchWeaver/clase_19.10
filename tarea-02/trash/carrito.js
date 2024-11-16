'user strict';
/*---------------OBJECTS_DEFINITION_SECTION----------------*/

// Estructura basica de cada producto:
const productoBase = {
  id: 0,
  nombre: "",
  precio: 0.0,
  cantidad: 0,
  venta: 0.0,
  actualizarPrecio: function(nuevoPrecio) {
    this.precio = nuevoPrecio;
  },
  actualizarCantidad: function(nuevaCantidad) {
    this.cantidad = nuevaCantidad;
  },
  calcularVenta: function() {
    this.venta = this.cantidad * this.precio;
    // console.log('venta: ' + this.venta);
  }
};

// Estructura del Carrito de compras:
const carritoDeCompras = {

  productos: [],
  totalArticulos: 0,
  montoTotal: 0.0,
  impuestos: 0.0,
  totalAPagar: 0.0,
  agregarProducto: function(idProducto, nombreProducto, precioUnitario, cantidadComprada) {
    
    if (this.productos.find(producto => producto.id === idProducto)) {
        let indice = this.productos.findIndex(producto => producto.id === idProducto);
  
        this.productos[indice].actualizarCantidad(cantidadComprada);
        this.productos[indice].calcularVenta();
  
    } else {
  
        const nuevoProducto = Object.create(productoBase);
        nuevoProducto.id = idProducto;
        nuevoProducto.nombre = nombreProducto;
        nuevoProducto.precio = precioUnitario;
        nuevoProducto.cantidad = cantidadComprada;
        nuevoProducto.calcularVenta();
  
        // console.log(nuevoProducto.venta);
        this.productos.push(nuevoProducto);
    };
  },
  removerProducto: function(idProducto) {
    this.productos = this.productos.filter(producto => producto.id !== idProducto)
  },
  vaciarCarrito: function() {
    this.productos = 0;
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
  productosDetalles: function(){

    let size = this.productos.length;
    let productosDetalles = [];

    for (let i = 0; i < size; i++) {

      const { id, nombre, precio, cantidad, venta } = this.productos[i];
      productosDetalles.push(id + ' | ' + nombre + ' x ' + cantidad + ' | ' + precio + '$ | ' + venta + '$ \n');

    };
    return productosDetalles;
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
  }
};

/*--------------FUNCTIONS_DEFINITION_SECTION----------------*/
function catalogo(productos) {
  let catalogo = [];
  for (let i = 0; i < productos.length; i++) {
    const { id, nombre, precioPorUnidad} = productos[i];
    catalogo.push(id + ' | ' + nombre + ' => ' + precioPorUnidad + '\$ \n');
  };
  return catalogo;
};
function searchName(productos, id) {
  let producto = productos.find(producto => producto.id === id);
  return producto.nombre;
};
function searchPrize(productos, id) {
  let producto = productos.find(producto => producto.id === id);
  return producto.precioPorUnidad;
};

function mostrarCatalogo(productos) {
  console.log('Catalogo de Productos:\n' +
    '---------------------------------------------' + '\n' +
    'ID | Articulo => Precio Unitario\n' +
    catalogo(productos) +
    '---------------------------------------------' + '\n' +
    'Si desea comprar algo, de aceptar para continuar.'
   );

  alert('OK! Vea nuestro catalogo:\n' +
        '---------------------------------------------' + '\n' +
        'ID | Articulo => Precio Unitario\n' +
        catalogo(productos)+
        '---------------------------------------------' + '\n' +
        ' Si desea comprar algo, de aceptar para continuar.'
        );
};
function ingresarOption() {
  option = prompt('¿Si desea comprar otra cosa ingrese "comprar".' + '\n' +
                  'Si desea ver lo que a comprado ingrese "mirar"' + '\n' +
                  'Si desea mirar el catalogo de nuevo ingrese "catalogo"' + '\n' +
                  'Si decea remover un producto ingrese "remover"' + '\n' +
                  'Si decea vaciar el carrito ingrese "vaciar"' + '\n' +
                  'Si decea terminar la compra ingrese "salir"'
                );
 
  while (option !== 'comprar' && option !== 'mirar'  && option !== 'catalogo' && option !== 'remover' && option !== 'vaciar' && option !== 'salir') {

    alert('Error: Opcion no valida. Vuelva a intentar.');
    option = prompt('¿Si desea comprar otra cosa ingrese "comprar".' + '\n' +
                  'Si desea ver lo que a comprado ingrese "mirar"' + '\n' +
                  'Si desea mirar el catalogo de nuevo ingrese "catalogo"' + '\n' +
                  'Si decea remover un producto ingrese "remover"' + '\n' +
                  'Si decea vaciar el carrito ingrese "vaciar"' + '\n' +
                  'Si decea terminar la compra ingrese "salir"'
                );
  };
  return option;
};

/*--------------VARIABLES_DEFINITION_SECTION----------------*/
const articulos = [
  { id: 1, nombre: "Laptop HP", precioPorUnidad: 800},
  { id: 2, nombre: "Smartphone Samsung", precioPorUnidad: 600},
  { id: 3, nombre: "Auriculares Sony", precioPorUnidad: 100},
  { id: 4, nombre: "Teclado Mecánico Razer", precioPorUnidad: 120},
  { id: 5, nombre: "Monitor LG 27\"", precioPorUnidad: 300},
  { id: 6, nombre: "Disco Duro Externo 1TB", precioPorUnidad: 80},
  { id: 7, nombre: "Impresora Canon", precioPorUnidad: 150},
  { id: 8, nombre: "Webcam Logitech", precioPorUnidad: 70},
  { id: 9, nombre: "Proyector Epson", precioPorUnidad: 400},
  { id: 10, nombre: "Ratón Inalámbrico", precioPorUnidad: 50}
];
let i = 'no';
const iva = 16;

/*--------------LOOP/MAIN_SECTION----------------*/
alert("¡Bienvenido!\n Este es el Carrito de Compras de la Tienda de Don Gorge.");

i = prompt('¿Desea Comprar? si / no');

if (i === 'si' || i === 'SI' || i === 'Si' || i === 'sI') {
  option = 'comprar';
} else {
  option = 'salir';
};

while (option !== 'salir') {
  mostrarCatalogo(articulos);

  let idProducto = prompt('Ingrese el ID del articulo que desea comprar: ');    
  idProducto = parseInt(idProducto);

  while (articulos.some(articulo => articulo.id === idProducto) === false) {

    alert('Error: Opcion no valida. Vuelva a intentar.');
    idProducto = prompt('Ingrese el ID del articulo que desea comprar: ');
    idProducto = parseInt(idProducto);

  };

  let cantidadComprada = prompt('Ingrese la cantidad que desea comprar: ', 1);
  cantidadComprada = parseInt(cantidadComprada);

  let nombreProducto = searchName(articulos, idProducto);
  let precioUnitario = searchPrize(articulos, idProducto);

  //console.log(nombreProducto, precioUnitario)
  carritoDeCompras.agregarProducto(idProducto, nombreProducto, precioUnitario, cantidadComprada);

  let option = ingresarOption();

  switch (option) {
    case 'comprar':
      break;

    case 'mirar':
      
      carritoDeCompras.calcularTotalArticulosMontoTotal();
      carritoDeCompras.calcularImpuestos(iva);
      carritoDeCompras.calcularTotalAPagar();
  
      carritoDeCompras.mostrarCompraConAlert(); 
      
      option = ingresarOption();
      break;
    
    case 'catalogo':

      mostrarCatalogo(articulos);

      option = ingresarOption();
      break;

    case 'remover':
      carritoDeCompras.mostrarCompraConAlert();

      let idProducto = prompt('Ingrese el ID del articulo que desea remover: ');    
      idProducto = parseInt(idProducto);
    
      while (articulos.some(articulo => articulo.id === idProducto) === false) {
    
        alert('Error: Opcion no valida. Vuelva a intentar.');
        idProducto = prompt('Ingrese el ID del articulo que desea remover: ');
        idProducto = parseInt(idProducto);
    
      };

      carritoDeCompras.removerProducto(idProducto);

      option = ingresarOption();
      break;

    case 'vaciar':
      carritoDeCompras.vaciarCarrito();

      option = ingresarOption();
      break;
    case 'salir':
      option = 'salir';
      break;

    default:
      // Por si acaso
      option = 'comprar';
      break;
  }
};
