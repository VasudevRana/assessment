def que_3_rat_maze():
    N = int(input("Enter N \n"))
    M = int(input("Enter M \n"))

    main_maze = []

    for row in range(0, N):
        list1 = []
        for cols in range(0, M):
            list_elements = str(input(f"Enter element \n"))
            if list_elements == "X":
                list1.append(1)
            elif list_elements == "O":
                list1.append(0)
        main_maze.append(list1)
        print("\n")
    print(main_maze)

    def printSolution(sol):
        for i in sol:
            for j in i:
                print(j)
            print("\n")

    def isSafe(maze, x, y):
        if 0 <= x < N and 0 <= y < M and maze[x][y] == 1:
            return True

        return False

    def solveMaze(maze):
        sol = [[0 for _j in range(4)] for _i in range(5)]
        if not solveMazeUtil(maze, 0, 0, sol):
            print("-1")
            return False
        printSolution(sol)
        return True

    def solveMazeUtil(maze, x, y, sol):
        if x == N - 1 and y == M - 1 and maze[x][y] == 1:
            sol[x][y] = 1
            return True

        if isSafe(maze, x, y):
            sol[x][y] = 1

            if solveMazeUtil(maze, x, y + 1, sol):
                return True

            if solveMazeUtil(maze, x + 1, y, sol):
                return True

            sol[x][y] = 0
            return False

        solveMaze(main_maze)


if __name__ == '__main__':
    que_3_rat_maze()
