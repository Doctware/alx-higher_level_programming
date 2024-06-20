#!/usr/bin/node
function factorial (n) {
  if (isNaN(n)) {
    return 1;
  }
  if (n === 0) {
    return 1;
  }

  return n * factorial(n - 1);
}

const args = process.argv.slice(2);
const n = Math.floor(Number(args[0]));

console.log(factorial(n));
