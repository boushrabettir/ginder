<script lang="ts">
    import { onMount } from 'svelte';
    import { writable } from 'svelte/store';
    import type { User } from '$lib/user';

    // TODO - Change to cookies (don't use local storage D:)
    
    let user_data = writable<User>();
    
    onMount(() => {
        const retrieve_code_value = (): string | null => {
            // Retrieves code param unique to the user

            const url_search = window.location.search;
            const url_params = new URLSearchParams(url_search);
            const code_param = url_params.get("code");
     
            return code_param;
        } 

        const local_storage_hold =  async () => {

            // Retrieve the code once authorization went through
            let param = retrieve_code_value();
                
            if (param && localStorage.getItem("token") === null) {

                    const retrieve_token = async () => {
                        // Retrieve OAuth token

                        try {
                            let response = await fetch(`http://127.0.0.1:5000/get_token?code=${param}`);

                            if (response.ok) {
                                // Retrieve the access token text
                                let raw_response_data = await response.text();
                                
                                // If there exists an access token, then add it to the local storage
                                if (raw_response_data) {
                                    localStorage.setItem("token", raw_response_data)
                                }
                            } else {
                                console.error(`Error response: ${response.status}`)
                            }
                        } catch (error) {
                            console.error(`Fetching error: ${error}`)
                        }
                        
                    }

                    retrieve_token();
                }
            }

        local_storage_hold();

        
    })


    const retrieve_user_data = async () => {

        try {
            const response = await fetch("http://127.0.0.1:5000/get_user_data", {
                method: "GET",
                headers: {
                    "Authorization":`Bearer ${localStorage.getItem("token")}`
                }
            });

            if (response.ok) {
                // Convert string literal to JSON object
                let data: any = await response.text()
                const object = JSON.parse(data);

                if (data) {
                    user_data.set({
                        avatar_url: object["avatar_url"],
                        username: object["login"]

                    }); 
                }
            } else {
                console.error(`Error with response: ${response.status}`);
            }

        } catch (error) {
            console.error(`Error fetching data: ${error}`);
        };
        
        return user_data;
    }

</script>

<p>you logged in</p>


{#if $user_data}
  <div>
    <img src={$user_data.avatar_url} alt="User Avatar" />
    <h2>{$user_data.username}</h2>
  </div>
{:else}
  <p>Loading user data...</p>
{/if}
<button on:click={retrieve_user_data}>Click for the test</button>
