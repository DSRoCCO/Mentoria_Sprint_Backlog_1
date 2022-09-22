/**
* Defines the `findSymbols` function that receives a string as an argument
* and identifies a certain sequence of symbols in the string. It is important
* that you observe the sequence that each character follows in the string and
* result of each comparison is true.
**/


// ++ Write YOUR CODE Below

function findSymbols(cadena){
    return /^[\+\-][a-z][\+\-].{4}[\+\-][a-z][\+\-]$/.test(cadena);
}



// *~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*
// *~*~*~*~*~*~*~* Tests (Don't Touch) *~*~*~*~*~*~*~*~*
// *~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*


/*-------------------TEST-1-------------------------*/

console.log("==== ex-04-findSymbols : TEST 1 ====");

console.assert(findSymbols("-m+=10=+s+") === true);

/*-------------------TEST-2-------------------------*/

console.log("==== ex-04-findSymbols : TEST 2 ====");

console.assert(findSymbols("h++l+") == false);

/*-------------------TEST-3-------------------------*/

console.log("==== ex-04-findSymbols : TEST 3 ====");

console.assert(findSymbols("lk-+jh") == false);

/*-------------------TEST-4-------------------------*/

console.log("==== ex-04-findSymbols : TEST 4 ====");

console.assert(findSymbols("-+hello") == false);

/*-------------------TEST-4-------------------------*/

console.log("==== ex-04-findSymbols : TEST 5 ====");

console.assert(findSymbols("-d+0=sa-z-") == true);

/*-------------------TEST-5-------------------------*/

console.log("==== ex-04-findSymbols : TEST 6 ====");

console.assert(findSymbols("--+0=sa-z-") == false);

/*-------------------TEST-6-------------------------*/

console.log("==== ex-04-findSymbols : TEST 7 ====");

console.assert(findSymbols("-++0=sa-z-") == false);

/*-------------------TEST-7-------------------------*/

console.log("==== ex-04-findSymbols : TEST 8 ====");

console.assert(findSymbols("-8+0=sa-z-") == false);


/*--------------------------------------------------*/
/*-------------------END----------------------------*/
console.log('\n\n');
