from PIL import Image


#sets up an image that will be used to visually represent the cellular automata
def setupImage(dimx, dimy):
	#creates an image in the appropriate dimensions
	file = Image.new("RGB", (dimx,dimy))

	#makes the entire image white for a blank background
	for i in range(dimx):
	    for j in range(dimy):
	        file.putpixel((i,j),(255,255,255))
	return file


#sets up array that will store the cells
def setupArray(dimx, dimy):
	#creates a 2d array with the given dimensions
	grid = [[0 for x in range(dimx)] for y in range(dimy)]


	#places one black pixel in the middle of the first row
	grid[0][round((dimx-1)/2)] = 1
	return grid


#creates an array with all possible inputs
def ruleInputs():
	#ruleInputs contains 8 arrays, each array is one possible set of inputs
	#each input array corresponds to a single output
	ruleInputs = []
	for l in [1,0]:
	    for t in [1,0]:
	        for r in [1,0]:
	            ruleInputs.append([l,t,r])
	return ruleInputs


#for each possible input, if the input array = that array, return the corresponding output
def checkRule(givenInput, ruleI, ruleR):
    for i in range(8):
        if givenInput == ruleI[i]:
            return ruleR[i]


#runs the given rules on the given grid
def runRule(grid, dimx, dimy, ruleI, ruleR):
    for row in range(1,dimy):
        for col in range(dimx):
        	#looks at pixels to the top left, top middle, and top right
            left = grid[row-1][col-1]
            top = grid[row-1][col]
            right = grid[row-1][(col+1)%dimx] #modulus here is used to loop back to the other side once one side is reached

            #sets each pixel as defined by the given rules
            grid[row][col] = checkRule([left,top,right], ruleI, ruleR)
    return grid




#maps the 2d array (grid) onto the PNG image (file)
def showPicture(file, grid, dimx, dimy):
	for i in range(dimy):
	    for j in range(dimx):
	        color = 255*(0**grid[i][j])
	        file.putpixel((j,i),(color,color,color))
	return file






#dimensions of array and image
dimx = 62
dimy = 32

displayImage = setupImage(dimx,dimy)
grid = setupArray(dimx,dimy)
ruleInputs = ruleInputs()

#rule outputs correspinding to rule inputs. this is rule 30, but any could be used
# in this example, the first input array [1,1,1] corresponds to the first output (0), [1,1,0] with the second output (0), and so on
ruleReturns = [0,0,0,1,1,1,1,0]

grid = runRule(grid, dimx, dimy, ruleInputs, ruleReturns)
displayImage = showPicture(displayImage, grid, dimx, dimy)
displayImage.save("cellular.png","PNG")