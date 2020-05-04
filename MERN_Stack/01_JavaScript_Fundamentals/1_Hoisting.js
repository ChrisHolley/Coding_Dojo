console.log("Example");
console.log(example);
var example = "I'm the example!";
// After hoisting by the interpreter
// var example;
// console.log(example); // logs undefined
// example = "I'm the example!"

// console.log("Example ES6 syntax")
// console.log(example2);
// let example2 = "I'm the example!";

//Problem #1
console.log("Problem #1");
//Given:
console.log(hello);
var hello = 'world';
// After hoisting by the interpreter
// var hello;
// console.log(hello);
// hello = 'world';
// undefined

console.log("Problem #2");
var needle = 'haystack';
test();
function test(){
    var needle = 'magnet';
    console.log(needle);
}
//Predicted outcome:
// var needle = 'haystack';
// test();
// var needle = 'magnet';
// magnet

console.log("Problem #3");
var brendan = 'super cool';
function print(){
    brendan = 'only okay';
    console.log(brendan);
}
console.log(brendan);
//Predicted outcome:
// var brendan = 'super cool';
// print() is not called;
// super cool

console.log("Problem #4");
var food = 'chicken';
console.log(food);
eat();
function eat(){
    food = 'half-chicken';
    console.log(food);
    var food = 'gone';
}
//Predicted Outcome:
// var food = 'chicken';
// chicken
// var food;
// food = 'half-chicken';
// half-chicken
// food = 'gone';

console.log("Problem #5");
// mean();
console.log(food);
var mean = function() {
    food = "chicken";
    console.log(food);
    var food = 'fish';
    console.log(food);
}
console.log(food);
//Predicted outcome:
// var mean;
// mean(); undefined
// undefined
// ndefined

console.log("Problem #6");
console.log(genre);
var genre = "disco";
rewind();
function rewind() {
    genre = "rock";
    console.log(genre);
    var genre = "r&b";
    console.log(genre);
}
//Predicted outcome:
// var genre
// undefined
//  genre = "disco"
// rewind();
// var genre;
// genre = "rock";
// rock
// genre = "r&b";
// r&b

console.log("Problem #7");
dojo = "san jose";
console.log(dojo);
learn();
function learn() {
    dojo = "seattle";
    console.log(dojo);
    var dojo = "burbank";
    console.log(dojo);
}
console.log(dojo);

//Predicted outcome;
// dojo = "san jose";
// san jose
// learn();
// var dojo;
// dojo = "seattle";
// seattle
// dojo = "burbank";
// burbank
// san jose







