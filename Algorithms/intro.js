// Create a function that accepts an array as a parameter and multiplies every 
// value in that array. Return the same array at the end of the function. 

function arr (parameter){

    for(i = 0; i < parameter.length; i++){
  
      parameter[i] = parameter[i] * 2;
  
    }
  
    return parameter
  
  }
  
  // console.log(arr([1, 2]))

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

// findAverage([1,2,3,4,5])

function stringCap(arr){

  let string = ""

  for(i = 0; i < arr.length; i++){
      console.log("Before Adding Charachter: " + arr[i])
      string += arr[i].toUpperCase()
      console.log("After Adding Charachter: " + arr[i])
  }
  return string
}

// capword = "hey"

// console.log(stringCap(capword))

function pushFront(arr,val){
  arr.push(val)

  for(let i = arr.length - 1; i>0; i--){
    let temp = arr[i] 
    arr[i] = arr.length[0]
    arr[i-1] = temp
    
    [1,3,4,5,2]
  }


  return arr
}


// console.log(pushFront(test, 1))

// test.pop()

// console.log(test)

