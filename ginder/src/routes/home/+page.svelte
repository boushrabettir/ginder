<script lang="ts">
  import { onMount } from 'svelte';
  import { user_data, local_storage_hold, retrieve_user_data, pop_new_project } from "$lib/data";
  import { retrieve_next_project_group } from './gh_data';
  import "../../app.css";
  import Swipe from '$lib/components/Swipe/Swipe.svelte';
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
  
  let userData: any;
  let isDataLoaded = false;

  onMount(async () => {
    await local_storage_hold();

    await retrieve_user_data();
    
    const unsuscribe = user_data.subscribe((v) => {
      userData = v;
      isDataLoaded=true;
    });
    console.log(userData);

    curr = pop_new_project();

    return unsuscribe;

  });
  
</script>

<html lang="en">
  <meta charset="utf-8">
  <head>
    <link href="/dist/output.css" rel="stylesheet">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>ginder</title>
  </head>

  <body>
    <div class="text-white flex justify-between ml-5 mr-5">
      <h1 class="flex inline-block align-middle ">ginder | 
        
          
          {#if isDataLoaded}
            <img src={userData["avatar_url"]} alt="Github profile" class=" inline-block align-middle h-24 w-24 scale-50 rounded-full"/>
            {userData["username"]}
          {:else}
            <p>Loading in your data..</p>
          {/if}
    
      </h1>
      <p>Like it? Swipe right. Don’t? Swipe left. It’s that simple.</p>
      <h1>Logout </h1>
   
    </div>

 
 
    <!-- <div class="container">
      <div class="post">
        <img src="/photos/github.png" alt="Github portfolio">
        <p><span id="bolded" class="text-white">thedaviddias/Front-End-Checklist •</span> thedaviddias</p>
        <button>+ Follow</button>
        <p id="title">Front-End-Checklist</p>
        <p id="subtext">🗂 The perfect Front-End Checklist for modern websites and meticulous developers</p>
        <p id="stats">🔤 <span id="bolded">Languages:</span> Python,Makefile</p>
        <p id="stats">⭐<span id="bolded">Stargazers:</span> 65819 • 📥<span id="bolded">Forks:</span> 6337 • 📝<span id="bolded">Contributers:</span> 116</p>
        <a href="/" id="view">View here!</a>
      </div> -->
    <!-- {#if curr}

      <p>{curr["owner"]} • {curr["username"]}</p>
      <button>+ Follow</button>
      <p>{curr["name"]}</p>
      <p>{curr["desc"]}</p>
      <p>Languages: {curr["languages"]}</p>
      <p>Stargazers: {curr["stars"]} • Forks: {curr["forks"]} • Contributers: {curr["contributers"]}</p>
    {/if} -->
      <!-- <button >{'<'}</button>
      <button >{'>'}</button> -->
      <!-- <button on:click={left}>{'<'}</button>
      <button on:click={right}>{'>'}</button> -->
    <!-- </div> -->
    
 
    <Swipe/>
    <div class="flex justify-center text-white gap-20 text-3xl mt-5 font-bold">
      <button on:click={left}>{'<'}</button>
      <button on:click={right}>{'>'}</button>
    </div>

</body>
</html>

<style lang="postcss">
  html, body {
      height: 100%;
      margin: 0;
      padding: 0;
  }
  body {
      background: linear-gradient(to bottom right, #11111b, #383843, #171721);
  }
  
  * {
    font-family: "Poppins", sans-serif;  
  }

  #circle-img {
    border-radius: 50%;
    width: 3rem;
    height: 3rem;
    margin-right: 0.5rem;
    vertical-align: middle;
  }

 
</style>

