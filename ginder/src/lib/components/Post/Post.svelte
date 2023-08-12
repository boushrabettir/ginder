<script lang="ts">

    import "../../../app.css";
</script>

<head>
    <link href="/dist/output.css" rel="stylesheet">
</head>

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


<style >
    
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

</style>
