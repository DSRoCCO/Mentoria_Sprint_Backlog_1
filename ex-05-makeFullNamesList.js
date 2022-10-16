/**
 * makeFullNamesList()
 *
 * Write a function called `makeFullNamesList` that takes an array
 * of objects with first and last names properties and returns
 * an array of strings, where each string is a full title + first & last
 * name.
 *
**/


// write the function here (: function declaration standard


function makeFullNamesList(Listas){
  var respuesta = [];
  Listas.forEach(lista => {
    if (lista.gender == "male") {title = "Mr.";}
    else {title = "Ms.";}
    respuesta.push(title + " "+lista.first+" "+lista.last);
  });
  return respuesta;
}


// write the function here (: function expression standard

/*
let makeFullNamesList = function(Listas){
  var respuesta = [];
  Listas.forEach(lista => {
    if (lista.gender == "male") {title = "Mr.";}
    else {title = "Ms.";}
    respuesta.push(title + " "+lista.first+" "+lista.last);
  });
  return respuesta;
}
*/

// write the function here (: ES6 Standard

/*
const makeFullNamesList = (Listas) => {
  var respuesta = [];
  Listas.forEach(lista => {
    if (lista.gender == "male") {title = "Mr.";}
    else {title = "Ms.";}
    respuesta.push(title + " "+lista.first+" "+lista.last);
  });
  return respuesta;
  }
*/



// *~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*
// *~*~*~*~*~*~*~* Tests (Don't Touch) *~*~*~*~*~*~*~*~*
// *~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*

console.group('ex-05');
  console.log('%cFunction: makeFullNamesList', 'background-color: green; color: white')
console.groupEnd();

var customersList = [
    { first: 'Joe', last: 'Blogs', gender: 'male'},
    { first: 'Kate', last: 'Smith', gender: 'female'},
    { first: 'Dave', last: 'Jones', gender: 'male'},
    { first: 'Jacky', last: 'White', gender: 'female'}
]

var moreCustomersList = [
	{ first: 'Ruby', last: 'Scooby', gender: 'female'},
	{ first: 'Jen', last: 'Vin', gender: 'female'},
	{ first: 'Dan', last: 'Theman', gender: 'male'},
]


var fullNamesList = makeFullNamesList(customersList)
var moreNamesList = makeFullNamesList(moreCustomersList)


/* ----------------------- TEST-1  ----------------------- */
// Function returns an array of strings
/* ------------------------------------------------------ */
console.log('TEST-1');

console.assert(Array.isArray(fullNamesList) === true)
console.assert(typeof fullNamesList[0] === 'string')

console.assert(Array.isArray(moreNamesList) === true)
console.assert(typeof moreNamesList[1] === 'string')


//* ----------------------- TEST-2  ----------------------- */
// Each string element in returned array is formatted
//    '«Gender-Title» «First-Name» «Last-Name»'
/* ------------------------------------------------------ */
console.log('TEST-2');

console.assert(fullNamesList.indexOf("Mr. Joe Blogs") >= 0)
console.assert(fullNamesList.indexOf("Ms. Kate Smith") >= 0)
console.assert(fullNamesList.indexOf("Ms. Jacky White") >= 0)


console.assert(moreNamesList.indexOf("Ms. Ruby Scooby") >= 0 )
console.assert(moreNamesList.indexOf("Mr. Dan Theman") >= 0 )

console.log('\n')
