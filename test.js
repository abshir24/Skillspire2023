// Given an array with only 2 values. 
// create a function that swaps the places of those 2 values and 
// return the altered array. Given [1,2] return [2,1]

//  Array swap pairs. Swap positions of successive pairs of values of given array. 
//  If length is odd, do not change the final element. For [1,2,3,4], 
//  return [2,1,4,3]. For example, change input ["Brendan",true,42] to [true,"Brendan",42]. 
//  As with all array challenges, do this without using any built-in array methods.

function swap(arr){
    var temp = arr[0] 
    arr[0] = arr[1]
    arr[1] = temp
}


var arr = [1,2,3,4] // [2,1,4,3]