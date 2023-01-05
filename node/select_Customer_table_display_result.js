//Create a node.js file that Select all records from the "customers" table, and display the result object on console.

var mysql = require('mysql');

var con = mysql.createConnection({
  host: 'localhost',
  user: "root",
  password: "nikhil96",
  database:'employee'
});

con.connect(function(err) {
  if (err) throw err;
  console.log("Connected!");
});

con.query('SELECT * FROM emp', (err,rows) => {
    if(err) throw err;
  
    console.log('Data received from Db:');
    console.log(rows);
  });
