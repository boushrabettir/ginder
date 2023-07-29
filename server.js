// TODO - Update **routes.py** to this
// Was more comfortable with express, so I ended up
// Using this before applying it to Flask.

const express = require("express");
const cors = require("cors");
const bodyParser = require("body-parser");
const fetch = (...args) => {
  import("node-fetch").then(({ default: fetch }) => fetch(...args));
};

// Create instance of an express app
let app = express();

// Requests come from any origin
app.use(cors());

// Send data to express routes in json format
app.use(bodyParser.json());

app.get("/get_token", async (req, res) => {
  const headers = new Headers();
  headers.append("Accept", "application/json");

  const CLIENT_ID = process.env.CLIENT_ID || "";
  const REDIRECT_URI = process.env.REDIRECT_URI || "";
  const SCOPE = process.env.SCOPE || "";

  const PARAMS = `?client_id=${CLIENT_ID}&redirect_uri=${REDIRECT_URI}&scope=${SCOPE}`;
  await fetch(`https://github.com/login/oauth/authorize${PARAMS}`, {
    method: "POST",
    headers: {
      Accept: "application/json",
    },
  }) // TODO - Update NULL from the fetch request
    .then((res) => {
      return res.json();
    })
    .then((data) => {
      console.log(data);
      res.json(data);
    });
});

app.get("/get_user_data", async (req, res) => {
  // Fetchs users data once called by our front end

  const headers = new Headers();
  headers.append("Authorization", req.get("Authorization"));

  await fetch("https://api.github.com/user", {
    method: "GET",
    headers: headers,
  })
    .then((res) => {
      return res.json();
    })
    .then((data) => {
      console.log(data);
      res.json(data);
    });
});

app.listen(4000, () => {
  console.log("Running.");
});
