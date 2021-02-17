/*
Problem # 6:
Find the difference between the sum of the squares
of the first one hundred natural numbers and the square of the sum.

*/

function difference_between_sums_squared(){

    squared = 0;
    summed = 0;
    for(var i=0; i < 100; i++){
        squared +=i**2;
        summed+=i;
    }

    return Math.abs(squared - (summed**2))
}