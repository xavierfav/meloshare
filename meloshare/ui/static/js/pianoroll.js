$(function() {
  var background = new Background();
  background.init();
});


function Background() {
  var height;
  var width;
  var canvas;
  var ctx;
  var stepBeat;
}

Background.prototype.init = function() {
  this.canvas = document.getElementById("background-canvas");
  this.ctx = this.canvas.getContext("2d");
  this.height = this.canvas.height;
  this.width = this.canvas.width;
  this.stepBeat = 20;

  this.drawAxis();
};

Background.prototype.drawAxis = function() {
  this.ctx.lineWidth = 0.5;
  this.ctx.beginPath();
  for (var i = 0; (i*this.stepBeat) < this.width; i++) {
    this.ctx.moveTo(i*this.stepBeat, 0);
    this.ctx.lineTo(i*this.stepBeat, this.height);
  }
  this.ctx.stroke();
};
