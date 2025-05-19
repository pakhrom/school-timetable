<script lang="ts">
	import SuperDebug, { superForm } from 'sveltekit-superforms';
	import { zod } from 'sveltekit-superforms/adapters';
	import { teacherWrite } from '$lib/schemas/teacher.js';
	import { baseUrl } from '$lib/secrets/secrets';
	import { debugMode } from '../../../shared.js';
	import { goto } from '$app/navigation';

	let { data } = $props();

	let changesMade: boolean = $state(false);

	let promise: Promise<void> | undefined = $state();
	let successMessage: string = $state('');
	let errorMessage: string = $state('');

	const { form, constraints, errors, enhance } = superForm(data.form, {
		dataType: 'json',
		SPA: true,
		resetForm: false,
		validators: zod(teacherWrite),
		onUpdate({ form }) {
			if (form.valid) {
				promise = fetch(baseUrl + '/teachers/' + (data.teacherId ? data.teacherId : ''), {
					method: data.teacherId ? 'PUT' : 'POST',
					body: JSON.stringify(form.data),
					headers: {
						'Content-Type': 'application/json',
						token: data.token
					}
				})
					.then(async (response) => {
						if (response.ok) {
							successMessage = data.teacherId
								? 'Преподаватель был успешно обновлён.'
								: 'Преподаватель был успешно добавлен.';

							changesMade = false;
							promise = undefined;

							if (!data.teacherId) {
								goto('/manage/teachers');
							}
						} else {
							const responseData = await response.json();
							if (responseData.error_type && responseData.error_type === 'JWTDecodeError') {
								localStorage.removeItem('token');
								window.location.href = '/login?invalid_token=';
								throw new Error(`Ваш токен устарел. Пожалуйста, войдите в аккаунт снова.`);
							} else {
								throw new Error(`Неизвестная ошибка ${response.status}: ${response.statusText}.`);
							}
						}
					})
					.catch((error) => {
						errorMessage = error.message;
						promise = undefined;
					});
			}
		}
	});
</script>

<a href="/manage">
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
	Вернуться к панели администратора
</a>
<h1>
	{#if !data.teacherId}
		Добавление преподавателя
	{:else if !data.error}
		Редактирование преподавателя
	{:else}
		Преподаватель не был найден
	{/if}
</h1>

{#if !data.error}
	<form action="POST" use:enhance>
		<div class="grid">
			<label for="last-name">
				Фамилия*
				<input
					type="text"
					name="last-name"
					id="last-name"
					aria-invalid={Object.keys($errors).length !== 0
						? $errors.fullname && $errors.fullname.last !== undefined
						: undefined}
					aria-describedby="last-name-message"
					bind:value={$form.fullname.last}
					oninput={() => {
						successMessage = '';
						errorMessage = '';
						changesMade = true;
					}}
					{...$constraints.fullname?.last}
				/>
				<small id="last-name-message">{$errors.fullname?.last}</small>
			</label>

			<label for="first-name">
				Имя*
				<input
					type="text"
					name="first-name"
					id="first-name"
					aria-invalid={Object.keys($errors).length !== 0
						? $errors.fullname && $errors.fullname.first !== undefined
						: undefined}
					aria-describedby="first-name-message"
					bind:value={$form.fullname.first}
					oninput={() => {
						successMessage = '';
						errorMessage = '';
						changesMade = true;
					}}
					{...$constraints.fullname?.first}
				/>
				<small id="first-name-message">{$errors.fullname?.first}</small>
			</label>

			<label for="middle-name">
				Отчество
				<input
					type="text"
					name="middle-name"
					id="middle-name"
					aria-invalid={Object.keys($errors).length !== 0
						? $errors.fullname && $errors.fullname.middle !== undefined
						: undefined}
					aria-describedby="middle-name-message"
					bind:value={$form.fullname.middle}
					oninput={() => {
						successMessage = '';
						errorMessage = '';
						changesMade = true;
					}}
					{...$constraints.fullname?.middle}
				/>
				<small id="middle-name-message">{$errors.fullname?.middle}</small>
			</label>
		</div>

		<fieldset>
			<legend> Пол </legend>
			<div class="horizontal-fieldset">
				<label for="female">
					<input
						type="radio"
						name="sex"
						value="female"
						id="female"
						bind:group={$form.gender}
						oninput={() => {
							successMessage = '';
							errorMessage = '';
							changesMade = true;
						}}
						{...$constraints.gender}
					/>
					Женский
				</label>
				<label for="male">
					<input
						type="radio"
						name="sex"
						value="male"
						id="male"
						bind:group={$form.gender}
						oninput={() => {
							successMessage = '';
							errorMessage = '';
							changesMade = true;
						}}
						{...$constraints.gender}
					/>
					Мужской
				</label>
			</div>
		</fieldset>

		<button
			type="submit"
			aria-busy={promise !== undefined}
			disabled={!changesMade || promise !== undefined}
			onclick={() => {
				successMessage = '';
				errorMessage = '';
			}}
		>
			{#if data.teacherId}
				{#if promise === undefined}
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
						class="icon icon-tabler icons-tabler-outline icon-tabler-device-floppy"
						><path stroke="none" d="M0 0h24v24H0z" fill="none" /><path
							d="M6 4h10l4 4v10a2 2 0 0 1 -2 2h-12a2 2 0 0 1 -2 -2v-12a2 2 0 0 1 2 -2"
						/><path d="M12 14m-2 0a2 2 0 1 0 4 0a2 2 0 1 0 -4 0" /><path
							d="M14 4l0 4l-6 0l0 -4"
						/></svg
					>
				{/if}
				Сохранить изменения
			{:else}
				{#if promise === undefined}
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
						class="icon icon-tabler icons-tabler-outline icon-tabler-circle-plus"
						><path stroke="none" d="M0 0h24v24H0z" fill="none" /><path
							d="M3 12a9 9 0 1 0 18 0a9 9 0 0 0 -18 0"
						/><path d="M9 12h6" /><path d="M12 9v6" /></svg
					>
				{/if}
				Добавить преподавателя
			{/if}
		</button>
	</form>

	{#if successMessage}
		<p class="form-message success">
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
				class="icon icon-tabler icons-tabler-outline icon-tabler-circle-check"
				><path stroke="none" d="M0 0h24v24H0z" fill="none" /><path
					d="M12 12m-9 0a9 9 0 1 0 18 0a9 9 0 1 0 -18 0"
				/><path d="M9 12l2 2l4 -4" /></svg
			>
			{successMessage}
		</p>
	{/if}
	{#if errorMessage}
		<p class="form-message error">
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
			{errorMessage}
		</p>
	{/if}

	{#if debugMode}
		<SuperDebug data={$form}></SuperDebug>
	{/if}
{/if}

<style>
	.grid {
		row-gap: 0.25em;
	}

	.horizontal-fieldset {
		display: inline-flex;
		flex-wrap: wrap;
		gap: 2em;
	}

	fieldset > legend {
		margin-bottom: 0.15em;
	}

	input[type='text'] {
		margin-bottom: 0;
	}
</style>
