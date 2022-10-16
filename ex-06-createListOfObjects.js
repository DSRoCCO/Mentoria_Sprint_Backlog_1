/**
 * createListOfObjects()
 *
 * Write a function called createListOfObjects that accepts an
 * an array of strings with first and last names and returns
 * an array of objects that each have the property `firstName`
 * and `lastName` and first name and last name values
 * corresponding value
 *
 * var namesList = ['Cameron Betts', 'Shana Lopez', 'Angela Li']
 *
 * createListOfObjects(namesList)
 *  =>
 *  [
 *     { firstName: 'Camer', lastName: 'Betts'},
 *     { firstName: 'Shana', lastName: 'Lopez'},
 *     { firstName: 'Angela', lastName: 'Li'}
 *  ]
 *
 * HINT: You might be able to reuse some of the logic from createNameObject()
*/


// write the function here (: function declaration standard

function createListOfObjects(nameslist){
  var respuesta = [];
  nameslist.forEach(names => {
  namesjson = {}
  namesjson.firstName=names.split(" ")[0].trim();
  namesjson.lastName=names.split(" ")[1].trim();
  //namesjson[names.split(" ")[0].trim()]=names.split(" ")[1].trim();
  respuesta.push(namesjson);
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
console.group('ex-06');
  console.log('%cFunction: createListOfObjects', 'background-color: green; color: white')
console.groupEnd();


var realNinjas = [
  'Chuck Norris',
  'Jackie Chan',
  'Lucy Liu',
  'Billy Blanks',
  'Michelle Yeoh',
  'Jet Li'
]

var realSportsStars = [
	'Kenny Powers',
	'Ricky Vaughn',
	'Dottie Hinson',
	'Jesus Shuttlesworth',
	'Scotty Smalls'
]


var ninjaListOfObjects = createListOfObjects(realNinjas)
var sportStarsListOfObjects = createListOfObjects(realSportsStars)

/* ----------------------- TEST-1  ----------------------- */
// Function returns an array of objects
/* ------------------------------------------------------ */
console.log('TEST-1');

console.assert(Array.isArray(ninjaListOfObjects) === true)
console.assert(typeof ninjaListOfObjects[0] === "object")


//* ----------------------- TEST-2  ----------------------- */
// Each object element of array has `firstName` + `lastName`
//    properties
/* ------------------------------------------------------ */
console.log('TEST-2');

// createListOfObjects(realNinjas)
console.assert(ninjaListOfObjects[0].firstName === "Chuck")
console.assert(ninjaListOfObjects[0].lastName === "Norris")

console.assert(ninjaListOfObjects[1].firstName === "Jackie")
console.assert(ninjaListOfObjects[1].lastName === "Chan")

console.assert(ninjaListOfObjects[3].firstName === "Billy")
console.assert(ninjaListOfObjects[3].lastName === "Blanks")



// createListOfObjects(realSportsStars)
console.assert(sportStarsListOfObjects[1].firstName === "Ricky")
console.assert(sportStarsListOfObjects[1].lastName === "Vaughn")

console.assert(sportStarsListOfObjects[3].firstName === "Jesus")
console.assert(sportStarsListOfObjects[3].lastName === "Shuttlesworth")

console.log('\n')
