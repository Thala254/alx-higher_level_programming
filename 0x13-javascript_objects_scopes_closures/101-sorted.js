#!/usr/bin/node
const dict1 = require('./101-data.js').dict;
let newDict = {};
for (let key in dict1) {
  if (newDict[dict1[key]] === undefined) {
    newDict[dict1[key]] = [];
  }
  newDict[dict1[key]].push(key);
}
console.log(newDict);
