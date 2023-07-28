<script lang="ts">

  let response_data;
  const fetch_gh_data = async () => {
    try {
      const RESPONSE: Response = await fetch("http://127.0.0.1:5000/get_projects");
      if (RESPONSE.ok) {
        response_data = await RESPONSE.json();
        console.log(response_data)
      } else {
        console.error("Response was not valid: ", RESPONSE.status, RESPONSE.statusText);
      }
    } catch (error) {
      console.error("Failed fetching data: ", error);
    }

  } 


  import Header from "./lib/Header.svelte";
  import Footer from "./lib/Footer.svelte";
  import Post from "./lib/Post.svelte";
</script>

<main>
  
  <p id=response>{response_data}</p>
  <button on:click={fetch_gh_data}>Fetch Data</button>
 
  <Header />
  <Post />
  <Footer />
</main>


<style>
 
</style>

