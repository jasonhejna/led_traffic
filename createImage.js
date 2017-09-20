// Uses webshot and phantom js to create image from supplied websites
//https://github.com/brenden/node-webshot

var webshot = require('webshot');
var cmd = require('node-cmd');
//var Jimp = require("jimp");

var options = {
  renderDelay: 19000,
  windowSize: {
    width:1920,
    height: 1080
  }
}

function createImage() {
  webshot('http://localhost:8080/index.html', 'yomap.png', options, function (err) {
    if (err) {
      console.log(err);
      return;
    }
    // screenshot now saved to yomap.png
    // now call python script to update the LED strup
    runPython();
  });
}

function runPython() {
  cmd.get(
      'sudo python led_control/updateled.py',
      function(err, data, stderr){
        console.log('err:', err);
        console.log('stderr:', stderr);
        console.log('python data:',data);
      }
  );
}

createImage();
