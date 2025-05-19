import { currentTab, validTabs, type TabType } from '../shared.svelte';
import type { PageLoad } from './$types';
import { error } from '@sveltejs/kit';

function isTabType(tab: string): tab is TabType {
	return (validTabs as readonly string[]).includes(tab);
}

export const load: PageLoad = async ({ params }) => {
	const tab = params.tab || currentTab.tab;

	if (!isTabType(tab)) {
		throw error(404, 'Invalid tab parameter');
	}

	return { tab };
};
