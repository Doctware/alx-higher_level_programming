#!/usr/bin/node
const args = process.argv.slice(2);
const myNum = Math.floor(Number(args[0]));

if (isNaN(myNum)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < myNum; i++) {
    console.log('C is fun');
  }
}
