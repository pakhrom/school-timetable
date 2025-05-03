import { superValidate } from 'sveltekit-superforms';
import { zod } from 'sveltekit-superforms/adapters';
import type { PageLoad } from './$types';
import { teacherWrite } from '$lib/schemas/teacher';

export const load: PageLoad = async ({ params /* , fetch */ }) => {
	const teacherId = params.id;

	let teacher;
	if (teacherId) {
		// fetch data from api
	}

	const form = await superValidate(teacher, zod(teacherWrite));
	return { teacherId, form };
};
