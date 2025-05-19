export const ssr = false;

import type { LayoutLoad } from './$types';

export const load: LayoutLoad = async () => {
	const tokenStored: string | null = localStorage.getItem('token');
	let token: string = '';
	if (tokenStored) {
		token = JSON.parse(tokenStored);
	}
	return { token };
};
