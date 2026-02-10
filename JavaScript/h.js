// JAVASCRIPT -- Dynamic Behaviour, Asynchronous,
// single threading(one task at one time)
// alert("External JS..")


// var a = 20;           //functional scope, re-declare and re assign
// let b = "Hello";      //block scope
// const c = 30;         //block scope
// console.log(a)

// function hello(){
    //     var x = 1;
    //     if(x){
        //         let a = 20;
        //     }
        //     console.log(a)
        // }
        // hello();
 

// var a = 50;
// var a = 40;
// console.log(a)


// let a = 20;          // global
// function hello(){
//     let a = 30;     // local
//     console.log(a)
// }
// hello()


// const a = 50;
// console.log(a)


// test(10, 20);
// function test(a, b){
//     console.log(a+ b)
// }
// test(10, 20);


// Hoisting -- var function --> you can use function or varaiable with var before declaration
// var a = 10;
// console.log(a);
// a = 20;

// // Arrow Functions :: 
// test = () => {
//     console.log("Functions...")
// }
// test()

// create a function from arrow function which display the fun message
// const message = () => {
//   const name = prompt("Enter your name");
//   alert(`Hello ${name}!`);
// }
// message();

// const userName = () => {
//   a = prompt("Enter your name: ")
//   return a;
// }
// userName();

// for ( let i = 0; i <=5; i++){
//   console.log(i);
// }

// var num = 4;
// let res = num%2==0 ? "even": "odd";
// console.log(res)


//getElementByID()
//getElementsByClassName()
//getElementByTagName()
//querySelector()
//querySelectorAll()

// let headingOne = document.getElementById("head");
// headingOne.style.color="red";


// var headClass = document.getElementsByClassName("headClass");
// headClass[1].style.color = "red";
// console.log(headClass.length);

//!getElementByID

// let head = document.getElementById("head");
// head.style.color = "red";

//!getElementClassName

// let head = document.getElementsByClassName("headClass");
// - - head[1].style.color = "red"
// for(let i=0; i<head.length; i++){
//     head[i].style.color = "red";
// }

//!getElementByTagName
// let head = document.getElementsByTagName("h1")
// head[0].style.color = "red";


//! Query Selector

//ID
// let head = document.querySelector("#head");
// head.style.color = "red";

//CLASS
// let head = document.querySelector(".headClass");
// head.style.color = "red";

//Tag
// let head = document.querySelector("h2");
// head.style.color = "red";

//querySelectorAll
// let head = document.querySelector("h3");
// head.style.color = "red";


// document.getElementById("head").innerHTML = "This is Heading";

// let div = document.getElementById("div");

// let p = document.createElement("p");
// div.append(p);
// p.innerHTML = "Paragraph"

// p.classList.add("para"); 


// let main = document.getElementById("main");

// const handleClick = () => {
//     if (main.style.display === "none") {
//         main.style.display = "block";
//     } else {
//         main.style.display = "none";
//     }
// };

colors = ["red", "blue", "green", "orange", "purple", "black"];
i = 0;

const handleClick = () => {
    // i = i + 1;
    // document.getElementById("main").style.backgroundColor = colors[i];

    const randomIndex = Math.floor(Math.random() * colors.length);
    document.getElementById("main").style.backgroundColor = colors[randomIndex];
}