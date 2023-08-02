<script lang="ts">
  import { onMount } from 'svelte';
  import { user_data, local_storage_hold, retrieve_user_data } from "$lib/data";
  import { retrieve_next_project_group } from './gh_data';
  
  export let data: any;
  let curr: any = data["data"].shift();


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
    curr = data["data"].shift();
    
    /**
     * Determines whether or not new data should be added
     * into the list
    */
    if (localStorage.getItem("right-swipes")?.length == 5) {
      let next_group = retrieve_next_project_group();
      data.push(next_group);
    }
    
  }

  /**
   * left retrieves the next data block
   */
  const left = () => {
    curr = data["data"].shift();
  }


  onMount(async () => {
    local_storage_hold();
    retrieve_user_data();
  });
</script>

<html lang="en">
  <meta charset="utf-8">
  <head>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@0.9.4/css/bulma.min.css">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>ginder</title>
  </head>
</html>
<p>You logged in!</p>

<!-- <p>ginder | @{user_data["username"]}</p>
<img src={user_data["avatar_url"]} /> -->

{#if curr}
  <p>Boushra Bettir • {curr["owner"]}</p>
  <button>+ Follow</button>
  <p>{curr["name"]}</p>
  <p>{curr["desc"]}</p>
  <p>Languages: {curr["languages"]}</p>
  <p>Stargazers: {curr["stars"]} • Forks: 12.1k • Commits: 12</p>
{/if}

<button on:click={left}>next</button>
<button on:click={right}>next</button>