<script lang="ts">
    import dotenv from 'dotenv';

    const CLIENT_ID = process.env.CLIENT_ID || '';
    const login_with_github = () => {
        window.location.assign(`https://github.com/login/oauth/authorize?client_id=${CLIENT_ID}`)
    }
</script>

<main>
    <h2 id="welcome">Welcome to...</h2>
    <p> 👾 Login through Github 🤖 </p>
    <button on:click={login_with_github}>
        Login
    </button>
</main>


<style>

</style>
