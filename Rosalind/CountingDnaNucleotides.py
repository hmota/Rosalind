'''
Problem

A string is simply an ordered collection of symbols selected from some alphabet and formed into a word; 
the length of a string is the number of symbols that it contains.

An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is 
"ATGCTTCAGAAAGGTCTTACG."

Given: A DNA string ss of length at most 1000 nt.

Return: Four integers (separated by spaces) counting the respective number of times that the symbols 
'A', 'C', 'G', and 'T' occur in ss.

Sample Dataset

AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC
Sample Output

20 12 17 21
'''

id = DNA
file = open('./rosalind_'+id+'.txt', 'r')
string = file.read()

print qt(string)

def qt(s):
      return s.count("A"), s.count("G"), s.count("C"), s.count("T")

'''
This problem can be solved similarly in every programming language.

The algorithm is straightforward: you should create a counter for every base and then iterate through the sequence, updating the necessary counter.

A_cnt := 0
T_cnt := 0
G_cnt := 0
C_cnt := 0
for i from 1 to length of S do
    if S[i] = 'A' then A_cnt := A_cnt + 1
    if S[i] = 'T' then T_cnt := T_cnt + 1
    if S[i] = 'G' then G_cnt := G_cnt + 1
    if S[i] = 'C' then C_cnt := C_cnt + 1
end do

Note that this algorithm looks four times at each symbol of SS. So we can estimate its running time as 4?N4?N, where NN is the length of SS. So the running time is proportional to NN with some constant, which depends on the programming language used and the speed of the computer. We say that this algorithm has linear complexity and denote it as O(N)O(N), pronounced "Big-Oh of N".
'''