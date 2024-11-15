// Paso 1: Definir un objeto base
const personaBase = {
  nombre: "",
  edad: 0,
  presentar: function() {
    console.log(`Hola, soy ${this.nombre} y tengo ${this.edad} años.`);
  }
};
// Paso 2: Crear un objeto que contenga un array
const grupo = {
  personas: [], // Inicializamos un array vacío
  agregarPersona: function(nombre, edad) {
    const nuevaPersona = Object.create(personaBase);
    nuevaPersona.nombre = nombre;
    nuevaPersona.edad = edad;
    this.personas.push(nuevaPersona); // Agregamos la nueva persona al array
  }
};
// Crear instancias de personas automáticamente
grupo.agregarPersona('Alice', 30);
grupo.agregarPersona('Bob', 25);
grupo.agregarPersona('Charlie', 35);

// Paso 4: Verificar el resultado
const {personas} = grupo;
console.log(personas);

// Llamar al método presentar para cada persona en el grupo
grupo.personas.forEach((element, indice, arr) => {
  grupo.personas[0].presentar();
});