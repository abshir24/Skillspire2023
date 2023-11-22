// [1,2,3,4,5,6,7,8] t = 7
//[4,5]

let window = (arr,target) =>{
    let output = []

    for(let i = 0;i<=arr.length-target;i++){
        let sum = 0
        for(let j = 0;j<target;j++){
            sum+=arr[i+j]
        }

        output.push(sum/target)
    }

    return output
}

console.log(window([1,2,3,4,5,6,7,8],7))