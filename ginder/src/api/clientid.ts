import { CLIENT_ID } from '$env/static/private';

export const get = ({ request }: any) => {
	return {
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify({ data: CLIENT_ID })
	};
};
