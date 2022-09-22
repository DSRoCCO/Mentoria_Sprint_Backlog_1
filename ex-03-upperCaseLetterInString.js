
/**
* Defines 'isUpper' function that receives a string as an argument
* and identify if there is a capital letter in the string.
**/


// ++ Write YOUR CODE Below

function isUpper(cadena){
    var result = false
    var temporal = cadena.split("")
    temporal.forEach(function(element){
        if ((isNaN(element)) && (element == element.toUpperCase())){
            result = true;
        }
    });
    return result;
}




// *~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*
// *~*~*~*~*~*~*~* Tests (Don't Touch) *~*~*~*~*~*~*~*~*
// *~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*


/*-------------------TEST-1-------------------------*/

console.log("==== ex-03-upperCaseLetterIn String : TEST 1 ====");

console.assert(isUpper("4567383939sR") === true);

/*-------------------TEST-2-------------------------*/

console.log("==== ex-03-upperCaseLetterIn String : TEST 2 ====");

console.assert(isUpper("23456666663a") === false);



/*--------------------------------------------------*/
/*-------------------END----------------------------*/
console.log('\n\n');
