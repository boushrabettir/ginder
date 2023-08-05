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

	let data = JSON.stringify(localStorage.getItem('right-swipes'));

	try {
		let response = await fetch('http://127.0.0.1:5000/get_next_group', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify(data)
		});

		if (response.ok) {
			next_group = await response.json();

			const in_session_projects = JSON.parse(localStorage.getItem('projects') || '[]');

			in_session_projects.push(next_group);

			const modified_content = JSON.stringify(in_session_projects);

			localStorage.setItem('projects', modified_content);
		}
	} catch (error) {
		console.error(`Error fetching data: ${error}`);
	}
};
