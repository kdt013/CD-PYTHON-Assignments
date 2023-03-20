// /* 
// Given an arr and a separator string, output a string of every item in the array separated by the separator.

// No trailing separator at the end
// Default the separator to a comma with a space after it if no separator is provided
// */
function join(arr, separator) {
    var x = ""
    for (var i = 0; i < arr.length; i++) {
        if (i == arr.length - 1) {
            x += arr[i]
        }
        else {
            x += arr[i] + separator;
        }
        console.log(x.toString())
    }
}

var arr1 = [1, 2, 3];
var separator1 = ", ";
var expected1 = "1, 2, 3";
console.log(join(arr1, separator1));

var arr2 = [1, 2, 3];
var separator2 = "-";
var expected2 = "1-2-3";
console.log(join(arr2, separator2));

var arr3 = [1, 2, 3];
var separator3 = " - ";
var expected3 = "1 - 2 - 3";
console.log(join(arr3,separator3));

var arr4 = [1];
var separator4 = ", ";
var expected4 = "1";
console.log(join(arr4,separator4));

var arr5 = [];
var separator5 = ", ";
var expected5 = "";
console.log(join(arr5,separator5));





/* 
    Book Index
    Given an array of ordered ints representing page numbers
    return a string with the page numbers formatted as page ranges when the nums
    span a consecutive range.
*/
// function bookIndex(nums) {
//     for(var i = 0; i<nums.length; i++){
//         var x = nums[i];
//         if(nums[i] + 1 == nums[i + 1]){
//         }
//     }
// }

// const nums1 = [1, 13, 14, 15, 37, 38, 70];
// const output1 = bookIndex(nums1);
// const expected1 = "1, 13-15, 37-38, 70";
// console.assert(output1 === expected1, {output: output1});

// const nums2 = [5, 6, 7, 8, 9];
// const output2 = bookIndex(nums2);
// const expected2 = "5-9";
// console.assert(output2 === expected2, {output: output2});

// const nums3 = [1, 2, 3, 7, 9, 15, 16, 17];
// const output3 = bookIndex(nums3);
// const expected3 = "1-3, 7, 9, 15-17";
// console.assert(output3 === expected3, {output: output3});