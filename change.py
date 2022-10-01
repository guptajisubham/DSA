# Python program to interchange
# the diagonals of matrix
N = 3;

# Function to interchange diagonals
def interchangeDiagonals(array):

	# swap elements of diagonal
	for i in range(N):
		if (i != N / 2):
			temp = array[i][i];
			array[i][i] = array[i][N - i - 1];
			array[i][N - i - 1] = temp;
		
	for i in range(N):
		for j in range(N):
			print(array[i][j], end = " ");
		print();

# Driver Code
if __name__ == '__main__':
	array = [ 4, 5, 6 ],[ 1, 2, 3 ],[ 7, 8, 9 ];
	interchangeDiagonals(array);
	
# This code is contributed by Rajput-Ji
