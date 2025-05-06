import { z } from 'zod';

export const subjectWrite = z.object({
	name: z.string({ required_error: 'Введите имя' }).trim().min(1, { message: 'Введите имя' }),
	shortName: z
		.string()
		.trim()
		.max(10, { message: 'Короткое название предмета не должно быть длиной более 10 символов' })
		.optional(),
	optional: z.boolean().default(false)
});

export const subjectRead = subjectWrite.extend({
	id: z.string().uuid()
});
