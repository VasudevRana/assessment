def que_3_rat_maze():
      N = int(input())          
      M = int(input())          

      maze = []

      for row in range(0,N):
            list1 =[]
            for cols in range(0,M):
                  list_elements = int(input())
                  list1.append(list_elements)
            maze.append(list1)
            print("\n")

      print(maze)
      def printSolution( sol ): 
            
          for i in sol: 
              for j in i: 
                  print(str(j) + " ", end ="") 
              print("") 
        
      def isSafe( maze, x, y ): 
            
          if x >= 0 and x < N and y >= 0 and y < M and maze[x][y] == 1: 
              return True
            
          return False
        
      def solveMaze( maze ): 
            
          sol = [ [ 0 for j in range(4) ] for i in range(5) ] 
            
          if solveMazeUtil(maze, 0, 0, sol) == False: 
              print("-1"); 
              return False
            
          printSolution(sol) 
          return True
            
      def solveMazeUtil(maze, x, y, sol): 
            
          if x == N - 1 and y == M - 1 and maze[x][y]== 1: 
              sol[x][y] = 1
              return True
                
          if isSafe(maze, x, y) == True: 
              sol[x][y] = 1
                
              if solveMazeUtil(maze, x, y + 1, sol) == True: 
                  return True
                    
              if solveMazeUtil(maze, x + 1, y, sol) == True: 
                  return True
                
              sol[x][y] = 0
              return False
        

      if __name__ == "__main__":        
          solveMaze(maze) 

que_3_rat_maze()


