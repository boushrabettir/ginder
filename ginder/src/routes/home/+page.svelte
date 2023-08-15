<script lang="ts">
  import { onMount } from 'svelte';
  import { user_data, local_storage_hold, retrieve_user_data, pop_new_project, determine_next_step } from "$lib/data";
  import { retrieve_next_project_group, add_project_to_stars } from './gh_data';
  import Swipe from '$lib/components/Swipe/Swipe.svelte';
  import Loading from '$lib/components/Loading/Loading.svelte';
  import "../../app.css";
  

  let curr: any;
  let data_user: any;
  let is_data_loaded = false;
  
  /**
   * right adds the next data object to the right swipes
   * for the reccomendation system and retrieves the next block
   */

   //TODO Update so it doesnt appropriate DRY.
  const right = async () => {

    if (localStorage.getItem("all") == null || localStorage.getItem("all") == undefined) {
      localStorage.setItem("all", JSON.stringify([curr]));
    } else {
      let right_swipe_data = JSON.parse(localStorage.getItem("all") || "[]");
      right_swipe_data.push(curr);
      localStorage.setItem("all", JSON.stringify(right_swipe_data));
      
    }

    if (localStorage.getItem("stars") == null || localStorage.getItem("stars") == undefined) {
      localStorage.setItem("stars", JSON.stringify([curr]));
    } else {
      let right_swipe_data = JSON.parse(localStorage.getItem("stars") || "[]");
      right_swipe_data.push(curr);
      localStorage.setItem("stars", JSON.stringify(right_swipe_data));
      
    }

    // Adds projects to stars list on Github profile
    await add_project_to_stars();


    if (localStorage.getItem("right-swipes") == undefined || localStorage.getItem("right-swipes") == null) {
      localStorage.setItem("right-swipes", JSON.stringify([curr]));
      
    } else {
      let right_swipe_data = JSON.parse(localStorage.getItem("right-swipes") || "[]");
      right_swipe_data.push(curr);
      localStorage.setItem("right-swipes", JSON.stringify(right_swipe_data));
    }

    curr = pop_new_project();
  
    // Determines whether or not new data should be added into the list 
    if (JSON.parse(localStorage.getItem("right-swipes") || "[]")?.length === 5) {
      retrieve_next_project_group();
    } else {
      await determine_next_step();
    }

    
    
  }

  /**
   * left retrieves the next data block
   */
  const left = async () => {
    
    if (localStorage.getItem("all") == null || localStorage.getItem("all") == undefined) {
      localStorage.setItem("all", JSON.stringify([curr]));
    } else {
      let right_swipe_data = JSON.parse(localStorage.getItem("all") || "[]");
      right_swipe_data.push(curr);
      localStorage.setItem("all", JSON.stringify(right_swipe_data));
      
    }

    curr = pop_new_project();
    await determine_next_step();
  }
  

  onMount(async () => {
    await local_storage_hold();

    await retrieve_user_data();
    
    const unsuscribe = user_data.subscribe((v: any) => {
      data_user = v;
      is_data_loaded=true;
    });
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
    <div class="text-white flex justify-between items-center ml-14 mr-14">
      <h1 class="flex items-center gap-0">
          <span class="text-3xl">ginder |</span>        
          {#if is_data_loaded}
              <img src={data_user["avatar_url"]} alt="Github profile" class="h-24 w-24 scale-50 rounded-full"/>
              <span >@{data_user["username"]}</span>
          {:else}
              <p>Loading in your data...</p>
          {/if}
      </h1>
      <p>Like it? Swipe right. Don’t? Swipe left. It’s that simple.</p>
      <h1>Logout</h1>
  </div>

 
    {#if curr && JSON.parse(localStorage.getItem("projects") || "[]").length > 0}
      <Swipe
        username={curr["username"]}
        followers={curr["followers"]}
        repo_title={curr["name"]}
        description={curr["desc"]}
        languages={curr["languages"]}
        stargazers={curr["stars"]}
        forks={curr["forks"]}
        contributers={curr["contributers"]}
        link={curr["link"]}
      />

      <div class="flex justify-center text-white gap-20 text-3xl mt-5 font-bold">
        <button on:click={left}>{'<'}</button>
        <button on:click={right}>{'>'}</button>
      </div>
    {:else}
      <Loading />
    {/if}



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
 
</style>

