#! /usr/bin/env python3

from queue import Queue

n = int(input('Enter the number of items to add :'))

q = Queue(maxsize = n)

print('Please enter your items separated by lines.')
for i in range(n):
	q.put(input())
print('Appending from queue to stack.')


stack = []
while q.empty()==False:
	stack.append(q.get())

print('Extracting data from stack')

while stack:
	print(stack.pop(),end=',')