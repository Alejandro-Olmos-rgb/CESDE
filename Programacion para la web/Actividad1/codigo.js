//Uso de variables
/*var nombre = 'CESDE';
console.log(nombre);
console.log(typeof(nombre));

var edad = 52;
console.log(edad);
console.log(typeof(edad));

edad = 'Cinco';
console.log(edad);
console.log(typeof(edad));

var sueldo = 1300000.99;
console.log(sueldo);
console.log(typeof(sueldo));

var tieneTrabajo = false;
console.log(tieneTrabajo);
console.log(typeof(tieneTrabajo));

var salon;
console.log(salon);

puestoDeTrabajo = null;
console.log(puestoDeTrabajo);

//  * Operadores matemáticos +, -, *, /
 

 var edadAna, edadMaria, diferenciaEdad;
 var sumaEdades, yearAna, yearMaria, yearActual;

 edadAna = 34;
 edadMaria = 28;
 yearActual = 2019;

diferenciaEdad = edadAna - edadMaria;
sumaEdades = edadAna + edadMaria;

yearAna = yearActual - edadAna;
yearMaria = yearActual - edadMaria;

console.log(diferenciaEdad);
console.log(sumaEdades);
console.log('Año en que nació Ana ' + yearAna);
console.log('Año en que nació María ' + yearMaria);
console.log(yearActual * 5);
console.log(yearActual / 2)

let persona = {nombre: 'JORGE', edad: 56};
document.writeln(persona.nombre);
document.writeln('<br>');
document.writeln(persona.edad);*/

let numero, unidades, decenas, centenas, resto;
numero = prompt("Ingrese un numero de 3 cifras");
centenas = Math.trunc(numero / 100);
resto = numero % 100;
decenas = Math.trunc(resto / 10);
unidades = resto % 10;
document.writeln('Unidades', unidades);
document.writeln('Decenas', decenas);
document.writeln('centenas', centenas)