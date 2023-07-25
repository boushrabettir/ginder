<<<<<<< Updated upstream
<script>
	let responseData;
  
	async function fetchData() {
	  try {
		const response = await fetch("http://127.0.0.1:5000/get_projects");
		if (response.ok) {
		  responseData = await response.json();
		  console.log(responseData)
		} else {
		  console.error("Failed to fetch data:", response.status, response.statusText);
		}
	  } catch (error) {
		console.error("Error fetching data:", error);
	  }
	}

	
  </script>
  
  <main>
	<h1>
=======
<script lang="ts">
  let response_data;

  const fetch_gh_data = async () => {
    try {
      const RESPONSE: Response = await fetch("http://127.0.0.1:5000/get_projects");
      if (RESPONSE.ok) {
        response_data = await RESPONSE.json();
        console.log(response_data)
      } else {
        console.error("Response was not ok: ", RESPONSE.status, RESPONSE.statusText);
      }
    } catch (error) {
      console.error("Failed fetching data: ", error);
    }

  } 
</script>

<main>
  <p>{response_data}</p>
  <button on:click={fetch_gh_data}>Fetch Data</button>
</main>
>>>>>>> Stashed changes

	  <button on:click={fetchData}>Fetch Data</button>
	</h1>
  </main>
  