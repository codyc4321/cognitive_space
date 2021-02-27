/*
Problem: We need to fetch lots of kitten images fast for our Machine Learning algorithm.

Download 128 images of various sizes from https://placekitten.com/. However, when you fetch the images,
do so asynchronously so that you can send off all the requests and then wait for the results to come back.

Then generate a static HTML page or dynamic page in the browser that shows off all your newly fetched images.

*/

var fs = require('fs');
// var url = require('url');
var http = require('http');
var exec = require('child_process').exec;

var DOWNLOAD_DIR = './images/';

var generate_width_and_height = function() {
  const random = Math.floor((Math.random() * 100) + 200);
  return random
}


var create_file_url = function() {
    return "http://placekitten.com/" + generate_width_and_height() + "/" + generate_width_and_height();
}

// https://www.hacksparrow.com/nodejs/using-node-js-to-download-files.html
var download_file_wget = function(file_url, file_number) {
    var file_name = "file_" + file_number;

    var wget = 'wget -O ' + DOWNLOAD_DIR + '/file_' + file_number + ' '+ file_url;

    var child = exec(wget, function(err, stdout, stderr) {
        if (err) throw err;
        else console.log(file_name + ' downloaded to ' + DOWNLOAD_DIR);
    });
};

var download_file = function(file_number) {
    download_file_wget(create_file_url(), file_number);
}


function saveFile(url, number) {
    console.log(url)
    return new Promise(function(resolve, reject) {
        download_file_wget(url, number)
    }).then(function(xhr) {
        console.log('downloaded file ' + number)
    });
}

function download_files() {
    let promises = []
    for (var i = 0; i <= 128; i++) {
        promises.push(saveFile(create_file_url(), i));
    }

    return Promise.all(promises);
}


download_files()


// https://nodejs.org/en/knowledge/HTTP/servers/how-to-serve-static-files/
http.createServer(function (req, res) {
  fs.readFile(__dirname + req.url, function (err, data) {
    if (err) {
      res.writeHead(404);
      res.end(JSON.stringify(err));
      return;
    }
    res.writeHead(200);
    res.end(data);
  });
}).listen(3000);
