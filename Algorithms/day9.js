

function rotateString(str, n){
    var result = "";
for(var i=str.length-1; i<str.length; i++){
    // result += str[i]
    }

for(var i=0; i<str.length-n; i++){
    result += str[i]
}
result = str[str.length-1] + result
return result;


}

console.log(rotateString("shde",1))


//1 rotation: shde --> eshd
//1 rotation: shde --> desh
//1 rotation: shde --> hdes

// const str = "Hello World";

// const rotateAmnt1 = 0;
// const expected1 = "Hello World";

// const rotateAmnt2 = 1;
// const expected2 = "dHello Worl";

// const rotateAmnt3 = 2;
// const expected3 = "ldHello Wor";

// const rotateAmnt4 = 4;
// const expected4 = "orldHello W";

// const rotateAmnt5 = 13;
// const expected5 = "ldHello Wor";