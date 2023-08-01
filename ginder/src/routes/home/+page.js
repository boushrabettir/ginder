import { retrieve_repositories } from './gh_data';

export const load = async () => {
	const data = await retrieve_repositories();
	return {
		data
	};
};
