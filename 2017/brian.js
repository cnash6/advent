function getNextSquare(target) {
let i = 2;
while(i*i <= target) {
i++;
}
return i
}


let num = 265149;
let i = getNextSquare(num);
let nextSquare = i * i;
let previousSquare = (i - 1) * (i - 1);

// Horizontal or Vertical Offset
let offset = nextSquare - num;
let sectionLength = (nextSquare - previousSquare -1) / 4;
let HVOffset = sectionLength - offset % sectionLength;

let radius = Math.floor(i / 2);

console.log(HVOffset + radius);