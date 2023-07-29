<script lang="ts">
    import { CLIENT_ID } from "../envconfig"
  
    const login_with_github = () => {
        window.location.assign(`https://github.com/login/oauth/authorize?client_id=${CLIENT_ID}`)
    }
</script>

<main>
    <p> Login through Github </p>
    <button on:click={login_with_github}>
        Login
    </button>
</main>
