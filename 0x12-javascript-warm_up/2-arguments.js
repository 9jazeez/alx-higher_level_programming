#!/usr/bin/node

const myVar = process.argv;
if (myVar.length === 2)
{
	console.log('No Argument');
}
else
{
	console.log('Argument found');
}
//console.log(myVar[2]);
