import { z } from 'zod';

export const teacherWrite = z.object({
	fullname: z.object({
		first: z.string({ required_error: 'Введите имя' }).trim().min(1, 'Введите имя').max(15, { message: 'Имя не должно быть длиной более 15 символов' }),
		last: z.string({ required_error: 'Введите фамилию' }).trim().min(1, 'Введите фамилию').max(15, { message: 'Фамилия не должна быть длиной более 15 символов' }),
		middle: z.string({ required_error: 'Введите отчество' }).trim().min(1, 'Введите отчество').max(15, { message: 'Отчество не должно быть длиной более 15 символов' })
	}),
	gender: z.enum(['female', 'male'])
});

export const teacherRead = teacherWrite.extend({
	objId: z.string().length(24),
	udpateDate: z.string().date()
});
