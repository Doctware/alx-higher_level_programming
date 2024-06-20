#!/usr/bin/node
const args = process.argv.slice(2).map(Number);

if (args.length === 0 || args.length === 1) {
  console.log(0);
} else {
  let max = -Infinity;
  let seMax = -Infinity;

  for (const num of args) {
    if (num > max) {
      seMax = max;
      max = num;
    } else if (num > seMax && num !== max) {
      seMax = num;
    }
  }
  console.log(seMax !== -Infinity ? seMax : 0);
}
