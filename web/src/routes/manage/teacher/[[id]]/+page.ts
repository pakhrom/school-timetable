import type { PageLoad } from './$types';
import { superValidate } from 'sveltekit-superforms';
import { zod } from 'sveltekit-superforms/adapters';
import { teacherWrite } from '$lib/schemas/teacher';
import { baseUrl } from '$lib/secrets/secrets';

export const load: PageLoad = async ({ params, fetch }) => {
	const teacherId = params.id;

	let teacher;
	let error;
	if (teacherId) {
		await fetch(baseUrl + '/teachers/' + teacherId)
			.then(async (response) => {
				if (response.ok) {
					teacher = await response.json();
				} else {
					throw new Error(`Неизвестная ошибка ${response.status}: ${response.statusText}.`);
				}
			})
			.catch((error_) => {
				error = error_.message;
			});
	}

	const form = await superValidate(teacher, zod(teacherWrite));
	return { teacherId, form, error };
};
