const reproductor = {
    cancion: '',
    reprodicir: id => console.log(`Reproduciendo cancion con id: ${id}`),
    pausar: id => console.log(`Pausando cancion con id: ${id}`),
    borrar: id => console.log(`Borrando cancion con id: ${id}`),
    crearPlayList: nombre => console.log(`Creando playList: ${nombre}`),
    reprodicirPlayList: nombre => console.log(`Reproduciendo playList: ${nombre}`),

    set nuevaCancion(cancion) {
        this.cancion = cancion;
        console.log(`Añadiendo ${cancion}`);
    },
    get obtenerCancion() {
        console.log(`Añadiendo ${this.cancion}`);
    }
};

reproductor.reprodicir(30);
reproductor.pausar(30);
reproductor.crearPlayList("Magenta");
reproductor.reprodicirPlayList("Magenta");





const carMovements = {

    carro: '',

    get obtenercarro() {
        return this.carro;
    },
    set nuevocarro(value) {
        this.carro = value;
    },

    encender: chofer => console.log(`El ${carMovements.obtenercarro}, a sido encendido por ${chofer}`),
    apagar: chofer => console.log(`El ${carMovements.obtenercarro}, a sido apagado por ${chofer}`),
    retoceso: chofer => console.log(`El ${carMovements.obtenercarro} de ${chofer} esta retrocediendo`),
    volar: chofer => console.log(`El ${carMovements.obtenercarro} de ${chofer} esta volando! Cuidado!!`),

};

carMovements.nuevocarro = "Mercedez Vens";

carMovements.encender("Juan Carlos")
carMovements.apagar("Juan Carlos")
carMovements.retoceso("Juan Carlos")
carMovements.volar("Juan Carlos")






const producto = {
    nombre: "Monitor 20 Pulgadas",
    precio: 30,
    disponible: true
};

console.log(Object.keys(producto))
console.log(Object.values(producto))
console.log(Object.entries(producto))
