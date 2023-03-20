//recursively find the factorial of num and return it!
function factorial(num){
    if(num === 1){
        return 1;
    }
    return num * factorial(num-1)
}
var f = factorial(5)
console.log(f)

