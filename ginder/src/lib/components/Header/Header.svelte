<script lang="ts">
    export let username: string;
    export let profile_picture: string;
</script>

<main>
    <div id="ginder">
        <p>ginder | <span id="img"><img src={profile_picture} alt="A github profile."/></span>@{username}</p>
    </div>
</main>


<style>
    
</style>

