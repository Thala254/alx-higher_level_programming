#!/usr/bin/node
const argv = parseInt(process.argv[2]);
const factorial = n => {
  if (isNaN(n) || n === 0) return 1;
  else return n * factorial(n - 1);
};
console.log(factorial(argv));
