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

	  <button on:click={fetchData}>Fetch Data</button>
	</h1>
  </main>
  