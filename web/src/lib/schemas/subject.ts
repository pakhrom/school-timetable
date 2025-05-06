import { z } from 'zod';

export const subjectWrite = z.object({
	name: z.string({ required_error: 'Введите имя' }).trim().min(1, { message: 'Введите имя' }),
	shortName: z
		.string()
		.max(12, { message: 'Короткое название предмета не должно быть длиной более 12 символов' })
		.trim()
		.optional(),
	optional: z.boolean().default(false)
});

export const subjectRead = subjectWrite.extend({
	id: z.string().uuid()
});
