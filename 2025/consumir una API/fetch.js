'use strict'

var users = [];

//Captura el div de usuario
var div_users = document.querySelector("#users");
fetch('https://reqres.in/api/users')
    .then(data => data.json())
    // Se convierte en un objeto Javascript
    // Esta conversion devuelve una promesa que se maneja en el siguiente .then

    .then(personas => {         // Este es el siguiente paso en la cadenma de personas. Una vez que los datos han sido convertidos un objero JS, se pasan como parametro (data) a la ssiguiente funcion
        users = personas.data;  // asigna los datos recibidos con los usuarios de la API a la variable users.
        console.log(users);

        users.map((personas, i) =>{
            let name = document.createElement('h4');
            name.innerHTML = i + " - " + personas.first_name + " " + personas.last_name;

            div_users.append(name);
        });
    })
    .catch(error => console.error('Error al obtener los datos:', error)); //Esta parte captura cualquier error que