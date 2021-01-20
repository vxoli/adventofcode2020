// Reading the file and converting it to int
const fs = require('fs')
var ipt = fs.readFileSync("d01p1-input.txt", 'utf8').split("\n").filter(x => x.length != 0);
ipt = ipt.map(x => parseInt(x));
// Doing the combn
var ipt2 = ipt;
var comb = ipt.flatMap(i => ipt2.map(j => [i, j]))
// Getting the 2020
var twentytwenty = comb.filter(x => (x[0] + x[1]) === 2020)
// Solution
twentytwenty.reduce(y => y[0] * y[1])
// Same with three
var ipt3 = ipt;
var comb2 = ipt.flatMap(i => ipt2.flatMap(j => ipt3.map(k => [i, j, k])));
// Doing the computation
var twentytwenty2 = comb2.filter(x => (x[0] + x[1] + x[2]) === 2020)
// Solution
twentytwenty2.map(y => y[0] * y[1] * y[2])[0]
