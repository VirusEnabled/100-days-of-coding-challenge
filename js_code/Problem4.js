/*
Euler Problem #4:



A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

*/

function isPalindrome(number){
    // takes a number and verifies if it's a palindrome
    var str = number.toString();
    var inverted = "";
    var result = false;
    for(x=str.length-1; x >= 0; x--){

        inverted = inverted+str[x]
    }

    if(inverted==str)
    {

        result = true;

    }

    return result;
}

function getMaxOfArray(numArray) {
  return Math.max.apply(null, numArray);
}

function largestPalindromeNumberOf3(){
    var result = []

    for(var x=100; x < 1000;x++){


        for(var y=100; y < 1000;y++)
        {

            if(isPalindrome(x*y))
            {
                result.push(x*y);
            }


        }

    }

    return getMaxOfArray(result);

}

largestPalindromeNumberOf3()