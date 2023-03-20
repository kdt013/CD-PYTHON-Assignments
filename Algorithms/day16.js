// fibonacci sequence using recursion
function fib(num){
    if(num === 1){
        return 0
    }
    else if(num === 2){
        return 1
    }
    else{

      var i =  fib(num-1) + fib(num-2)
        
    }
    return i
}
console.log(fib(50))
