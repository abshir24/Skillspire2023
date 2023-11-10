// Create a function that accepts an array of numbers 
// if the number is 0 or negative, change the number to a string
// that says "buffer"
// And adds 5 to every number in the array. 
// return the updated array 

function addFives(numbers){
    for(let i = 0; i < numbers.length; i++){
        if(numbers[i] <= 0){
            numbers[i] = "buffer"
        }else{
            numbers[i] += 5
        }
    }

    return numbers
}


var removeAt = function(arr, index){
    var temp = arr[index];
    
    for(var i = index; i < arr.length-1; i++){
        arr[i] = arr[i+1];
    }
    arr.pop()

    return temp
}

console.log(removeAt([1,2,3,4,5,6,7,8,9,10], 5));