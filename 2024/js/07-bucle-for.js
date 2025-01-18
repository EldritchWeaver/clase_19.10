/* const estados = ["Maracay", "Caracas", "Barinas", "Guarico", "Zulia"];

var estadosText = "";
var familyText = "";

for (let i = 0; i < estados.length; i++) {
    console.log(estados[i]) + "<br>";
    estadosText += estados[i] + "<br>";
}

const family = ["Gabriel", "Hugo", "Varymar", "María", "Nelly", "Dalia", "José"];

for (let i = 0; i < family.length; i++) {
    familyText +='<li id="family"></li>'; familyText += family[i];
}
document.getElementById("family").innerHTML = familyText;

document.getElementById("estados").innerHTML = estadosText;
 */

var numbers = [];
for (let i = 1; i <= 20; i++) {
    numbers[i] = i;
}

var text = "";

for (let i = 1; i <= numbers.length; i++) {
    console.log(numbers[i]);
    text += numbers[i] + "<br>";
}
document.getElementById("numbers").innerHTML = text;