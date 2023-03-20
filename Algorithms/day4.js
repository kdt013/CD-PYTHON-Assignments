/* 
  String: Is Palindrome
  Create a function that returns a boolean whether the string is a strict palindrome. 
    - palindrome = string that is same forwards and backwards
  
  Do not ignore spaces, punctuation and capitalization
 */

  function isPalindrome(str) {
    for(var left=0; left<str.length/2; left++){
        var right= str.length-1-left;
        if(str[left] != str[right]){
            return false;
        }
    }
  return true;
}


const str1 = "a x a";
const expected1 = true;
console.log(isPalindrome(str1));

const str2 = "racecar";
const expected2 = true;
console.log(isPalindrome(str2));

const str3 = "Dud";
const expected3 = false;
console.log(isPalindrome(str3));

const str4 = "oho!";
const expected4 = false;
console.log(isPalindrome(str4));

/* 
  Longest Palindrome
  For this challenge, we will look not only at the entire string provided,
  but also at the substrings within it.
  Return the longest palindromic substring. 
  Strings longer or shorter than complete words are OK.
  All the substrings of "abc" are:
  a, ab, abc, b, bc, c
*/
// function longestPalindromicSubstring(str) {
//     //check for a palindrome
//     for(var i=0; i<str.length; i++){
//         var substr = 0;
//         if(isPalindrome(substr)){
//             return str;
//         }
//         else{
            
//         }
//     }
//     }




// const phrase1 = "what up, daddy-o?";
// const expectedPhrase1 = "dad";
// console.log(longestPalindromicSubstring(phrase1));

// const phrase2 = "uh, not much";
// const expectedPhrase2 = "u";
// console.log(longestPalindromicSubstring(phrase2));

// const phrase3 = "Yikes! my favorite racecar erupted!";
// const expectedPhrase3 = "e racecar e";
// console.log(longestPalindromicSubstring(phrase3));

// const phrase4 = "a1001x20002y5677765z";
// const expectedPhrase4 = "5677765";
// console.log(longestPalindromicSubstring(phrase4));

// const phrase5 = "a1001x20002y567765z";
// const expectedPhrase5 = "567765";
// console.log(longestPalindromicSubstring(phrase5));

// const phrase6 = "racecar";
// const expectedPhrase6 = "racecar";
// console.log(longestPalindromicSubstring(phrase6));