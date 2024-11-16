// Paso 1: Definir un objeto base
const personaBase = {
  nombre: "",
  edad: 0
};
// Paso 2: Crear un objeto que contenga un array
const grupo = {
  personas: [], // Inicializamos un array vacío
  agregarPersona: function(nombre, edad) {
    const nuevaPersona = Object.create(personaBase);
    nuevaPersona.nombre = nombre;
    nuevaPersona.edad = edad;
    this.personas.push(nuevaPersona); // Agregamos la nueva persona al array
  },
  presentar: function() {
    let size = this.personas.length;
    
    for (let i = 0; i < size; i++) {
      const {nombre, edad} = this.personas[i];
      let str = 'Hola, soy ' + nombre + ' y tengo ' + this.edad + ' años.';
      console.log(str);
  };
    
  }
};

// Paso 3: Crear instancias de personas
grupo.agregarPersona('Alice', 30);
grupo.agregarPersona('Bob', 25);
grupo.agregarPersona('Charlie', 35);

// Paso 4: Verificar el resultado
const {personas} = grupo;
console.log(personas);

// Llamar al método presentar para cada persona en el grupo
grupo.presentar();