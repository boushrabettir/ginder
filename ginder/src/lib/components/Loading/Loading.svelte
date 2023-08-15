<script lang="ts">

    import "../../../app.css";
</script>

<head>
    <link href="/dist/output.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Poppins&display=swap" rel="stylesheet">
</head>

<div class="m-auto container flex justify-center items-center">
    <div class="bg-zinc-200 rounded-md text-center p-10 absolute z-10 center ml-5 mr-5">
        <h1 class="text-5xl font-bold tracking-wide text-red-800">HOLD UP!!!</h1>
        <p class="text-2xl mt-5 mb-5">We’re preparing a <span class="text-sky-400 italic">new batch</span> of projects just for you! Grab a cup of coffee, sit back, and unwind. Let us handle the heavy lifting for you. ☕🌟</p>
        <p class="text-sm italic">Once we’re ready this pop up will vanish!</p>
    </div>
</div>
<style>
    * {
    font-family: "Poppins", sans-serif;  
  }

.center {
   
    box-shadow: 0 0 1.2rem rgb(28, 28, 28);
   
} 

.container {
    animation: bounce 4s infinite;
    height: 80vh;
    
}

@keyframes bounce {
    
    0% {
    transform: translateY(10px);
    }
    50% {
    transform: translateY(-5px);
    }
    100% {
    transform: translateY(10px);
    }
}
</style>

