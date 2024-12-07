const calculadora = {
    sumar: function(n1, n2){
        suma = n1 + n2;
        document.getElementById('result').innerHTML = `La suma de ${n1} mas ${n2} es: ${suma}`;
    },
    restar: function(n1, n2){
        resta = n1 - n2;
        document.getElementById('result').innerHTML = `La resta de ${n1} menos ${n2} es: ${resta}`;
    },
    multiplicar: function(n1, n2){
        multi = n1 * n2;
        document.getElementById('result').innerHTML = `La multiplicacion de ${n1} por ${n2} es: ${multi}`;
    },
    division: function(n1, n2){
        divi = n1 / n2;
        document.getElementById('result').innerHTML = `La division de ${n1} entre ${n2} es: ${divi}`;
    }
}