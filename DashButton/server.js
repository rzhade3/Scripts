const DashButton = require('dash-button');
var dotenv = require('dotenv').load();

const MAC_ADDRESS = process.env.MAC_ADDRESS;
let button = new DashButton(MAC_ADDRESS);

var count = 1;

button.addListener(async () => {
	console.log("This worked " + count + " times");
	count += 1;
});