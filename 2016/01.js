var steps = ["R4", "R1", "L2", "R1", "L1", "L1", "R1", "L5", "R1", "R5", "L2", "R3", "L3", "L4", "R4", "R4", "R3", "L5", "L1", "R5", "R3", "L4", "R1", "R5", "L1", "R3", "L2", "R3", "R1", "L4", "L1", "R1", "L1", "L5", "R1", "L2", "R2", "L3", "L5", "R1", "R5", "L1", "R188", "L3", "R2", "R52", "R5", "L3", "R79", "L1", "R5", "R186", "R2", "R1", "L3", "L5", "L2", "R2", "R4", "R5", "R5", "L5", "L4", "R5", "R3", "L4", "R4", "L4", "L4", "R5", "L4", "L3", "L1", "L4", "R1", "R2", "L5", "R3", "L4", "R3", "L3", "L5", "R1", "R1", "L3", "R2", "R1", "R2", "R2", "L4", "R5", "R1", "R3", "R2", "L2", "L2", "L1", "R2", "L1", "L3", "R5", "R1", "R4", "R5", "R2", "R2", "R4", "R4", "R1", "L3", "R4", "L2", "R2", "R1", "R3", "L5", "R5", "R2", "R5", "L1", "R2", "R4", "L1", "R5", "L3", "L3", "R1", "L4", "R2", "L2", "R1", "L1", "R4", "R3", "L2", "L3", "R3", "L2", "R1", "L4", "R5", "L1", "R5", "L2", "L1", "L5", "L2", "L5", "L2", "L4", "L2", "R3"];
visited = [];

var x = 0, y = 0;
var face = 0;

function findLoc() {
  steps.forEach((step) => {
    var d = step.slice(0,1);
    var steps = Number(step.slice(1));

    if (d == 'R') {
      face = turnRight();
    } else {
      face = turnLeft();
    }
    var newLoc;
    switch(face){
      case 0:
        for (var i=0; i<steps; i++) {
          y+=1;
          newLoc = ""+x+":"+y;
          if (visited.indexOf(newLoc) != -1) {
            console.log("found");
            console.log(newLoc);
            console.log(Math.abs(x) + Math.abs(y));
            visited.push(newLoc);
            return (Math.abs(x) + Math.abs(y));
          }
          visited.push(newLoc);
        }
        break;
      case 1:
        for (var i=0; i<steps; i++) {
          x+=1;
          newLoc = ""+x+":"+y;
          if (visited.indexOf(newLoc) != -1) {
            console.log("found");
            console.log(newLoc);
            console.log(Math.abs(x) + Math.abs(y));
            visited.push(newLoc);
            return (Math.abs(x) + Math.abs(y));
          }
          visited.push(newLoc);
        }
        break;
      case 2:
        for (var i=0; i<steps; i++) {
          y-=1;
          newLoc = ""+x+":"+y;
          if (visited.indexOf(newLoc) != -1) {
            console.log("found");
            console.log(newLoc);
            console.log(Math.abs(x) + Math.abs(y));
            visited.push(newLoc);
            return (Math.abs(x) + Math.abs(y));
          }
          visited.push(newLoc);
        }
        break;
      case 3:
        for (var i=0; i<steps; i++) {
          x-=1;
          newLoc = ""+x+":"+y;
          if (visited.indexOf(newLoc) != -1) {
            console.log("found");
            console.log(newLoc);
            console.log(Math.abs(x) + Math.abs(y));
            visited.push(newLoc);
            return (Math.abs(x) + Math.abs(y));
          }
          visited.push(newLoc);
        }
        break;
    }
  });
}


findLoc();

// console.log(visited);


// console.log("x: " + x + ", y: " + y);
// console.log(Math.abs(x) + Math.abs(y));

function turnRight() {
  if (3 >= face+1) {
    return face+1;
  }
  return 0;
}

function turnLeft() {
  if (face-1 >= 0) {
    return face-1;
  }
  return 3;
}