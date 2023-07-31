<script lang="ts">
  import { onMount } from 'svelte';
  import { user_data, local_storage_hold, retrieve_user_data } from "$lib/data";
  import { projects, retrieve_repositories, retrieve_next_project_group, current_project, curr_project } from "$lib/gh_data";
  
  // TODO - Change to cookies (don't use local storage D:)

  /*
      Ideally here we want to trigger a flask route
      to when the length of the data gets to 5, we fetch
      that endpoint

      Also, there should be a 3-second pause between each swap so
      it doesn't break
  */
 
 
 
  onMount(async () => {
    local_storage_hold();
    const local_data = JSON.parse(localStorage.getItem("projects") || "[]");
    if (local_data.length === 5) {
      await retrieve_next_project_group();
    }
    await retrieve_repositories();

    console.log(curr_project);
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
{#if $user_data}
  <div>
    <img src={$user_data.avatar_url} alt="User Avatar" />
    <h2>{$user_data.username}</h2>
  </div>
{:else}
  <p>Loading user data...</p>
{/if}

<div class="post">
  {#if curr_project}
    <p>{curr_project}</p>
  {:else}
    <p>Loading project data...</p>
  {/if}
</div>
