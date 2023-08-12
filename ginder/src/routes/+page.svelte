<script lang="ts">
 
    // let CLIENT_ID = "";

    // const get_id = async () => {
    //         const response = await fetch("./ginder/src/api/clientid.ts");
    //         const data = await response.json();
    //         CLIENT_ID = data["data"];
    // }
   
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
    <!-- <link rel="stylesheet" href="ginder\static\root.css"> -->
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

        <div class="card rounded-md select-none text-slate-200 text-center">
            
            <div class="media bg-zinc-400 p-2 rounded-t-md">
              <div class="flex justify-center">
                <img src="./photos/github.png" alt="Placeholder " class="w-full rounded-md">
              </div>
         
              <p class=" text-slate-950 text-center inline-block text-xs align-middle mt-2">
                @jeffery_12 • <span class="font-bold">Followers:</span> 1.1k
              </p>
              
            </div>
            
            <div class="card-content ml-5 mr-5">
  
              <div class="content mt-2">
                <p class="text-2xl">BEARTEAR</p>
                <p class = "text-1xl mb-2 text-xs">
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor.
                </p>
                <p class="border-b-2 border-neutral-600"></p>
                <p class="mt-2 text-xs">
                  🔤 Languages: Rust, TypeScript<br/>
                  ⭐ Stargazers: 12.1k • 📥  Forks: 235 • 📝 Commits: 39
                </p>
                <button class="rounded-md text-xs text-slate-950 bg-sky-200 pl-6 pr-6 pt-1 pb-1 mb-3 mt-2">
                    View Here!
                </button>
              </div>
            </div>
          </div>
    </div>

    <p class = "text-center uppercase text-sky-300 mb-2 ">Created and maintained with 💙 by @boushrabettir</p>
</body>
</html>


<style type="postcss">
:global(body) {
    background: linear-gradient(to bottom right, #11111b, #383843, #171721);
    height: 100%;
    padding: 0;
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

.card {

    animation: bobble 4s infinite;
    box-shadow: 0 0rem 3rem rgb(19, 19, 19);
}

@keyframes bobble {
    
  0% {
    transform: translateY(10px) translateX(-3px) perspective(5px) rotateY(-0.3deg) scale(1);
  }
  50% {
    transform: translateY(-5px) translateX(3px) perspective(5px) rotateY(-0.3deg) scale(1);
  }
  100% {
    transform: translateY(10px) translateX(-3px) perspective(5px) rotateY(-0.3deg) scale(1);
  }
}

.pop-up {
    box-shadow: 0 0 1rem rgb(26, 26, 26);
    color: #1D1D27;
}


</style>
