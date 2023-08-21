<script lang="ts">

    import "../../../app.css";


    export let username: string;
    export let followers: number;
    export let repo_title: string;
    export let description: string;
    export let languages: Array<string>;
    export let stargazers: number;
    export let forks: number;
    export let contributers: number;
    export let link: string;
    export let pfp_photo: string;



    const format_large_numbers = (str_value: string) => {
      let number_value = parseInt(str_value, 10);
      if (number_value >= 1000) {
        return `${(number_value / 1000).toFixed(1)}k`;
      } else {
        return number_value.toString();
      }
    }

</script>

<head>
    <link href="/dist/output.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Poppins&display=swap" rel="stylesheet">
</head>

<div class="flex items-center justify-center mt-24">
<div class="scale-125 pb-5 w-96 shadow-2xl rounded-md mx-auto rounded-md text-slate-200 text-center ">
    <img src={pfp_photo} alt="Placeholder" class=" flex justify-center rounded-t-lg">
    <p class="text-slate-950 text-center inline-block text-xs align-middle absolute z-10 left-1/2 top-4 bg-neutral-900 text-white p-2 rounded-full -translate-x-1/2 w-max shadow-xl">
      {username} • <span class="font-bold">Followers:</span> {format_large_numbers(followers)}
    </p>
    <div class="card-content ml-3 mr-3">
        <div class="content mt-2">
          <p class="text-2xl">{repo_title}</p>
          <p class="mb-2 text-xs">
            {description}
          </p>
          <p class="border-b-2 border-neutral-600"></p>
          <p class="mt-2 text-xs mb-3">
            🔤 Languages:{languages}<br/>
            ⭐ Stargazers: {format_large_numbers(stargazers)} • 📥 Forks: {format_large_numbers(forks)} • 📝 Contributers: {format_large_numbers(contributers)}
          </p>
          <a href={link} target="_blank" class="font-bold border-b-2 rounded-md text-md text-slate-950 bg-sky-200 pl-6 pr-6 pt-1 pb-1 shadow-2xl">
            View Here!
          </a>
        </div>
      </div>
    </div>
</div>