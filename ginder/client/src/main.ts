// main.ts
import "./root.css";
import App from "./App.svelte";
import Login from "./Login.svelte";

const app = new App({
  target: document.getElementById("app"),
});

// Code to handle the new route
if (window.location.pathname === "/another") {
  new Login({
    target: document.getElementById("login"),
  });
}

export default app;
