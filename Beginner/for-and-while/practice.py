'''
Practice Questions
  1.  What keys can you press if your Python program is stuck in an infinite loop?
A = Ctrl + C
  2.  What is the difference between break and continue?
A = Break is for end the loop while continue is used to start over the loop from the begining
  3.  What is the difference between range(10), range(0, 10), and range(0, 10, 1) in a for loop?
A = The first one is for the number of times you want to repeat a block of code, the second has the start number and the finish but do not including the last and the third has the start number, the end number and the step 
  4.  Write a short program that prints the numbers 1 to 10 using a for loop. Then, write an equivalent program that prints the numbers 1 to 10 using a while loop.
for num in range(1, 11):
    print("num")
num = 1
while num < 11:
    print(num)
    num = num + 1
  5.  If you had a function named bacon() inside a module named spam, how would you call it after importing spam?
A = span.bacon()
'''

for num in range(1, 11):
    print(num)
num = 1
while num < 11:
    print(num)
    num = num + 1