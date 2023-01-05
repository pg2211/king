//Create a Node.js file that demonstrate create database and table in MySQL

var mysql = require('mysql');  
var con = mysql.createConnection({  
host: "localhost",  
user: "root",  
password: "nikhil96",
database: "Node"  
});  
con.connect(function(err) {  
if (err) throw err;  
console.log("Connected!");  
con.query("CREATE DATABASE WFN", function (err, result) {  
if (err) throw err;  
console.log("Database created");  
});  
});  

var sql = "CREATE TABLE customers2(name VARCHAR(25), address VARCHAR(25))";
con.query(sql, function (err, result) {
  if (err) throw err;
  console.log("Table created");
});
