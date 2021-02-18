/*
# problem 7:

By listing the first six prime numbers:
 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?


*/

function prime_number_10001(){
    var counter = 0;
    for (i=0;i<100000;i++){

        if(i % 2 !=0){
            if(counter==10001){
                return i;
            }
            counter+=1;


        }

    }


}