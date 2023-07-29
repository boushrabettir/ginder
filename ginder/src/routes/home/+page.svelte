
<script lang="ts">
    import { onMount } from 'svelte';
    

    onMount(() => {
        const retrieve_code_value = (): string | null => {

        // Retrieves code param unique to the user
        const url_search = window.location.search;
        const url_params = new URLSearchParams(url_search);
        const code_param = url_params.get("code");

        return code_param;
        }

        const local_storage_hold =  async () => {
        let param = retrieve_code_value();

        if (param && localStorage.getItem("token")===null) {
                // Grab access token from our server

                const retrieve_token = async () => {
                    await fetch(`http://localhost:4000/get_token?code=${param}`, {
                        method: "GET",
                    }).then((res) => {
                        return res.json()
                    }).then((data: any) => {
                        console.log(data);
                        if (data.access_token) {
                            localStorage.setItem("token", data.access_token);
                        }
                        
                    });
                }

                retrieve_token();
            }
        }

        local_storage_hold();
    })
    // TODO - Use Cookies instead of local storage

    

  </script>

<p>you logged in</p>