<script lang="ts">
 
    // let CLIENT_ID = "";

    // const get_id = async () => {
    //         const response = await fetch("./ginder/src/api/clientid.ts");
    //         const data = await response.json();
    //         CLIENT_ID = data["data"];
    // }
    import Post from "$lib/components/Post/Post.svelte";
    import "../app.css";
    const login_with_github = () => {
        let CLIENT_ID ="f4b411c4d7b6b50ef40e";
        window.location.assign(`https://github.com/login/oauth/authorize?client_id=${CLIENT_ID}`)
    }
</script>



<html lang="en">
  <meta charset="utf-8">
  <head>
  
    <link href="/dist/output.css" rel="stylesheet">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://fonts.googleapis.com/css2?family=Poppins&display=swap" rel="stylesheet">
    <title>ginder</title>
  </head>


  <body>
  
    <div class="middle flex flex-nowrap justify-center items-center mx-auto max-w-7xl">
        <div class="container selection:bg-sky-300 selection:text-sky-700">
            <div class="title-section">
                <p class="subtitle" id="welcome">Welcome to...</p>
                <p class="text-7xl font-bold title" id="ginder">ginder</p>
                <p class="subtitle" id="welcome">Effortless connection and collaboration with a <span class="text-sky-300 italic">simple</span> swipe.</p>
        
                <button class="pop-up bg-gradient-to-r from-cyan-500 to-sky-500 hover:bg-sky-400 ease-out duration-300 hover:scale-110 font-bold rounded-md text-1xl p-3" on:click={login_with_github}>
                  🤖 Login through Github 👾
                </button>
            </div>
        </div>
            
        <Post />
    
    </div>

    
</body>
</html>


<style type="postcss">


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

.middle {
    height: 100vh;
  
}


.title-section p {
    color: white;
}

.title-section .title {
    letter-spacing: 0.5rem;
}

.title-section .subtitle {
    font-size: 2.5rem;
    padding: 0.5rem 0;
    text-transform: uppercase;
}

</style>
