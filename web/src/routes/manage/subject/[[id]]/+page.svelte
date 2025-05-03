<script lang="ts">
	import { subjectWrite } from '$lib/schemas/subject.js';
	import SuperDebug, { superForm } from 'sveltekit-superforms';
	import { zod } from 'sveltekit-superforms/adapters';

	let { data } = $props();

	let changesMade = $state(false);

	const { form, constraints, errors, enhance } = superForm(data.form, {
		SPA: true,
		resetForm: false,
		validators: zod(subjectWrite),
		onUpdate({ form }) {
			if (form.valid) {
				changesMade = false;
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
	{#if data.subjectId}
		Редактирование предмета
	{:else}
		Добавление предмета
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
				aria-invalid={Object.keys($errors).length !== 0 ? $errors.name !== undefined : undefined}
				aria-describedby="name-message"
				bind:value={$form.name}
				oninput={() => {
					changesMade = true;
				}}
				{...$constraints.name}
			/>
			<small id="name-message">
				{$errors.name}
			</small>
		</label>
		<label for="short-name">
			Сокращённое название
			<input
				type="text"
				name="short-name"
				id="short-name"
				aria-invalid={Object.keys($errors).length !== 0
					? $errors.shortName !== undefined || $form.name.length > 12
					: undefined}
				aria-describedby="short-name-message"
				bind:value={$form.shortName}
				oninput={() => {
					changesMade = true;
				}}
				{...$constraints.shortName}
			/>
			<small id="short-name-message">
				{#if $form.name.length > 12}
					Название предмета очень длинное, <strong>крайне рекомендуется</strong> назначить
					сокращённое название.
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
				changesMade = true;
			}}
			{...$constraints.optional}
		/>
		Посещение по желанию
	</label>

	<button type="submit" disabled={!changesMade}>
		{#if data.subjectId}
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
				/><path d="M12 14m-2 0a2 2 0 1 0 4 0a2 2 0 1 0 -4 0" /><path d="M14 4l0 4l-6 0l0 -4" /></svg
			>
			Сохранить изменения
		{:else}
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
			Добавить предмет
		{/if}
	</button>
</form>

<SuperDebug data={$form}></SuperDebug>

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
