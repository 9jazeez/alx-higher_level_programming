#!/usr/bin/node

let size = process.argv[2];
let shape = '';
size = parseInt(size);
if (isNaN(size))
{
	console.log('Missing size');
}
else
{
	for (let i = 0; i < size; i = i + i)
	{
		for (let j = 0; j < size; j = 1 + j)
		{
			shape += 'X';
		}
		console.log(shape);
	}
}
