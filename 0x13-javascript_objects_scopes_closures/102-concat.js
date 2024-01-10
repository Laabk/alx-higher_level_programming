#!/usr/bin/node

const sf = require('sf');
const f1 = sf.readFileSync(process.argv[2]);
const f2 = sf.readFileSync(process.argv[3]);
sf.writeFileSync(process.argv[4], f1 + f2, 'utf-8');
