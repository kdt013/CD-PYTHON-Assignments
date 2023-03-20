/* 
Given a string containing space separated words
Reverse each word in the string.
If you need to, use .split to start, then try to do it without.
*/
function reverseWords(str) {
    var newStr = "";
    var newStr2 = "";
    for(var i=str.length-1; i >= 0; i--){
        newStr += str[i];
        if(str[i] == " "){
            for(var j= i-1; j>=0; j--){
                newStr2 += str[j];
            }
            var result = newStr2 + " " + newStr;
        }
    }
    return result;
}
// 

var str1 = "hello";
var expected1 = "olleh";
console.log(reverseWords(str1));

var str2 = "hello world";
var expected2 = "olleh dlrow";
console.log(reverseWords(str2));

var str3 = "abc def ghi";
var expected3 = "cba fed ihg";
console.log(reverseWords(str3));








//write a function that, given a string of words(with spaces),
//returns a new string with words in reverse sequence.
//"This is a test" -> "test a is This"
// const reverseWordOrder = (str) => {
// }

// console.log(reverseWordOrder("Did I shine my shoes       today?        "));
// console.log(reverseWordOrder("'Son, I am able,' she said 'Though you scare me' 'Watch,' said I 'beloved,' I said, 'Watch me scare you though,' Said she, 'Able am I son.'"))
// console.log(reverseWordOrder("This is freaking insane because I live in Cincinnati but I want to live in Mississippi with my family!"));