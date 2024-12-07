const datos = [
    {id: 0, nombre: "Juan", apellido: "Kilos"},
    {id: 1, nombre: "Carlos", apellido: "Villa"},
    {id: 2, nombre: "Jose", apellido: "Alfonzo"},
    {id: 3, nombre: "Lorenzo", apellido: "Merenguyes"}
]
var rnd = Math.floor(Math.random() * 4)
//console.log(rnd, datos[rnd])
const {id, nombre, apellido} = datos[rnd]
///console.log(id, nombre, apellido)
