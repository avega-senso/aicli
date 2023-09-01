'use strict';

const fs = require('fs');

const write = function (callback) {
    fs.mkdir('./writeFolder', (err, data) => {
        if (err) return callback(err)
        fs.writeFile('./writeFolder/foobar.txt', 'Hello World!');
    });
}

write(console.log);
