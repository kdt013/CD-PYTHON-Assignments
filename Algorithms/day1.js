/* 
  Acronyms
  Create a function that, given a string, returns the string’s acronym 
  (first letter of each word capitalized). 
  Do it with .split first if you need to, then try to do it without
*/
function acronymize(str) {
    var result=""
    if(str[0] != " "){
       // console.log(str[0]);
       result += str[0];
      }
    for(i = 0; i< str.length;i++){
       if(str[i]== " " ){
        i++;
        //console.log(str[i]);
        result += str[i];
       }
    }
return result;
}

var str1 = "object oriented programming";
var expected1 = "OOP";
console.log(acronymize(str1));

// // The 4 pillars of OOP
var str2 = "abstraction polymorphism inheritance encapsulation";
var expected2 = "APIE";
console.log(acronymize(str2));

var str3 = "software development life cycle";
var expected3 = "SDLC";
console.log(acronymize(str3));

// // // Bonus: ignore extra spaces
// var str4 = "  global   information tracker    ";
// var expected4 = "GIT";
// console.log(acronymize(str4));