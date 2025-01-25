'use strict';

window.addEventListener('load', function() {
    console.log('DOM Loading')

    var form = document.querySelector('#form');
    var box = document.querySelector('.alumnos');
    box.style.display = 'none';

    form.addEventListener('submit', function() {
        console.log('Catching Form');

        var name = document.querySelector('#name').value;
        var last_name = document.querySelector('#last_name').value;
        var age = document.querySelector('#age').value;
        
        if (name.trim() == null || name.trim().length === 0) {
            document.querySelector('#error_name').innerHTML = "Error: Nombre inválido";
            document.querySelector('#error_name').style.color = "red";
            return false;
        } else {
            document.querySelector('#error_name').style.display = "none";
        }
        
        if (last_name.trim() == null || last_name.trim().length === 0) {
            document.querySelector('#error_last_name').innerHTML = "Error: Apellido inválido";
            document.querySelector('#error_last_name').style.color = "red";
            return false;
        } else {
            document.querySelector('#error_last_name').style.display = "none";
        }
        
        if (age == null || age <= 0 || isNaN(age)) {
            document.querySelector('#error_age').innerHTML = "Error: Dato inválido";
            document.querySelector('#error_age').style.color = "red";
            return false;
        } else {
            document.querySelector('#error_age').style.display = "none";
        }

        box.style.display = 'block';

        var p_name = document.querySelector('#p_name span');
        var p_last_name = document.querySelector('#p_last_name span');
        var p_age = document.querySelector('#p_age span');
        
        p_name.innerHTML = name;
        p_last_name.innerHTML = last_name;
        p_age.innerHTML = age;
    });
});