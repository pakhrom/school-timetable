<script lang="ts">
	import { defaults, superForm } from 'sveltekit-superforms';
	import { baseUrl } from '../shared';
	import { zod } from 'sveltekit-superforms/adapters';
	import { loginSchema } from '$lib/schemas/login';

	let loginPromise: Promise<void> | undefined = $state();
	let loginMessage: string = $state('');

	const { form, errors, constraints, enhance, reset } = superForm(defaults(zod(loginSchema)), {
		SPA: true,
		resetForm: false,
		validators: zod(loginSchema),
		onUpdate({ form }) {
			if (form.valid) {
				loginPromise = fetch(baseUrl + '/auth/login', {
					method: 'POST',
					headers: {
						'Content-Type': 'application/json'
					},
					body: JSON.stringify(form.data)
				})
					.then(async (response) => {
						loginPromise = undefined;
						if (response.ok) {
							const responseData: { access_token: string } = await response.json();
							localStorage.setItem('token', JSON.stringify(responseData.access_token));

							reset();
							loginPromise = undefined;

							window.location.href = '/manage';
							return;
						} else {
							if (response.status === 404) {
								throw new Error('Неверный логин или пароль.');
							}
							throw new Error(`Неизвестная ошибка ${response.status}: ${response.statusText}.`);
						}
					})
					.catch((error) => {
						reset({ data: { username: form.data.username } });
						loginMessage = error.message;
						loginPromise = undefined;
					});
			}
		}
	});
</script>

<a href="/">
	<svg
		xmlns="http://www.w3.org/2000/svg"
		width="24"
		height="24"
		viewBox="0 0 24 24"
		fill="none"
		stroke="currentColor"
		stroke-width="2"
		stroke-linecap="round"
		stroke-linejoin="round"
		class="icon icon-tabler icons-tabler-outline icon-tabler-arrow-left"
		><path stroke="none" d="M0 0h24v24H0z" fill="none" /><path d="M5 12l14 0" /><path
			d="M5 12l6 6"
		/><path d="M5 12l6 -6" /></svg
	>
	Вернуться к расписанию
</a>
<h1>Вход в аккаунт</h1>

<form method="post" use:enhance>
	<div class="grid">
		<label for="username">
			Логин
			<input
				type="text"
				name="username"
				id="username"
				bind:value={$form.username}
				aria-invalid={Object.keys($errors).length !== 0
					? $errors.username !== undefined
					: undefined}
				aria-describedby="username-message"
				oninput={() => {
					loginMessage = '';
				}}
				{...$constraints.username}
			/>
			<small id="username-message">{$errors.username}</small>
		</label>
		<label for="password">
			Пароль
			<input
				type="password"
				name="password"
				id="password"
				bind:value={$form.password}
				aria-invalid={Object.keys($errors).length !== 0
					? $errors.password !== undefined
					: undefined}
				aria-describedby="password-message"
				oninput={() => {
					loginMessage = '';
				}}
				{...$constraints.password}
			/>
			<small id="password-message">{$errors.password}</small>
		</label>
	</div>
	<button class="wide" aria-busy={loginPromise !== undefined} disabled={loginPromise !== undefined}>
		<svg
			xmlns="http://www.w3.org/2000/svg"
			width="24"
			height="24"
			viewBox="0 0 24 24"
			fill="none"
			stroke="currentColor"
			stroke-width="2"
			stroke-linecap="round"
			stroke-linejoin="round"
			class="icon icon-tabler icons-tabler-outline icon-tabler-login"
		>
			<path stroke="none" d="M0 0h24v24H0z" fill="none" />
			<path d="M15 8v-2a2 2 0 0 0 -2 -2h-7a2 2 0 0 0 -2 2v12a2 2 0 0 0 2 2h7a2 2 0 0 0 2 -2v-2" />
			<path d="M21 12h-13l3 -3" />
			<path d="M11 15l-3 -3" />
		</svg>
		Войти
	</button>
</form>

{#if loginMessage}
	<p class="error">
		<svg
			xmlns="http://www.w3.org/2000/svg"
			width="24"
			height="24"
			viewBox="0 0 24 24"
			fill="none"
			stroke="currentColor"
			stroke-width="2"
			stroke-linecap="round"
			stroke-linejoin="round"
			class="icon icon-tabler icons-tabler-outline icon-tabler-exclamation-circle"
			><path stroke="none" d="M0 0h24v24H0z" fill="none" /><path
				d="M12 12m-9 0a9 9 0 1 0 18 0a9 9 0 1 0 -18 0"
			/><path d="M12 9v4" /><path d="M12 16v.01" /></svg
		>
		{loginMessage}
	</p>
{/if}

<style>
	a {
		display: inline-flex;
		align-items: center;
		gap: 0.25em;

		text-decoration: none;
	}

	.grid {
		margin-bottom: 1em;
		row-gap: 0;
	}

	input {
		margin: 0.25em 0;
	}

	button {
		display: flex;
		align-items: center;
		gap: 0.25em;
	}

	.wide {
		width: 100%;
		justify-content: center;
	}

	.error {
		display: flex;
		align-items: center;
		gap: 0.5em;

		margin-top: 1em;

		color: var(--pico-del-color);
	}
</style>
