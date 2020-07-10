class Solution(object):
    def rotate(self, matrix):
        n = len(matrix)
        if n%2 == 0:
        	m = n/2
        else:
        	m = n/2 + 1

        for i in range(int(n/2)):
        	for j in range(int(m)):
        		temp = matrix[i][j]
        		matrix[i][j] = matrix[n-j-1][i]
        		matrix[n-j-1][i] = matrix[n-i-1][n-j-1]
        		matrix[n-i-1][n-j-1] = matrix[j][n-i-1]
        		matrix[j][n-i-1] = temp