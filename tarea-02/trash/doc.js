document.write(`
    <div class="factura">
        <h1>FACTURA</h1>
        <hr>
        <table>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Producto</th>
                    <th>Cantidad a Comprar</th>
                    <th>Precio por Unidad</th>
                    <th>Costos</th>
                </tr>
            </thead>
            <tbody>
`);

// Datos preestablecidos para la tabla
const items = [
    { id: 1, producto: 'Producto A', cantidad: 12, precio: 123, costo: 1476 },
    { id: 2, producto: 'Producto B', cantidad: 5, precio: 200, costo: 1000 }
];

// Agregar filas a la tabla usando document.write
items.forEach(item => {
    document.write(`
        <tr>
            <td>${item.id}</td>
            <td>${item.producto}</td>
            <td>${item.cantidad}</td>
            <td>${item.precio}</td>
            <td>${item.costo}</td>
        </tr>
    `);
});

// Calcular el monto total, IVA y total a pagar
const montoTotal = items.reduce((total, item) => total + item.costo, 0);
const iva = montoTotal * 0.16; // 16% de IVA
const totalAPagar = montoTotal + iva;
const cantidad = 23;

// Cerrar la tabla y agregar la sección de totales
document.write(`
            </tbody>
        </table>
        <hr>
        <section class="info">

            <div class="card">
                <ul>
                    <li>Monto Total: </li>
                    <li>Iva -- 16%: </li>
                    <li>Total a Pagar: </li>
                </ul>
            </div>

            <div class="card">
                <ul>
                    <li>${montoTotal.toFixed(2)} $</li>
                    <li>${iva.toFixed(2)} $</li>
                    <li>${totalAPagar.toFixed(2)} $</li>
                </ul>
            </div>
            <div class="card card2">
                <p>Items:</p>
            </div>

            <div class="card card2">
                <p>${cantidad}</p>
            </div>
        </section>
        <hr>
    </div>
`);