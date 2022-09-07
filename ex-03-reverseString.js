
/**
 * reverseString()
 *
 * Write a function called reverseString that takes a string as input
 * and returns a string with the characters in reverse order.
 *
 * (note: can't use the native Array .reverse() method )
 *
*/

// ++ Write YOUR CODE Below

function reverseString(word) {
    var array = word.split("");
    var r_array = array.reverse();
    word = r_array.join("")
    return word

  }


// *~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*
// *~*~*~*~*~*~*~* Tests (Don't Touch) *~*~*~*~*~*~*~*~*
// *~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*


/*-------------------TEST-1-------------------------*/
//  function accepts string and
//    should return the string in reverse order
/*--------------------------------------------------*/
console.log("==== ex-03-reverseString : TEST 1 ====");

console.assert( reverseString('books') === 'skoob')
console.assert( reverseString('coolness') === 'ssenlooc')
console.assert( reverseString('bedtime') === 'emitdeb')
console.assert( reverseString('yah sure') === 'erus hay')

/*-------------------END----------------------------*/
console.log('\n\n');
