import { z } from 'zod';

export const teacherWrite = z.object({
	name: z.object({
		first: z.string({ required_error: 'Введите имя' }).trim().min(1, 'Введите имя'),
		last: z.string({ required_error: 'Введите фамилию' }).trim().min(1, 'Введите фамилию'),
		middle: z.string().trim().optional()
	}),
	gender: z.enum(['female', 'male'])
});

export const teacherRead = teacherWrite.extend({
	id: z.string().uuid()
});
