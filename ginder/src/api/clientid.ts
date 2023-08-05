import { CLIENT_ID } from '$env/static/private';

export const get = ({ request }: any) => {
	return {
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify({ data: 'f4b411c4d7b6b50ef40e' })
	};
};
