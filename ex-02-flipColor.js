/**
 * flipColor()
 *
 * Write a function called flipColor. This function may be
 * used to change the color of a tile in a game. It should
 * take as input an object. If that object's color property
 * has the value blue, it should change it to red, and
 * vice-versa.
*/

// write the function here (: function declaration standard

function flipColor(Objson){
  //console.log(tileObj)
  if (Objson.color == "blue") {
    Objson.color ="red";
  } else if (Objson.color == "red") {
    Objson.color ="blue";
  } else {
    pass
  }
  return Objson
}

// write the function here (: function expression standard

/*
let flipColor= function(Objson){
  if (Objson.color == "blue") {
    Objson.color ="red";
  } else if (Objson.color == "red") {
    Objson.color ="blue";
  } else {
    pass
  }
  return Objson
}
*/

// write the function here (: ES6 Standard

/*
const flipColor = (tileObj) => if (Objson.color == "blue") {
    Objson.color ="red";
  } else if (Objson.color == "red") {
    Objson.color ="blue";
  } else {
    pass
  }
  return Objson;
*/

// *~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*
// *~*~*~*~*~*~*~* Tests (Don't Touch) *~*~*~*~*~*~*~*~*
// *~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*
console.group('ex-02');
  console.log('%cFunction: flipColor', 'background-color: green; color: white')
console.groupEnd();

var tileObj = {
    width: "200px",
    height: "150px",
    color: "blue"
}

/* ----------------------- TEST-1  ----------------------- */
// Function takes object w/ `color` property with value of 'red'
//   returns object with `color` property with value of 'blue'
/* ------------------------------------------------------ */
console.log('TEST-1');

var tileObj2 = flipColor(tileObj)
console.assert(tileObj2.color === "red")

/* ----------------------- TEST-2  ----------------------- */
// Function takes object w/ `color` property with value of 'blue'
//   returns object with `color` property with value of 'red'
/* ------------------------------------------------------ */
console.log('TEST-2');

var tileObj3 = flipColor(tileObj2)
console.assert(tileObj3.color === "blue")


/* ----------------------- TEST-3  ----------------------- */
// Other properties are not changed
/* ------------------------------------------------------ */
console.log('TEST-3');

console.assert(tileObj3.width === "200px")
console.assert(tileObj3.height === "150px")

/* ----------------------- END  ----------------------- */
console.log('\n')
