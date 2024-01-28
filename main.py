sticks = 10
p1Take = 0
p2Take = 0

print('Welcome to the game of sticks. ' 'The starting amount of sticks will be', sticks)

def picker():
  global sticks
  #input part that will be looped through until sticks =1
  p1Take = input('Player 1: How many sticks do you take (1-3)? ')
  p1Take = int(p1Take)
  sticks = sticks - p1Take
  print('There are now', sticks, 'on the board')
  if(sticks<=1):
    print('Player 2, you have lost')
    return
  p2Take = input('Player 2: How many sticks do you take (1-3)? ')
  p2Take = int(p2Take)
  sticks = sticks - p2Take
  print('There are now ', sticks, ' sticks on the board')
  if(sticks<=1):
    print('Player 1, you have lost')

while(sticks >1):
    picker()

