#!/usr/bin/node
const args = process.argv.slice(2);
const fArg = args[0];
const number = Math.floor(Number(fArg));

if (isNaN(number)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${number}`);
}
