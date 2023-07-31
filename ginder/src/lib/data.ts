import type { User } from '$lib/interface';
import { writable, type Writable } from 'svelte/store';

export let user_data = writable<User>();

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
export const retrieve_user_data = async (): Promise<Writable<User>> => {
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
				user_data.set({
					avatar_url: object['avatar_url'],
					username: object['login']
				});
			}
		} else {
			console.error(`Error with response: ${response.status}`);
		}
	} catch (error) {
		console.error(`Error fetching data: ${error}`);
	}

	return user_data;
};
