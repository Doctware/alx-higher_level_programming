#!/usr/bin/node
function add (a, b) {
  return a + b;
}

const args = process.argv.slice(2);
const myNum0 = Math.floor(Number(args[0]));
const myNum1 = Math.floor(Number(args[1]));

console.log(add(myNum0, myNum1));
