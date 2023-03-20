//given a number of cents, return an object with the count
//of how many of each coin should be returned
//67 -> 2 quarters, 1 dime, 1 nickel, 2 pennies
//78 -> 3 quarters, 0 dimes, 0 nickels, 3 pennies

//given a number less than or equal to 99 give change in the least amount of coins
//each input, divide by 25, then by 10, then 5, then 1
//store the remaining cents in a var using % 25,10,5,1 before continuing to the next coin
function coinChange(cents){
    var quarters = 0;
    var dimes = 0;
    var nickels = 0;
    var penny = 0;

    // if(cents <= 99){

        quarters = Math.floor(cents/25);
        cents = cents % 25;

        dimes = Math.floor(cents/10);
        cents = cents % 10;

        nickels = Math.floor(cents/5);
        cents= cents % 5;

        penny = Math.floor(cents/1);
        cents = cents % 1;

        console.log("quarters: " + quarters) 
        console.log("dimes: " + dimes)  
        console.log("nickels: " + nickels) 
        console.log("pennies: " + penny) 
        console.log("cents: " + cents)  
    // }

//     change = {"coins": "quarters", "nickels", "dimes", "penny"}
//    console.log(change)
}
console.log(coinChange(125));
console.log(coinChange(27));
console.log(coinChange(73));
console.log(coinChange(67))


//if you get the time, work on dollarAndCoinChange
//given a cent amount, return an object with the count
//of how many dollars(1s, 5s, 10s) and how many coins
//should be returned. NOTE: use whole cents, not decimals
//4632 -> 4 tens, 1 five, 1 one, 1 quarter, 0 dimes, 1 nickel, 2 pennies
function dollarAndCoinChange(cents){
    var quarters = 0;
    var dimes = 0;
    var nickels = 0;
    var penny = 0;

    if(cents <= 99){

        quarters = Math.floor(cents/25);
        cents = cents % 25;

        dimes = Math.floor(cents/10);
        cents = cents % 10;

        nickels = Math.floor(cents/5);
        cents= cents % 5;

        penny = Math.floor(cents/1);
        cents = cents % 1;
}

}