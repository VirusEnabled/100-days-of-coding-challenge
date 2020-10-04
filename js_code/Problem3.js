/*
Euler Problem #3:


The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?

*/

function find_smallest_prime_factor(number)
{
    var upper_bound = number*1/2
	for(i=0;i<upper_bound;i++)
	{
	    if(number % i == 0)
	    {
            return i;
	    }

	}

	return num;

}



function find_largest_prime_factor()
{
    number = 600851475143
	while(true)
	{
	    smallest_factor = find_smallest_prime_factor(number);
		if (smallest_factor < number)
		{
            number/= smallest_factor;
		}
		else
		{
            return number;
		}
	}


}