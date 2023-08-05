<script lang="ts">
 
    // let CLIENT_ID = "";

    // const get_id = async () => {
    //         const response = await fetch("./ginder/src/api/clientid.ts");
    //         const data = await response.json();
    //         CLIENT_ID = data["data"];
    // }
   
    const login_with_github = () => {
        let CLIENT_ID ="f4b411c4d7b6b50ef40e";
        window.location.assign(`https://github.com/login/oauth/authorize?client_id=${CLIENT_ID}`)
    }
</script>



<html lang="en">
  <meta charset="utf-8">
  <head>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@0.9.4/css/bulma.min.css">
    <!-- <link rel="stylesheet" href="ginder\static\root.css"> -->
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://fonts.googleapis.com/css2?family=Poppins&display=swap" rel="stylesheet">
    <title>ginder</title>
  </head>


  <body>
   
    <div class="middle">
        <div class="container">
            <div class="title-section">
                <p class="subtitle" id="welcome">Welcome to...</p>
                <p class="title" id="ginder">ginder</p>
                <p class="subtitle" id="welcome">Effortless connection and<br/> collaboration with a <span id="blue-text">simple</span> swipe.</p>
        
                <button class="pop-up" on:click={login_with_github}>
                    👾 Login through Github 🤖
                </button>
            </div>
      
        </div>
        <div class="card">
            <div class="card-image">
              <figure class="image is-4by6">
                <img src="./photos/github.png" alt="Placeholder ">
              </figure>
            </div>
            <div class="card-content">
              <div class="media">
                <div class="media-content">
                  <p class="subtitle is-4">
                    <span>Jeffery Thompsan</span> • @jeffery_12<br/>
                    <span>Followers:</span> 1.1k
                  </p>
                  <button id="dummy-button">+ Follow</button>
                </div>
              </div>
          
              <div class="content">
                <p class="title is-3">BEARTEAR</p>
                <p class = "subtitle is-5 dummy-sub">
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor.<br/>
                    🔤 Languages: Rust, TypeScript<br/>
                    ⭐ Stargazers: 12.1k • 📥  Forks: 235 • 📝 Commits: 39
                </p>
                <button class="dummy-view">
                    View Here!
                </button>
              </div>
            </div>
          </div>
    </div>
 
</body>
</html>

<style>
:global(body) {
    background: linear-gradient(to bottom right, #11111b, #383843, #171721);
    height: 100%;
    padding: 0;
}

* {
    font-family: "Poppins", sans-serif;
}

.middle {
    display: flex;
    align-items: center;
    justify-content: center; /* Center horizontally */
    height: 100vh; /* This will make .middle take the full viewport height */
    margin-left: 12rem;
    margin-right: 2rem;
}


.title-section p {
    color: white;
}

.title-section .title {
    font-size: 5rem;
    letter-spacing: 0.5rem;
}

.title-section .subtitle {
    font-size: 2.5rem;
    padding: 0.5rem 0;
    text-transform: uppercase;
}

#blue-text {
    font-style: italic;
    color: #89CEFF;
}

.card, figure img {
    border-radius: 1rem;
}
.card {
    
    animation: bobble 4s infinite;
    box-shadow: 0 0rem 3rem rgb(19, 19, 19);
}

@keyframes bobble {
    
  0% {
    transform: translateY(10px) translateX(-3px) perspective(10px) rotateZ(0.5deg) rotateY(-0.3deg) scale(0.55);
  }
  50% {
    transform: translateY(-5px) translateX(3px) perspective(10px) rotateZ(0.5deg) rotateY(-0.3deg) scale(0.55);
  }
  100% {
    transform: translateY(10px) translateX(-3px) perspective(10px) rotateZ(0.5deg) rotateY(-0.3deg) scale(0.55);
  }
}

.pop-up {
    background-color: #89CEFF;
    border: none;
    padding: 0.8rem;
    font-size: 1.2rem;
    border-radius: 0.3rem;
    box-shadow: 0 0 1rem rgb(26, 26, 26);
    font-weight: 600;
    color: #1D1D27;
    cursor: pointer;
    transition: ease 100ms all;
}

.pop-up:hover {
    transform: scale(1.1);
    box-shadow: 0 0 2rem rgb(26, 26, 26);
}

#dummy-button {
    background-color: #1D1D27;
    color: white;
    border: none;
    padding: 0.5rem 3rem;
}

.content, .media-content {
    text-align: center;
    
}

.dummy-view {
    border: none;
    background-color: #89CEFF;
    padding: 0.5rem 5rem;
    font-size: 1rem;
    border-radius: 15rem;
    box-shadow: 0 0 0.5rem rgba(40, 40, 40, 0.557);
}

.dummy-sub {
    margin-left: 1rem;
    margin-right: 1rem;
}

</style>
