// Create a function that accepts an array as a parameter and multiplies every 
// value in that array. Return the same array at the end of the function. 

function arr (parameter){

    for(i = 0; i < parameter.length; i++){
  
      parameter[i] = parameter[i] * 2;
  
    }
  
    return parameter
  
  }
  
  console.log(arr([1, 2]))

// Create a function that accepts an array as a parameter and returns 
// the average value of all the numbers in that array. To find the average 
// take the sum of all numbers in the array and divide it by the length of the array.
// Example: [1,2,3,4,5]
function findAverage(array){
    var sum = 0

    for(let i = 0;i < array.length;i++){
        sum += arr[i]
    }

    var average = sum / arr.length // 15 / 5 = 3

    return average
}

findAverage([1,2,3,4,5])

