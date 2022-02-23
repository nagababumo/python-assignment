#What makes NumPy.shape() different from NumPy.size()?
import numpy as np
n=np.array([[2,9,7,6],[9,5,4,3]])
c=np.shape(n)
print(c)
print(np.size(n))
##2. In NumPy, describe the idea of broadcasting.
"""yes in numpy idea of broadcasting is described because its an methodology to do arithmetic operations"""
##3. What makes Python better than other libraries for numerical computation?
"""in python there are so many libraries to do scientific and numerical computations. there are 1.scipy
2.nlp
3.pandas
4.ipython
5.numpy
among this only numpy is the best python library to do numerical computations"""
###4. How does NumPy deal with files?
###5. Mention the importance of NumPy.empty().
"""NumPy empty enables you to create arrays of a 
specific shape The main use of NumPy empty is that it enables you to quickly
 create an array with a specific size and shape. So if you need a
  “holding container” for some future values, you can use the NumPy empty
   function to create it."""