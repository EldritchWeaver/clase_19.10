var number = 100;
var num = 0;

var text = "";

while (num < number) {
    num++;
    console.log(num);
    text += "Número es: " + num + "<br>";
}
document.getElementById("numbers").innerHTML = text;