import { z } from 'zod';

export const subjectWrite = z.object({
	fullName: z.string({ required_error: 'Введите имя' }).trim().min(1, { message: 'Введите имя' }).max(20, { message: 'Название предмета не должно быть длиной более 20 символов' }),
	shortName: z
		.string()
		.trim()
		.max(10, { message: 'Короткое название предмета не должно быть длиной более 10 символов' })
		.default(''),
	optional: z.boolean().default(false)
});

export const subjectRead = subjectWrite.extend({
	objId: z.string(),
	updateDate: z.string().date()
});
