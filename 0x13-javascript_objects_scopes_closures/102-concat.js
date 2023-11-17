#!/usr/bin/node

// a script that concats 2 files
const args = process.argv;
const fileA = args[2];
const fileB = args[3];
const file = require('fs');
const contentA = file.readFileSync(fileA, 'utf8');
const contentB = file.readFileSync(fileB, 'utf8');
const fileC = args[4];
file.writeFileSync(fileC, contentA +contentB);
