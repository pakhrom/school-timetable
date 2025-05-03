import { superValidate } from 'sveltekit-superforms';
import { zod } from 'sveltekit-superforms/adapters';
import type { PageLoad } from './$types';
import { subjectWrite } from '$lib/schemas/subject';

export const load: PageLoad = async ({ params /* , fetch */ }) => {
	const subjectId = params.id;

	let subject;
	if (subjectId) {
		// fetch data from api
	}

	const form = await superValidate(subject, zod(subjectWrite));
	return { subjectId, form };
};
