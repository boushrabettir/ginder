<script lang="ts">
    import { onMount } from 'svelte';
    import { user_data, local_storage_hold, retrieve_user_data } from "$lib/data";
    import { projects, top_user_languages, next_group, retrieve_repositories, retrieve_languages, retrieve_next_project_group } from "$lib/gh_data";
    // TODO - Change to cookies (don't use local storage D:)

    /*
        Ideally here we want to trigger a flask route
        to when the length of the the in data gets to 5, we fetch
        that end point

        Also, there should be a 3 second pause between each swap so
        it doesn't break
    */
   
    
    onMount(() => {
        local_storage_hold();
        retrieve_repositories();

        if(localStorage.getItem("")?.length() <= 5) {
          retrieve_next_project_group();
        }
    });

</script>

<!DOCTYPE html>
<html lang="en">
  <meta charset="utf-8">
  <head>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@0.9.4/css/bulma.min.css">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>ginder</title>
  </head>
</html>
<p>You logged in!</p>

{projects}

{#if $user_data}
  <div>
    <img src={$user_data.avatar_url} alt="User Avatar" />
    <h2>{$user_data.username}</h2>
  </div>
{:else}
  <p>Loading user data...</p>
{/if}
<button on:click={retrieve_user_data}>Click for the test</button>

