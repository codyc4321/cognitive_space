// alert("it works")

function myFunction() {
  // alert("inside my function")
  var img = document.createElement("img");
  img.src = '/images/file_2'
  document.body.appendChild(img);
  // document.getElementById('body').appendChild(img);
}

myFunction()
