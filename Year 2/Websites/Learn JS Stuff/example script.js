// Basics
let name = "Alice"; // Block scoped
const age = 30; // Cannot be reassigned
var city = "New York" // Function scoped

// Operators
let result = (5 + 10) * 3; // 45
let isEqual = 5 === 5; // true
let isNotEqual = 5 !== "5"; // true

// For loop
for (let i=0; i < 5; i++) {
    console.log(i);
}

// While loop
let counter = 0;
while (counter < 5) {
    console.log(counter);
    counter++;
}

// Switch-case
let day = "Monday";
switch (day) {
    case "Monday":
        console.log("Start of the week");
        break; // Required
    case "Friday":
        console.log("End of the week");
        break; // Required
    default: // Not required
        console.log("Regular day");
}

// Objects
let person = {
    name: "Alice",
    age: 25,
    greet: function (who) {
        console.log(`Hello ${who}!`);
    }
}
console.log(person.name);
person.greet("Bob");

// Arrays
let fruits = ["Apple", "Banana", "Orange"];
console.log(fruits[0]);

fruits.push("Mango");

for (let fruit of fruits) {
    console.log(fruit);
}