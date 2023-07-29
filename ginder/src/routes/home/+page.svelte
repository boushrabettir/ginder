<script lang="ts">
    import { onMount } from 'svelte';
    import { user_data, local_storage_hold, retrieve_user_data } from "$lib/data";

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
    });

</script>

<p>You logged in!</p>


{#if $user_data}
  <div>
    <img src={$user_data.avatar_url} alt="User Avatar" />
    <h2>{$user_data.username}</h2>
  </div>
{:else}
  <p>Loading user data...</p>
{/if}
<button on:click={retrieve_user_data}>Click for the test</button>
