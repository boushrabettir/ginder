import type { User } from '$lib/interface';

export let user_data: any = {};

/**
 * retrieve_code_value retrieves the oauth code from the URL
 */
const retrieve_code_value = (): string | null => {
	const url_search: string = window.location.search;
	const url_params: URLSearchParams = new URLSearchParams(url_search);
	const code_param: string | null = url_params.get('code');

	return code_param;
};

/**
 * local_storage_hold stores the users authentication token in local storage
 */
export const local_storage_hold = async () => {
	// Retrieve the code once authorization went through
	let param = retrieve_code_value();

	if (param && localStorage.getItem('token') === null) {
		const retrieve_token = async () => {
			// Retrieve OAuth token

			try {
				let response = await fetch(`http://127.0.0.1:5000/get_token?code=${param}`);

				if (response.ok) {
					// Retrieve the access token text
					let raw_response_data: string = await response.text();

					// If there exists an access token, then add it to the local storage
					if (raw_response_data) {
						localStorage.setItem('token', raw_response_data);
					}
				} else {
					console.error(`Error response: ${response.status}`);
				}
			} catch (error) {
				console.error(`Fetching error: ${error}`);
			}
		};

		retrieve_token();
	}
};

/**
 * retrieve_user_data retrieves the users data from github using the authentication token
 */
export const retrieve_user_data = async () => {
	try {
		const response = await fetch('http://127.0.0.1:5000/get_user_data', {
			method: 'GET',
			headers: {
				Authorization: `Bearer ${localStorage.getItem('token')}`
			}
		});

		if (response.ok) {
			// Convert string literal to JSON object
			let data: string = await response.text();
			console.log(data);
			const object: any = JSON.parse(data);

			if (data) {
				user_data = {
					avatar_url: object['avatar_url'],
					username: object['login']
				};
				localStorage.setItem('user-data', JSON.stringify(user_data));
			}
		} else {
			console.error(`Error with response: ${response.status}`);
		}
	} catch (error) {
		console.error(`Error fetching data: ${error}`);
	}
};

/**
 * pop_new_project grabs data from local storage and
 * pops a new project
 */
export const pop_new_project = (): Object => {
	let local_data = JSON.parse(localStorage.getItem('projects') || '[]');
	let curr: Object = local_data.shift();
	localStorage.setItem('projects', JSON.stringify(local_data));

	return curr;
};
