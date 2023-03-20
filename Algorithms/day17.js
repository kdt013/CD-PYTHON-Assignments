//Many paint applications have a "fill" feature in which
//one pixel, and surrounding pixels of the same color, are 
//changed to a new color. We will build that with a 2D 
//array and integers.

// given a 2 dimensional array(canvas2d), startXY(an array 
// with 2 integers denoting the x and y location from the 
// top left), and newColor(an integer), replace a pixel's 
// color value in canvas2d only if it is the same color as 
// the origin coordinate and is directly adjacent via X or 
// Y to another pixel you will change.
// note: diagonally related pixels are not considered adjacent

//given:
//[[3,2,3,4,3],
// [2,3,3,4,0],
// [7,3,3,5,3],
// [6,5,3,4,1],
// [1,2,3,3,3]]
//...plus startXY of [2,2](x moves right, y moves down) 
//and newColor of 1,
//we change the value denoted by || and all adjecent values,
//and adjacent values to the adjacent value recursively so you 
//end up with the canvas2d returned looking like 
//[[3,2,1,4,3],
// [2,1,1,4,0],
// [7,1,1,5,3],
// [6,5,1,4,1],
// [1,2,1,1,1]]
function floodFill(canvas2d, startXY, newColor){
    return canvas2d;
}

let img = [ [3,2,3,4,3],
            [2,3,3,4,0],
            [7,3,3,5,3],
            [2,5,3,4,1],
            [2,2,3,3,3]];
console.log(img);
console.log(floodFill(img, [2,2], 1));