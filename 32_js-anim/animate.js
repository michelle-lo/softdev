// Team MJ :: Michelle Lo, Josephine Lee
// SoftDev pd2
// K31 -- Paint Paint Paint...
// 2022-02-16t

// model for HTML5 canvas-based animation

// SKEELTON


//access canvas and buttons via DOM
//access canvas and buttons via DOM
var c = document.getElementById("playground");
var dotButton = document.getElementById("buttonCircle");
var stopButton = document.getElementById("buttonStop");
var logoButton = document.getElementById("buttonLogo");

//prepare to interact with canvas in 2D
var ctx = c.getContext("2d");

//set fill color to team color
ctx.fillStyle = "pink";

var requestID;  //init global var for use with animation frames


//var clear = function(e) {
var clear = (e) => {
    console.log("clear invoked...")
    ctx.clearRect(0, 0, c.clientWidth, c.clientHeight);
};


var radius = 0;
var growing = true;


//var drawDot = function() {
var drawDot = () => {
    console.log("drawDot invoked...")

    window.cancelAnimationFrame(requestID);
    requestID = window.requestAnimationFrame(drawDot);

    clear();
    ctx.beginPath();

    if (radius == c.clientWidth/2 || radius < 0) {
        growing = !growing;
    }

    if (growing) {
        radius += 2;
    } else {
        radius -= 2;
    }

    ctx.arc(c.clientWidth/2, c.clientHeight/2, radius, 0, 360);
    ctx.fill();

    // YOUR CODE HERE

    /*
      ...to
      Wipe the canvas,
      Repaint the circle,
      ...and somewhere (where/when is the right time?)
      Update requestID to propagate the animation.
      You will need
      window.cancelAnimationFrame()
      window.requestAnimationFrame()
     */
};


//var stopIt = function() {
var stopIt = () => {
    console.log("stopIt invoked...")
    console.log(requestID);

    window.cancelAnimationFrame(requestID);
    // YOUR CODE HERE
    /*
      ...to
      Stop the animation
      You will need
      window.cancelAnimationFrame()
    */
};


let myImage = new Image(100, 50);
myImage.src = 'logo_dvd.jpg';
  //document.body.appendChild(myImage);
  /* function getRandomInt(max) {
    return Math.floor(Math.random() * max);
  } */

let xVel = -1;
let yVel = 3;
let dx = Math.floor(Math.random() * (c.width - myImage.width));
let dy = Math.floor(Math.random() * (c.height - myImage.height));


let dvd = () => {

  console.log("DVD!");
  requestID = window.cancelAnimationFrame(requestID);
  clear();
  ctx.beginPath();

  ctx.drawImage(myImage, dx, dy, 100, 50); 


  if (dx >= c.width - myImage.width || dx <= 0) {
		xVel *= -1;
	}

  if (dy >= c.height - myImage.height || dy <= 0) {
		yVel *=-1;
	}

  dx += xVel;
  dy += yVel;

  // ctx.arc(c.clientWidth/2, c.clientHeight/2, radius, 0, 360);
  requestID = window.requestAnimationFrame(dvd);
  //ctx.fill();

}
//dvd();


dotButton.addEventListener("click", drawDot);
stopButton.addEventListener("click", stopIt);
logoButton.addEventListener("click", dvd);
