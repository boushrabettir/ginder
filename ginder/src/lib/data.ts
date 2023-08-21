import type { User } from '$lib/interface';
import { writable } from 'svelte/store';
import { retrieve_next_project_group, retrieve_repositories } from '../routes/home/gh_data';

export let user_data: any = writable();

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

		await retrieve_token();
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
			// Convert response text to JSON object directly
			const object = await response.json();

			if (object) {
				localStorage.setItem(
					'user-data',
					JSON.stringify({
						avatar_url: object['avatar_url'],
						username: object['login']
					})
				);

				// Update user_data immediately after setting in localStorage
				user_data.set({
					avatar_url: object['avatar_url'],
					username: object['login']
				});

				console.log(user_data);
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

/**
 * determine_next_step determines whether or not to add extra
 * projects if there exists less than 5 right swipes and
 * the project list is less than 10
 */
export const determine_next_step = async () => {
	let project_data = JSON.parse(localStorage.getItem('projects') || '[]');
	let right_swipes = JSON.parse(localStorage.getItem('right-swipes') || '[]');

	if (project_data?.length == 10) {
		if (right_swipes?.length == 0) {
			await retrieve_repositories();
		} else {
			await retrieve_next_project_group();
		}
	}
};
