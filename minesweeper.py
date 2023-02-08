
grid=[ ["-","-","-","#","#"],
        ["-","#","-","-","-"],
        ["-","-","#","-","-"],
        ["-","#","#","-","-"],
        ["-","-","-","-","-"]]

#running loop through row and columns
for row in range(len(grid)):
    for col in range(len(grid[0])):

        if grid[row][col] == '-':
            count = 0
            #For every x coordinate from -1 to 1, for every y coordinate from -1 to 1, 
            # if the position is not a '#' 'count' will then increase by 1
            for x in(-1, 0, 1):
                for y in(-1,0, 1):                                              
                    #looping through all of the cells in every row and column, checking if it is not a '#' character
                    if(0 <= row+x < len(grid) and 0<= col+y <len(grid[0])and grid[row+x][col+y] == "#"):
                        count += 1
            # writes out the value of "count" on '-' cells
            grid[row][col]=str(count)

           
new_grid = [
    [   #checks to see if it is equal to "#"
        "#" if position == "#" 
        #checking if eah cell in the grid is equal to '#'.If it is, it will print out the sum
        #of adjacent cells
        else str(sum(0 <= i+x < len(grid) and 0 <= col+y < len(row) and grid[i+x][col+y] == "#"
        
        for x in (-1, 0, 1) for y in (-1, 0, 1))) 
        #loop through each row and column in the grid, isolating the position of each grid cell that has a '-' in it.
        for col, position in enumerate(row)
    ]   for i, row in enumerate(grid)
]
for i in (new_grid):
    print(i)
