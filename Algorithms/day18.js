// Last Python Algorithm !

//  String Anagrams

// Given a string,
// return array ...
// where each element is a string 
// representing a different anagram
//  (a different sequence of the letters in that string).
//   Ok to use built in methods
input="iceman"

function anagram(str){
    const output = [];
    function split_str(str, change = ''){
        
      if (!str) output.push(change)
      for (let i = 0; i < str.length; i++){
        split_str(str.slice(0,i) + str.slice(i+1), change + str[i]);
      }
    }
    split_str(str)
    return output
  }

console.log(anagram("abc"));