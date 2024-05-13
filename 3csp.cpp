//Constraint satisfaction problems (CSPs) are mathematical questions defined as a set of objects whose state must satisfy a number of constraints or limitations
//A 3 x 3 Latin square is a grid of size 3 x 3, that is filled with three different symbols in such a way that no row has duplicate symbols and no column has duplicate symbols,
// C++ program to print Latin Square
// A Latin Square is a n x n grid filled by n distinct numbers each appearing exactly once in each row and column.

#include <iostream> 
using namespace std; 

// Function to print n x n Latin Square 
void printLatin(int n) 
{ 
	// A variable to control the rotation 
	// point. 
	int k = n+1; 

	// Loop to print rows 
	for (int i=1; i<=n; i++) 
	{ 
		// This loops runs only after first 
		// iteration of outer loop. It prints 
		// numbers from n to k 
		int temp = k; 
		while (temp <= n) 
		{ 
			cout << temp << " "; 
			temp++; 
		} 

		// This loop prints numbers from 1 to k-1. 
		for (int j=1; j<k; j++) 
			cout << j << " "; 

		k--; 
		cout << endl; 
	} 
} 

// Driver program to test above function 
int main(void) 
{ 
	int n = 5; 

	// Invoking printLatin function 
	printLatin(n); 

	return 0; 
} 
