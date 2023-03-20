/* 
  Balance Index
  Here, a balance point is ON an index, not between indices.
  Return the balance index where sums are equal on either side
  (exclude its own value).

  Return -1 if none exist.

*/

function balancedIndex(arr){
 
    var sumleft=0;
    var sumright=0
    for (var i= 0; i<arr.length ;i++){   
        sumright += arr[i]        
    }
// in each step, we reduce arr[i] from sumleft and add it to sumright unitl they match. 
    for( var i=0; i<arr.length; i++){
        
        sumleft += arr[i]
        //console.log(sumleft,sumright)
        if (sumleft == sumright){
            return i
        }
        sumright -= arr[i]
    }
// if they didn't match we return -1
    return -1
}

const nums1 = [-2, 5, 7, 0, 3];
const expected1 = 2;

const nums2 = [9, 9];

