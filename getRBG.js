// Uses webshot and phantom js to create image from supplied websites
//https://github.com/brenden/node-webshot

var webshot = require('webshot');
var options = {
  renderDelay: 15000,
  windowSize: {
    width:1920,
    height: 1080
  }
}
var Jimp = require("jimp");

function createImage() {
  webshot('http://localhost:8080/index.html', 'yomap.png', options, function (err) {
    if (err) {
      console.log(err);
      return;
    }
    // screenshot now saved to yomap.png
    // now call python script to update the LED strup
    
  });
}
createImage();
