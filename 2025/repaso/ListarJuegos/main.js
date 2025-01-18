'use strict';

var form = document.querySelector('#form');
var ul = document.querySelector('#fixGames');

//Funcion para construir la lista
function buildList() {
    ul.innerHTML = ''; //Limpiamos el contenido antes de recostruir
    for (var i in localStorage) {
        if (typeof localStorage[i] === 'string') {
            var li = document.createElement('li');
            li.textContent = localStorage[i];
            ul.appendChild(li);
        }
    }
}

buildList(); //Construir lista al cargar la pagina

form.addEventListener('submit', function(event) {
    event.preventDefault(); //Evita el envio del formulario por defecto

    var game = document.querySelector('#addGame').value;
    if (game.length >= 1) {
        localStorage.setItem(game, game);
        buildList();
    }
});