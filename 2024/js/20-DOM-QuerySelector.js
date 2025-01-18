/* const course23 = document.querySelector('.course .red');

let course = document.querySelector('.course');
console.log(course);
console.log(course.innerText);
console.log(course.TextContent);
console.log(course.innerHTML)

const description = document.querySelector('#description');
console.log(description);

const course2 = document.querySelectorAll('.course');
console.log(course2);

courses = document.querySelector('.course').textContent = "Calma Vladimir";
console.log(courses);

let newText = "son cosas que pasan, para razonar hay que mantener la calma";
course = document.querySelector('.course').textContent = newText;
console.log(course) */

/* let form = document.querySelector('.form');
let name = document.querySelector('.name').textContent = "Name";
let lastName = document.querySelector('.lastName').textContent = "Last Name"; */

/* document.getElementById('foto-1').src = "../img/gato.jpg"
document.getElementById('foto-1').alt = "gato serio" */

// CAMBIAR HTML STYLES:

var course = document.querySelector('.course');
course.style.color = 'blue';
course.style.background = 'red';
course.style.textAlign = 'center';
course.style.fontSize  = '36px';


let desc = document.querySelector('.description');
console.log(desc.classList);

desc.classList.add('bgblue', 'title');
/* desc.classList.remove('bgblue'); */