// aynchronous
// microstask queue(promises)  callback queue(callbacks)

//Callbacks :: function which can be return into another function as a parameter.

// function test(){
//     console.log("Fetching data...")
// }

// function data(callback){
//     callback();
//     console.log("Data Fetched...")
// }

// data(test)


// function test(){
//     console.log("HTML")
//     setTimeout(() => {
//         console.log("Javascript...")
//         setTimeout(() => {
//             console.log("Python")
//         },1000)
//         console.log("Kotlin...")
//         setTimeout(() => {
//             console.log("CSS")
//         },1000)
//     },500)
//     console.log("CSAS")
// }
// console.log(1);
// test();


// function test(){
//     let i=0;
//     let interval = setInterval(() =>{
//         console.log(i);
//         i++;
//         if(i==15){
//             clearInterval(interval)
//         }
//     },1000)
// }
// test();

// 13-02-2026


// obj = {
//     name: "Rahul",
//     age: 31,
// }
// console.log(obj)

// //JSON.stringify() -- object to json
// let str = JSON.stringify(obj);
// console.log(str)

// //JSON.parse()--> Json to object
// let obj2 = JSON.parse(str);
// console.log(obj2)


// Template-literals -- write statement with variables

// let a = "JAVAScript"
// console.log(`Hello This is ${a}`)

//Settime - creating delay at once
//Setintertval - repeating the function within a span of time
//Call back

// function test(){
//     setTimeout(() => {
//         console.log('HTML')     
//     },1000)
//     console.log("CSS")   //synchronous 1
//     setTimeout(() => {
//         setTimeout(()=> {
//             console.log("JS")  //3
//             setTimeout(()=>{
//                 setTimeout(()=>{
//                     setTimeout(()=>{
//                         console.log("callback hell...")
//                     })
//                 })
//             })
//         },1000)
//         console.log("Python")   
//     })
// }
// test()

//Promise - accept , running, reject
// let promise = new Promise((resolve, reject) =>{
//     setTimeout(() => {
//         resolve("Resolved");
//     },1000)
// })

// console.log(promise)
// .then((data) =>{
//     console.log(data)
// })
// .catch((err) =>{
//     console.log(err);
// })


// let promise = new Promise((resolve, reject) =>{
//     setInterval(() => {
//         resolve(1)
//     },1000)
// })

// .then((data) => {
//     console.log(data)
//     return data + 5;
// })
// .then((data) => {
//     console.log(data)
// })


// function test(){
//     return new Promise((resolve) => {
//         setTimeout(() => {
//             resolve("Promise is resolved")

//         },1000)
//     })
// }

// //async or await will be used when u using setTimeout in above function 
// async function data(){  //asyn
//     let res = await test();
//     console.log(res);
// }
// data();


//fetch the data from the server
// "https://jsonplaceholder.typicode.com/users" 

async function fetchData() {

    const output = document.getElementById("output");
    output.innerHTML = "Loading...";

    const response = await fetch("https://jsonplaceholder.typicode.com/users");
    const data = await response.json();

    console.log(data[0]);
    output.innerHTML = ""; 

    data.forEach((val) => {
        
    })
}