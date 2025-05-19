<script lang="ts">
	import SuperDebug, { superForm } from 'sveltekit-superforms';
	import { zod } from 'sveltekit-superforms/adapters';
	import { subjectWrite } from '$lib/schemas/subject.js';
	import { baseUrl } from '$lib/secrets/secrets';
	import { debugMode } from '../../../shared.js';
	import { goto } from '$app/navigation';

	let { data } = $props();

	let changesMade = $state(false);

	let promise: Promise<void> | undefined = $state();
	let successMessage: string = $state('');
	let errorMessage: string = $state('');

	const { form, constraints, errors, enhance } = superForm(data.form, {
		SPA: true,
		resetForm: false,
		validators: zod(subjectWrite),
		onUpdate({ form }) {
			if (form.valid) {
				promise = fetch(baseUrl + '/subjects/' + (data.subjectId ? data.subjectId : ''), {
					method: data.subjectId ? 'PUT' : 'POST',
					body: JSON.stringify(form.data),
					headers: {
						'Content-Type': 'application/json',
						token: data.token
					}
				})
					.then(async (response) => {
						if (response.ok) {
							successMessage = data.subjectId
								? 'Предмет был успешно обновлён.'
								: 'Предмет был успешно добавлен.';

							changesMade = false;
							promise = undefined;

							if (!data.subjectId) {
								goto('/manage/subjects');
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
	{#if !data.subjectId}
		Добавление предмета
	{:else if !data.error}
		Редактирование предмета
	{:else}
		Предмет не был найден
	{/if}
</h1>

<form action="POST" use:enhance>
	<div class="grid">
		<label for="name">
			Название*
			<input
				type="text"
				name="name"
				id="name"
				aria-invalid={Object.keys($errors).length !== 0
					? $errors.fullName !== undefined
					: undefined}
				aria-describedby="name-message"
				bind:value={$form.fullName}
				oninput={() => {
					successMessage = '';
					errorMessage = '';
					changesMade = true;
				}}
				{...$constraints.fullName}
			/>
			<small id="name-message">
				{$errors.fullName}
			</small>
		</label>
		<label for="short-name">
			Сокращённое название
			<input
				type="text"
				name="short-name"
				id="short-name"
				aria-invalid={Object.keys($errors).length !== 0 && $form.fullName.length <= 10
					? $errors.shortName !== undefined
					: undefined}
				aria-describedby="short-name-message"
				bind:value={$form.shortName}
				oninput={() => {
					successMessage = '';
					errorMessage = '';
					changesMade = true;
				}}
				{...$constraints.shortName}
			/>
			<small id="short-name-message">
				{#if $form.fullName.length > 10 && (($form.shortName?.length && $form.shortName.length === 0) || !$form.shortName)}
					Название предмета очень длинное, рекомендуется назначить сокращённое название.
					<br />
				{/if}
				{$errors.shortName}
			</small>
		</label>
	</div>

	<label for="optional">
		<input
			type="checkbox"
			role="switch"
			name="optional"
			id="optional"
			aria-describedby="optional-message"
			bind:checked={$form.optional}
			oninput={() => {
				successMessage = '';
				errorMessage = '';
				changesMade = true;
			}}
			{...$constraints.optional}
		/>
		Посещение по желанию
	</label>

	<button
		type="submit"
		aria-busy={promise !== undefined}
		disabled={!changesMade || promise !== undefined}
		onclick={() => {
			successMessage = '';
			errorMessage = '';
		}}
	>
		{#if data.subjectId}
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
			Добавить предмет
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

<style>
	.grid {
		row-gap: 0.25em;
	}

	input[type='text'] {
		margin-bottom: 0;
	}

	input[type='checkbox'] {
		margin-top: 0.9em;
		margin-bottom: 1em;
	}
</style>
