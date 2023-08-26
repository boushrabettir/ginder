<script lang="ts">
  import { onMount } from 'svelte';
  import { user_data, local_storage_hold, retrieve_user_data, pop_new_project, determine_next_step } from "$lib/data";
  import { retrieve_next_project_group, add_project_to_stars } from './gh_data';
  import { final_response, determine_message } from "./responses";
  import Swipe from '$lib/components/Swipe/Swipe.svelte';
  import Loading from '$lib/components/Loading/Loading.svelte';
  import Notification from '$lib/components/Notification/Notification.svelte';
  import "../../app.css";
  

  let curr: any;
  let data_user: any;
  let is_data_loaded = false;
  
  /**
   * local_storage_get_and_set is a helper function
   * to get/set local storage data
  */
  const local_storage_get_and_set = (local_name: string) => {
    
    if (localStorage.getItem(local_name) == null || localStorage.getItem(local_name) == undefined) {
      localStorage.setItem(local_name, JSON.stringify([curr]));
    } else {
      let right_swipe_data = JSON.parse(localStorage.getItem(local_name) || "[]");
      right_swipe_data.push(curr);
      localStorage.setItem(local_name, JSON.stringify(right_swipe_data));  
    }
  };

  /**
   * right adds the next data object to the right swipes
   * for the reccomendation system and retrieves the next block
   */
  const right = async () => {
 
    local_storage_get_and_set("all");
    local_storage_get_and_set("stars");

    // Adds projects to stars list on Github profile
    await add_project_to_stars();

    local_storage_get_and_set("right-swipes");

    curr = pop_new_project();
  
    // Determines whether or not new data should be added into the list 
    if (JSON.parse(localStorage.getItem("right-swipes") || "[]")?.length === 5) {
      retrieve_next_project_group();
    } else {
      await determine_next_step();
    }

  };

  /**
   * left retrieves the next data block
   */
  const left = async () => {
    local_storage_get_and_set("all");
    curr = pop_new_project();
    await determine_next_step();
  }
  

  if (curr) {
    determine_message(curr["stars"]);
  }
  

  onMount(async () => {

    await local_storage_hold();


    await retrieve_user_data();
  
    
    
    const unsuscribe = user_data.subscribe((v: any) => {
      data_user = v;
      is_data_loaded = true;
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

  <body class="selection:bg-sky-300 selection:text-sky-700">
    <div class="text-white flex justify-between items-center ml-14 mr-14">
      <h1 class="flex items-center gap-0">
          <span class="text-3xl font-bold">ginder |</span>        
          {#if is_data_loaded}
              <img src={data_user["avatar_url"]} alt="Github profile" class="h-24 w-24 scale-50 rounded-full"/>
              <span >@{data_user["username"]}</span>
          {:else}
              <p>Loading in your data...</p>
          {/if}
      </h1>
      <p class="font-bold">Like it? Swipe right. Don’t? Swipe left. It’s that simple.</p>

  </div>

    <Notification />
    
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
        pfp_photo={curr["profile_picture"]}
      />
      
      <div class="flex justify-center text-white gap-20 text-3xl mt-24 font-bold">
        <button on:click={left}>{'<'}</button>
        <button on:click={right}>{'>'}</button>
      </div>

      <p class="text-center text-sky-300 text-sm">{final_response}</p>
      
    {:else}
      <div class="blurry-bg">
        <Loading />
      </div>
    {/if}



</body>
</html>

<style lang="postcss">
  html, body {
      height: 100%;
      margin: 0;
      padding: 0;
  }

  @keyframes movingGradient {
            0% {
                background-position: 0% 0%;
            }
            50% {
                background-position: 100% 100%;
            }
            100% {
              background-position: 0% 0%;
            }
    }

  body {
      animation: movingGradient 25s linear infinite;
      background: linear-gradient(to bottom right, #0a0a0f, #3d3d43, #0a0a11);
      background-size: 200% 200%; 
  }

  
  * {
    font-family: "Poppins", sans-serif;  
  }

  .blurry-bg {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    backdrop-filter: blur(0.3rem);
    background-color: rgba(0, 0, 0, 0.5);
    z-index: 1000;
  }
</style>

