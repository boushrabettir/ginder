// TODO - This appropriates 'DRY'. Refactor.

export let projects: Object[] = [];
export let top_user_languages: string[] = [];
export let curr_project: Object = {};

/**
 * retrieve_repositories retrieves the github repositories
 * from the server
 */
export const retrieve_repositories = async (): Promise<Object[]> => {
	try {
		let response = await fetch('http://127.0.0.1:5000/get_projects', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},

			body: JSON.stringify({ token: localStorage.getItem('token') })
		});

		if (response.ok) {
			let data = await response.json();

			if (data) {
				projects = data['serialized_data'];
				localStorage.setItem('projects', JSON.stringify(projects));
			}
		}
	} catch (error) {
		console.error(`Error fetching data: ${error}`);
	}

	return projects;
};

/**
 * retrieve_languages retrieves the users top three
 * languages from the server
 */
export const retrieve_languages = async (): Promise<string[]> => {
	try {
		let response = await fetch('http://127.0.0.1:5000/get_projects');

		if (response.ok) {
			let data = await response.json();

			if (data) {
				top_user_languages = data['top_languages'];
			}
		}
	} catch (error) {
		console.error(`Error fetching data: ${error}`);
	}

	return top_user_languages;
};

/**
 * retrieve_next_project_group retrieves the next batch of
 * github projects from the server
 */
export const retrieve_next_project_group = async () => {
	let next_group: Object[] = [];

	try {
		let response = await fetch('http://127.0.0.1:5000/get_next_group', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({
				data: localStorage.getItem('right-swipes'),
				token: localStorage.getItem('token')
			})
		});

		if (response.ok) {
			next_group = await response.json();

			const in_session_projects = JSON.parse(localStorage.getItem('projects') || '[]');

			in_session_projects.push(...next_group);

			localStorage.setItem('projects', JSON.stringify(in_session_projects));

			localStorage.removeItem('right-swipes');
		}
	} catch (error) {
		console.error(`Error fetching data: ${error}`);
	}
};

/**
 * add_project_to_stars adds each project from local storage
 * (right swipes) to the users Github stars list
 */
export const add_project_to_stars = async () => {
	try {
		let response = await fetch('http://127.0.0.1:5000/add_to_stars', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({
				data: localStorage.getItem('stars'),
				token: localStorage.getItem('token')
			})
		});

		if (response.ok) {
			let gh_stars_projects = JSON.parse(localStorage.getItem('stars') || '[]');
			if (gh_stars_projects && gh_stars_projects.length > 0) {
				gh_stars_projects.pop();
			}

			localStorage.setItem('stars', JSON.stringify(gh_stars_projects));
		}
	} catch (error) {
		console.error(`Error fetching endpoint to add GH star: ${error}`);
	}
};
