/**
* Define the 'findUpper' function that receives two arrays as an argument and
* returns a new array with two sub-arrays. Every sub-array will have the first letter
* of the word as first item and the second item will be the word that
* contains this letter, as long as this word starts with a capital letter.
**/


// ++ Write YOUR CODE Below

function findUpper(array1, array2){
    return [array1.sort()[0], array2.sort()[0]];
}

// *~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*
// *~*~*~*~*~*~*~* Tests (Don't Touch) *~*~*~*~*~*~*~*~*
// *~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*

/*-------------------Output-------------------------*/

var arrayExample2 = ['cool', 'great', 'Nice', 'awesome', 'sweet']
var arrayExample3 = ['cool', 'great', 'awesome', 'Super']

var newList = findUpper(arrayExample2, arrayExample3)

/*-------------------TEST-1-------------------------*/

console.log("==== ex-01-findUpper : TEST 1 ====");

console.assert(newList[0][0] === "N");
console.assert(newList[1][0] === "S");



/*--------------------------------------------------*/
/*-------------------END----------------------------*/
console.log('\n\n');
