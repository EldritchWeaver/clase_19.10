'user strict';

const carro1 = {
    marca1: 'Toyota',
    modelo1: 'Toyota Corolla',
    año1: '2010',
    placa1: 'A43J0B',
    color1: 'Azul',
    puertas1: 2,
    estadoGeneral1: 'Nuevo'
}
/* console.log(carro); */

const curso = {
    nombre: 'programacion',
    precio: 40,
    disponible: true,

    info: {
        fechaInicio: '5 de noviembre',
        fechaFinalizacion: '10 de Diciembre',

        carro2: {
            marca: 'Toyota',
            modelo: 'Toyota Corolla',

            datosTec: {
                año: '2010',
                placa: 'A43J0B',
                color: 'Azul',
                puertas: 2,
                estadoGeneral: 'Nuevo'
            }
        }
    },

    calculadora: {

        suma: function(a, b) {
            return a + b;
        },
        resta: function(a, b) {
            return a - b;
        }
    }
}
/* console.log(curso); */

/* curso.modalidad = 'presencial';

delete curso.modalidad;
console.log(curso); */

// Forma Antigua de desestructurar un objeto
/* const nombreCurso = curso.nombre;
console.log(nombreCurso); */

/* 
Object.freeze(curso); // No se puede modificar
console.log(Object.isFrozen(curso)) // Verifia si esta conjelado
*/

/* Object.seal(curso);

delete curso.nombre;

curso.nombre = 'Programacion'; */

// Nueva forma
const {nombre, precio, disponible, calculadora: {suma}, info, info: {carro2, carro2: {datosTec, datosTec:{año}}}} = curso;

console.log(nombre);
console.log(suma(5, 10))


const planificacion = Object.assign(curso, carro1);

console.log(planificacion);
