import type { PageLoad } from './$types';
import { superValidate } from 'sveltekit-superforms';
import { zod } from 'sveltekit-superforms/adapters';
import { subjectWrite } from '$lib/schemas/subject';
import { baseUrl } from '$lib/secrets/secrets';

export const load: PageLoad = async ({ params, fetch }) => {
	const subjectId = params.id;

	let subject;
	let error;
	if (subjectId) {
		await fetch(baseUrl + '/subjects/' + subjectId)
			.then(async (response) => {
				if (response.ok) {
					subject = await response.json();
				} else {
					throw new Error(`Неизвестная ошибка ${response.status}: ${response.statusText}.`);
				}
			})
			.catch((error_) => {
				error = error_.message;
			});
	}

	const form = await superValidate(subject, zod(subjectWrite));
	return { subjectId, form, error };
};
