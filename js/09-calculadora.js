/* ---------------------------------------------- */

var n1 = 1;
var n2 = 8;

/* ---------------------------------------------- */

var sum = n1 + n2;
var text1 = "";

text1 += n1 + " + " + n2 + " : " + sum + "<br>";
document.getElementById("sum").innerHTML = text1;


/* ---------------------------------------------- */

var count = 0;
var text = "";

while (count < 10) {

    var result = n1 * n2;

    text += n1 + " x " + n2 + " : " + result + "<br>";

    n1++;
    count++;
    
} document.getElementById("result").innerHTML = text; 

/* ---------------------------------------------- */