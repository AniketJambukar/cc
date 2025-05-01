def dfs(graph, visited, node):
if node not in visited:
visited.append(node)
for n in graph[node]:
dfs(graph, visited, n)
return visited
graph = {'A': ['B', 'C'],
'B': ['D', 'E'],
'C': ['F'],
'D': [],
'E': ['F'],
'F': []}
visited = dfs(graph, [], 'A')
print(visited)
def bfs(graph, visited, queue):
if queue:
node = queue.pop(0)
if node not in visited:
visited.append(node)
for n in graph[node]:
queue.append(n)
bfs(graph, visited, queue)
return visited
graph = {'A': ['B', 'C'],
'B': ['D', 'E'],
'C': ['F'],
'D': [],
'E': ['F'],
'F': []}
visited = bfs(graph, [], ['A'])
print(visited)


Assign. 2😎😎

import copy
from heapq import heappush, heappop
n = 3
row = [ 1, 0, -1, 0 ]
col = [ 0, -1, 0, 1 ]
class priorityQueue:
def __init__(self):
self.heap = []
def push(self, k):
heappush(self.heap, k)
def pop(self):
return heappop(self.heap)
def empty(self):
if not self.heap:
return True
else:
return False
class node:
def __init__(self, parent, mat, empty_tile_pos,
cost, level):
self.parent = parent
self.mat = mat
self.empty_tile_pos = empty_tile_pos
self.cost = cost
self.level = level
def __lt__(self, nxt):
return self.cost < nxt.cost
def calculateCost(mat, final) -> int:
count = 0
for i in range(n):
for j in range(n):
if ((mat[i][j]) and
(mat[i][j] != final[i][j])):
count += 1
return count
def newNode(mat, empty_tile_pos, new_empty_tile_pos,
level, parent, final) -> node:
new_mat = copy.deepcopy(mat)
x1 = empty_tile_pos[0]
y1 = empty_tile_pos[1]
x2 = new_empty_tile_pos[0]
y2 = new_empty_tile_pos[1]
new_mat[x1][y1], new_mat[x2][y2] = new_mat[x2][y2], new_mat[x1][y1]
cost = calculateCost(new_mat, final)
new_node = node(parent, new_mat, new_empty_tile_pos,
cost, level)
return new_node
def printMatrix(mat):
for i in range(n):
for j in range(n):
print("%d " % (mat[i][j]), end = " ")
print()
def isSafe(x, y):
return x >= 0 and x < n and y >= 0 and y < n
def printPath(root):
if root == None:
return
printPath(root.parent)
printMatrix(root.mat)
print()
def solve(initial, empty_tile_pos, final):
pq = priorityQueue()
cost = calculateCost(initial, final)
root = node(None, initial, empty_tile_pos, cost, 0)
pq.push(root)
while not pq.empty():
minimum = pq.pop()
if minimum.cost == 0:
printPath(minimum)
return
for i in range(4):
new_tile_pos = [
minimum.empty_tile_pos[0] + row[i],
minimum.empty_tile_pos[1] + col[i], ]
if isSafe(new_tile_pos[0], new_tile_pos[1]):
child = newNode(minimum.mat,
minimum.empty_tile_pos,
new_tile_pos,
minimum.level + 1,
minimum, final,)
pq.push(child)
initial = [ [ 1, 2, 3 ],
[ 5, 6, 0 ],
[ 7, 8, 4 ] ]
final = [ [ 1, 2, 3 ],
[ 5, 8, 6 ],
[ 0, 7, 4 ] ]
empty_tile_pos = [ 1, 2 ]
solve(initial, empty_tile_pos, final)




swaping assig.3 😎😎

def selectionSort(array, size):
for ind in range(size):
min_index = ind
for j in range(ind + 1, size):
# select the minimum element in every iteration
if array[j] < array[min_index]:
min_index = j
# swapping the elements to sort the array
(array[ind], array[min_index]) = (array[min_index], array[ind])
arr = [34,20,3,14]
size = len(arr)
selectionSort(arr, size)
print('The array after sorting in Ascending Order by selection sort is:')
print(arr)



queen assig 4:😎😎

print ("Enter the number of queens")
N = int(input())
board = [[0]*N for _ in range(N)]
def attack(i, j):
for k in range(0,N):
if board[i][k]==1 or board[k][j]==1:
return True
for k in range(0,N):
for l in range(0,N):
if (k+l==i+j) or (k-l==i-j):
if board[k][l]==1:
return True
return False
def N_queens(n):
if n==0:
return True
for i in range(0,N):
for j in range(0,N):
if (not(attack(i,j))) and (board[i][j]!=1):
board[i][j] = 1
if N_queens(n-1)==True:
return True
board[i][j] = 0
return False
N_queens(N)
for i in board:
print (i)




chatbot assg. 5:😎😎

def chatbot():
name = input("Enter your name: ")
print("Hello " + name + "!")
print("How can I help you?")
questions = ["What is your college name?", "What is your college code?", "What is your college
address?", "What is your college phone number?"]
answers = ["LoGMIEER", "4093", "Canda Corner, Nashik", ""]
while True:
question = input("Enter your question: ")
if question.lower() == "exit":
break
if question in questions:
print(answers[questions.index(question)])
else:
print("I don't understand.")
chatbot()



asssig 5A chatbot: 😎😎

def greet(bot_name, birth_year):
print("Hello! My name is {0}.".format(bot_name))
print("I was created in {0}.".format(birth_year))
def remind_name():
print('Please, remind me your name.')
name = input()
print("What a great name you have, {0}!".format(name))
def guess_age():
print('Let me guess your age.')
print('Enter remainders of dividing your age by 3, 5 and 7.')
rem3 = int(input())
rem5 = int(input())
rem7 = int(input())
age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105
print("Your age is {0}; that's a good time to start programming!".format(age))
def count():
print('Now I will prove to you that I can count to any number you want.')
num = int(input())
counter = 0
while counter <= num:
print("{0} !".format(counter))
counter += 1
greet('Sbot', '2021') # change it as you need
remind_name()
guess_age()
count()
test()
end()
