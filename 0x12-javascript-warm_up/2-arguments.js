#!/usr/bin/node
const len = process.argv.length - 2;
const print = console.log;

if (!len) print('No argument');
if (len === 1) print('Argument found');
if (len > 1) print('Arguments found');
