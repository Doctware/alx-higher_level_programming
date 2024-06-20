#!/usr/bin/node
const args = process.argv.slice(2);
const myX = Math.floor(Number(args[0]));

if (isNaN(myX)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < myX; i++) {
    let row = '';
    for (let j = 0; j < myX; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
