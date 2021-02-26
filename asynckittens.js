/*
Problem: We need to fetch lots of kitten images fast for our Machine Learning algorithm.

Download 128 images of various sizes from https://placekitten.com/. However, when you fetch the images,
do so asynchronously so that you can send off all the requests and then wait for the results to come back.

Then generate a static HTML page or dynamic page in the browser that shows off all your newly fetched images.

https://www.hacksparrow.com/nodejs/using-node-js-to-download-files.html

*/

var fs = require('fs');
var url = require('url');
var http = require('http');
var exec = require('child_process').exec;
var spawn = require('child_process').spawn;

var DOWNLOAD_DIR = './downloads/';

var generate_width_and_height = function() {
  const random = Math.floor((Math.random() * 100) + 200);
  console.log(random);
  return random
}


var create_file_url = function() {
  return "http://placekitten.com/" + generate_width_and_height() + "/" + generate_width_and_height()
}


var download_file_wget = function(file_url, file_number) {
  // extract the file name
  var file_name = "file_" + file_number
  // compose the wget command
  var wget = 'wget -P ' + DOWNLOAD_DIR + ' ' + file_url;
  // excute wget using child_process' exec function

  var child = exec(wget, function(err, stdout, stderr) {
    if (err) throw err;
    else console.log(file_name + ' downloaded to ' + DOWNLOAD_DIR);
  });
};

var download_file = function(file_number) {
    download_file_wget(create_file_url(), file_number);
}

// download_file(1)


function saveFile(url, number) {
  console.log(url)
  return new Promise(function(resolve, reject) {
    download_file_wget(url, 1)
  }).then(function(xhr) {
    console.log('downloaded')
  });
}

function download(urls) {
  let promises = []
  for (var i = 0; i <= 1; i++) {
    promises.push(saveFile(urls[i], i));
  }

  return Promise.all(promises);
}

download(["http://placekitten.com/300/300", "http://placekitten.com/250/250"])
