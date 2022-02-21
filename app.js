const calculateSeconds = (colors) => {
    let seconds = colors.length * 2;
    for(let i = 1; i < colors.length; i++){
        if(colors[i] === colors[i-1]){
            continue;
        }
        seconds ++;
    }
    return seconds;
}

console.log(calculateSeconds(["Red", "Blue", "Red", "Blue", "Red"]) + " seconds")
console.log(calculateSeconds(["Blue"]) + " seconds")
console.log(calculateSeconds(["Red", "Yellow", "Green", "Blue"]) + " seconds")
console.log(calculateSeconds(["Blue", "Blue", "Blue", "Red", "Red", "Red"]) + " seconds")
