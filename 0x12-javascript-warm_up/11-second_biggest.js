#!/usr/bin/node

function sec (a) {
  let tmp;
  if (a.length === 3 || a.length < 3) {
    console.log(0);
  } else {
    for (let i = 2; i < a.length; i += 1) {
      for (let j = 2; j < a.length; j += 1) {
        if (parseInt(a[j]) < parseInt(a[j + 1])) {
          tmp = a[j + 1];
          a[j + 1] = a[j];
          a[j] = tmp;
        }
      }
    }
    console.log(a[3]);
  }
}

const val = process.argv;
sec(val);
