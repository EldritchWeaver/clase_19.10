'user strict';


window.addEventListener('load', function() {
    console.log('DOM Loading')

    var form = document.querySelector('#form');

    form.addEventListener('submit', function() {
        console.log('Catching Form');

        var name = document.querySelector('#name').value;
        var last_name = document.querySelector('#last_name').value;
        var age = document.querySelector('#age').value;

        console.log(name, last_name, age)
    });
});