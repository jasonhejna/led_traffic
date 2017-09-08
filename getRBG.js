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

//http://localhost:8080/index.html
webshot('http://localhost:8080/index.html', 'yomap.png', options, function(err) {
  if (err) {
    console.log(err);
    return;
  }
  findrgb();
  // screenshot now saved to google.png
});

function findrgb(){
  Jimp.read("./yomap.png").then(function (image) {
    // do stuff with the image
    var x = 111;
    var y = 254;
    var pixelColor = image.getPixelColor(x, y);
    console.log('pixelColor', pixelColor);
    var pixelColorRGB = Jimp.intToRGBA(pixelColor);
    console.log('pixelColorRGB',pixelColorRGB);
  }).catch(function (err) {
    // handle an exception
    console.log(err);
  });
}