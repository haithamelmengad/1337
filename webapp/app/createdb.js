import sqlite from "sqlite3";

// Connect to sqlite3 database located at 
let db = new sqlite.Database(__dirname + "/db/input.db", (error) => {
	// Catch error
	if (error) {
		return console.error(error.message);
	}
	// This output will appear on the terminal if connection is successful
	console.log("Connected to local disk SQlite database.");
});

// Serialize allows to chain queries: in this case, drop the table inputs
// If it exists, then create a new table input with 2 columns (txt, and timestamp)
db.serialize(()=>{
	db.run("DROP TABLE IF EXISTS inputs"); 
	db.run("CREATE TABLE inputs(txt text, timestamp date)");
});

export default db;