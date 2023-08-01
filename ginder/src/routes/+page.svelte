<script lang="ts">
    // import dotenv from 'dotenv';

    // const CLIENT_ID = process.env.CLIENT_ID || '';
    const TEMP = "";
    const login_with_github = () => {
        window.location.assign(`https://github.com/login/oauth/authorize?client_id=${TEMP}`)
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
    <div class="container">
        <div class="title-section">
            <p class="subtitle" id="welcome">Welcome to...</p>
            <p class="title" id="ginder">ginder</p>
            <p class="subtitle" id="welcome">Effortless connection and collaboration with a <span id="blue-text">simple</span> swipe.</p>
        </div>
        <button on:click={login_with_github}>
            👾 Login through Github 🤖
        </button>
    </div>
   

      
</body>
</html>
<!-- 
<style>
:global(body) {
    background: linear-gradient(to bottom right, #11111b, #383843, #171721);
    height: 100vh;
    margin: 0;
    padding: 0;
    display: flex;
    justify-content: center;
    align-items: center;
}

* {
    font-family: "Poppins", sans-serif;
}

body {
    align-items: center;
    align-content: center;
    margin: 0;
    padding: 0 12rem; /* Adjust the padding-left and padding-right */
}

.container {
    margin-bottom: 3rem;
}

.title-section p {
    color: white;
    margin: 0.5rem 0;
}

.title-section #ginder {
    letter-spacing: 0.5rem;
    font-size: 5rem;
    margin: 0;
}

.title-section #welcome {
    text-transform: uppercase;
    font-size: 2.5rem;
    line-height: 3.5rem;
    margin: 0;
}

#blue-text {
    font-style: italic;
    color: #89CEFF;
}

#button-color {
    background-color: #89CEFF;
    border: none;
    box-shadow: 0 0 2rem rgb(14, 14, 14);
    font-weight: 600;
    color: #1D1D27;
    font-size: 1.2rem;
    margin-top: 2rem;
}

.card {
    
    transform: perspective(20px) rotateZ(0.5deg) rotateY(-0.7deg) scale(0.7) translateX(5rem);
    box-shadow: 0.5rem 0.5rem 1rem rgb(21, 21, 21);
    background-color: #222222;
    z-index: 2;
}

.c2 {
    transform: perspective(20px) rotateZ(0.5deg) rotateY(-0.7deg) scale(0.7) translateX(-15rem);
    z-index: 1;
}

.card, #follow-button, #user-info, .media p, #stats {
    color: #FFFFFF;
}

#follow-button {
    background-color: #1D1D27;
    border: none;
    margin-top: 0.4rem;
    font-size: 1.1rem;
    padding: 0.5rem 3rem;
    border-radius: 0.4rem;
}

#bolded {
    font-weight: 800;
}

#user-info {
    background-color: #9e9e9e;
    padding: 1rem;
    font-size: 1.2rem;
    text-align: center;
}

.media-content p {
    border-bottom: solid 2px rgba(255, 255, 255, 0.436);
    text-align: center;
}

.content {
    text-align: center;
}

#stats {
   margin-top: 0.7rem;
}

</style> -->
