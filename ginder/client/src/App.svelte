<script lang="ts">
  let response_data;

  const fetch_gh_data = async () => {
    try {
      const RESPONSE: Response = await fetch("http://127.0.0.1:5000/get_projects");
      if (RESPONSE.ok) {
        response_data = await RESPONSE.json();
        console.log(response_data)
      } else {
        console.error("Response was not ok: ", RESPONSE.status, RESPONSE.statusText);
      }
    } catch (error) {
      console.error("Failed fetching data: ", error);
    }

  } 
</script>

<main>
  <p>{response_data}</p>
  <button on:click={fetch_gh_data}>Fetch Data</button>
</main>


<style>
  .logo {
    height: 6em;
    padding: 1.5em;
    will-change: filter;
    transition: filter 300ms;
  }
  .logo:hover {
    filter: drop-shadow(0 0 2em #646cffaa);
  }
  .logo.svelte:hover {
    filter: drop-shadow(0 0 2em #ff3e00aa);
  }
  .read-the-docs {
    color: #888;
  }
</style>
