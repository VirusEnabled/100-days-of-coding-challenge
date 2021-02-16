/*
Problem # 5:



2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

*/

function divisible(number){
let result = true;
for(i=0;i<=20;i++){
    if(number % i != 0){
        result = false;
        break;
    }
}
return result;
}


function smallestDivisible(){

for(i=0;i<=200000000;i++){
    if (divisible(i)){
        return i;
    }
}

}