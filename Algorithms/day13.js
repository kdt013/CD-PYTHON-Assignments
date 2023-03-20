// Deduplication, or deduping for short, is the process of removing identical entries from two or more data sets such as mailing lists.
// Today's algorithm is about "deduping" of an array of numbers. 
// First, to make it easy, we do it for a sorted array. Then, we will dedupe an unsorted array.

// Example for deduping sorted array: 
// dedupe of  [ 1, 1, 1, 3, 4, 4, 4, 7, 8, 8 ] will be  [ 1, 3, 4, 7, 8 ]

// Example for deduping of unsorted array:
// Dedupe of [ 3, 4, 1, 4, 4, 5, 3, 4 ] will be [ 1, 3, 4, 5 ]

function dedupe(arr){
    var temp = []
    for(var i=0; i<arr.length; i++){
        if(arr[i] != arr[i-1]){
            temp.push(arr[i])
        }
    }
    return temp
}
console.log(dedupe([1,1,1,3,4,4,4,7,8,8]))

console.log(dedupe([ 3, 4, 1, 4, 4, 5, 3, 4 ]))

console.log(dedupe([]))