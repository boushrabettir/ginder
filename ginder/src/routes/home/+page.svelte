<script lang="ts">
  import { onMount } from 'svelte';
  import { user_data, local_storage_hold, retrieve_user_data, pop_new_project } from "$lib/data";
  import { retrieve_next_project_group } from './gh_data';
  import "../../app.css";

  let curr: any;

  /**
   * right adds the next data object to the right swipes
   * for the reccomendation system and retrieves the next block
   */
  const right = () => {
    if (localStorage.getItem("right-swipes") == undefined || localStorage.getItem("right-swipes") == null) {
      localStorage.setItem("right-swipes", JSON.stringify([curr]));
    } else {
      let right_swipe_data = JSON.parse(localStorage.getItem("right-swipes") || "[]");
      console.log(right_swipe_data);
      right_swipe_data.push(curr);
      localStorage.setItem("right-swipes", JSON.stringify(right_swipe_data));
    }

    curr = pop_new_project();
  
    /**
     * Determines whether or not new data should be added
     * into the list
    */
    if (JSON.parse(localStorage.getItem("right-swipes") || "[]")?.length === 5) {
      retrieve_next_project_group();
    }
    
  }

  /**
   * left retrieves the next data block
   */
  const left = () => {
    curr = pop_new_project();
  }

  
  onMount(async () => {
    local_storage_hold();

    await retrieve_user_data();
    
    curr = pop_new_project();

    console.log(user_data);
  });

</script>

<html lang="en">
  <meta charset="utf-8">
  <head>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@0.9.4/css/bulma.min.css">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>ginder</title>
  </head>


  <body>
    <div class="header">
      <h1>ginder | <span id="user-img"><img src="/photos/boush.png" alt="Github profile" id="circle-img"/>@{user_data["username"]}</span></h1>
      <p>Like it? Swipe right. Don’t? Swipe left. It’s that simple.</p>
      <h1>Logout</h1>
    </div>

    <div class="container">
      <div class="post">
        <img src="/photos/github.png" alt="Github portfolio">
        <p><span id="bolded">thedaviddias/Front-End-Checklist •</span> thedaviddias</p>
        <button>+ Follow</button>
        <p id="title">Front-End-Checklist</p>
        <p id="subtext">🗂 The perfect Front-End Checklist for modern websites and meticulous developers</p>
        <p id="stats">🔤 <span id="bolded">Languages:</span> Python,Makefile</p>
        <p id="stats">⭐<span id="bolded">Stargazers:</span> 65819 • 📥<span id="bolded">Forks:</span> 6337 • 📝<span id="bolded">Contributers:</span> 116</p>
        <a href="/" id="view">View here!</a>
      </div>
    <!-- {#if curr}

      <p>{curr["owner"]} • {curr["username"]}</p>
      <button>+ Follow</button>
      <p>{curr["name"]}</p>
      <p>{curr["desc"]}</p>
      <p>Languages: {curr["languages"]}</p>
      <p>Stargazers: {curr["stars"]} • Forks: {curr["forks"]} • Contributers: {curr["contributers"]}</p>
    {/if} -->

      <button on:click={left}>{'<'}</button>
      <button on:click={right}>{'>'}</button>
    </div>

</body>
</html>

<style lang="postcss">

  :global(html) {
    background-color: theme(colors.gray.100);
  }
  
  * {
      font-family: "Poppins", sans-serif;  
  }
  /* #circle-img {
    border-radius: 50%;
    width: 3rem;
    height: 3rem;
    margin-right: 0.5rem;
    vertical-align: middle;
  }

  h1 {
    font-size: 2rem;
    font-weight: 600;
  }

  .header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin: 1rem;
  }
  
  #user-img {
    font-size: 1.2rem;
  }
  
  .container {
    text-align: center;
  }

  #bolded {
    font-weight: 600;
  }

  #title {
    text-transform: uppercase;
    font-weight: 800;
    font-size: 1.5rem;
  }

  .post {
    background-color: #222222;
    color: white;
    padding: 3rem;
  }
  .container {
   width: 30rem;
    
  } */

</style>

