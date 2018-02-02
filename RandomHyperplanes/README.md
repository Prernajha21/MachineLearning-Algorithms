Python program to experiment with random hyperplanes
for classification. The program takes a dataset as input and
produce new features following the procedure below.

Input training data matrix X: n rows, m columns
Input training labels Y
Input test data X' (n' rows and m columns)


For i = 0 to k do:
a. Create random vector w where each wi is uniformly sampled between -1 and 1.
Set w0 = 0.

b. Project training data X (each row is datapoint xj) onto w. 
Let projection vector zi be Xw (here X has dimensions n by m and w is m by 1).
Append (1+sign(zi))/2 as new column to the right end of Z. Remember that zi is
a vector and so (1+sign(zi))/2 is 0 if the sign is -1 and 1 otherwise.

c. Project test data X' (each row is datapoint xj) onto w. 
Let projection vector z'i be X'w. Append z'i as new column to the right end 
of Z'.

1. Run linear SVM on Z and predict on Z'
2. Do values of k=10, 100, 1000, and 10000.
3. How does the error compare to liblinear on original data X and X for each k?


