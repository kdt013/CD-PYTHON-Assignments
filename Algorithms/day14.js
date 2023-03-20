// function mostFreq(arr){
//     var count = []
//     var hash = {}
//     for(var i=0; i <arr.length; i++){
//         var result = arr[i]
//         if(hash[i]==0)
//             count++
//         }
// return arr
// }

function frequency(arr){
    myHash = {};
    newArr = [];
    for(i = 0; i < arr.length; i++){
        if (!(myHash[arr[i]])){
            myHash[arr[i]] = 1;
        }
        else{
            myHash[arr[i]]++;
        }
    }
    highestFrequency = 0
    for(key in myHash){
        if (myHash[key] > highestFrequency)
        {
            highestFrequency = myHash[key];
        }
    }
    for(key in myHash){
        if(myHash[key] == highestFrequency){
            newArr.push(parseInt(key));
        }
    }
    
    return newArr;
}



const nums1 = [];
const expected1 = [];

const nums2 = [1];
const expected2 = [1];

const nums3 = [5, 1, 4];
const expected3 = [];

const nums4 = [5, 1, 4, 1];
const expected4 = [1];

const nums5 = [5, 1, 4, 1, 5];
const expected5 = [5, 1];