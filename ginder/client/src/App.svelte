<script lang="ts">
  /*
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
  */

  import Header from "./lib/Header.svelte";
  import Footer from "./lib/Footer.svelte";
  import Post from "./lib/Post.svelte";
</script>

<main>
  <!--
  <p id=response>{response_data}</p>
  <button on:click={fetch_gh_data}>Fetch Data</button>
  -->
  <Header />

  <Post />

  <Footer />
</main>


<style>
  /* @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500&display=swap');
  button, 
  #response {
    margin-bottom: 100px;
  }

  .logo {
    height: 8em;
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

  main {
    font-family: 'Poppins', sans-serif;
  }

  #footer {
    font-size: 7;
    color: #FFFFFF;
    text-align: center;
    position: absolute;
    right: 0;
    left: 0;
    bottom: 0;
  }

  a {
    color: #FFFFFF;
    text-decoration: none;
  }

  #logo {
    color: #FFFFFF;
    font-size: 15;
    position: absolute;
    margin-top: 10px;
    margin-left: 30px;
    font-weight: bolder;
  }

  #small-circle {
    height: 30px;
    width: 30px;
    border-radius: 50%;
    background-color: #D9D9D9;
    position: absolute;
    margin-top: 19px;
    margin-left: 163px;
  }

  #slogan {
    position: absolute;
    font-weight:500;
    text-align: center;
    top: 0;
    left: 0;
    right: 0;
    font-size: 7;
    margin-top: 32px;
  }

  #center-block {
  background-color: #B5B5C2;
  height: 440px;
  width: 375px;
  border-radius: 6px;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

#circle-block {
  height: 190px;
  width: 190px;
  border-radius: 50%;
  background-color: #CDCDD7;
  position: absolute;
  top: 23%;
  left: 50%;
  transform: translate(-50%, -50%);
} */

</style>

<!-- these are the list of components. I would have a component for
1. 'Your Stars' button
2. username corner
3. Project Name
4. Project owner
5. Total stars
6. Languages used
7. Description
8. Link to repo
9. the text at the bottom that says there are 10k stargazers


in app.svelte, i could put the text with no logic behind it where they only need to be designed
1. 'ginder' in the corner
2. the text in the middle top
3. the text at the middle low
4. the box and circle design in the middle

-->