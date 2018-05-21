import express from "express";
import bodyParser from "body-parser"; // middleware to parse request body in req.body
import db from "./createdb.js"; // import database from file
import path from "path";

// Express set-up:
const app = express();
app.use(bodyParser.urlencoded({ extended: true })); 

app.use(express.static(path.join(__dirname, "../") + "client")); 

// Set up a get endpoint at "/" that renders index.html
app.get("/", (req, res) => {
	res.sendFile("index.html", {
		// The following line uses path middleware to set the absolute path
		// of index file "./" equivalent to the path at "../client"
		root: path.join(__dirname, "../") +"client"
	});
});

// Set up a post route at "/" endpoint
app.post("/", (req, res) => {
	// Check input, if it's not null, insert into database
	if(req.body.input.length >0){
		db.serialize(()=>{
			// Inserts a row into "inputs" table with the user input and the current date
			db.run("INSERT INTO inputs(txt, timestamp) VALUES(?, ?)",req.body.input, new Date(), function(err) {
				if (err) {
					return console.log(err.message);
				}
				console.log(`${this.changes} row inserted`);
			})
				// The following get command is not functionally necessary, but it proves that
				// user input is recorded in the database and logs it in the terminal
				.get(`SELECT * FROM inputs WHERE txt = "${req.body.input}"`, (err, row)=>{
					if (err) {
						return console.log(err.message);
					}
					console.log(`Input: "${row.txt}" recorded on ${Date(row.timestamp)}`);				
				});
          
		});
	}

	// Redirect to get endpoint --> clears submission form
	res.redirect("/");
});

// Open port at http://localhost:3000/
const port = process.env.PORT || 3000;
app.listen(port);
console.log("Server running at http://localhost:%d/", port);