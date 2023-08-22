<script lang="ts">

    import "../../../app.css";
</script>

<head>
    <link href="/dist/output.css" rel="stylesheet">
</head>

<div class="card shadow-2xl rounded-md select-none text-slate-200 text-center">
            
    <div class="media rounded-t-md">
      <div class="flex justify-center">
        <img src="./photos/github.png" alt="Placeholder " class="w-full rounded-t-lg">
      </div>
 
      <p class=" text-slate-950 text-center inline-block text-xs align-middle mt-2 absolute z-10 left-1/2 top-0 bg-neutral-900 text-white  p-2 rounded-full -translate-x-1/2 w-max shadow-xl">
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
          ⭐ Stargazers: 12.1k • 📥  Forks: 235 • 📝 Contributers: 39
        </p>
        <button class="pointer-events-none rounded-md text-xs text-slate-950 bg-sky-200 pl-6 pr-6 pt-1 pb-1 mb-3 mt-2">
            View Here!
        </button>
      </div>
    </div>
  </div>


<style >
    
.card {

    animation: bobble 4s infinite;
  
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

</style>
