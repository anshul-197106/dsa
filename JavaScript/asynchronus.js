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


function test(){
    let i=0;
    let interval = setInterval(() =>{
        console.log(i);
        i++;
        if(i==15){
            clearInterval(interval)
        }
    },1000)
}

test();