import { z } from "zod";

export const loginSchema = z.object({
  username: z.string({ required_error: 'Введите имя пользователя' }).trim().min(1, { message: 'Введите имя пользователя' }),
  password: z.string({ required_error: 'Введите пароль' }).trim().min(1, { message: 'Введите пароль' })
})