// Create a node.js file that Select all records from the "customers" table, and delete the specified record.

var mysql = require('mysql');
var con = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "nikhil96",
  database: "employee"
});
con.connect(function(err) {
  if (err) throw err;
  var sql = "DELETE FROM emp WHERE name = 'dada'";
  con.query(sql, function (err, result) {
    if (err) throw err;
    console.log("Number of records deleted: " + result.affectedRows);
  });
});
