<script lang="ts">
	import SuperDebug, { superForm } from 'sveltekit-superforms';
	import { zod } from 'sveltekit-superforms/adapters';
	import { teacherWrite } from '$lib/schemas/teacher.js';
	import { debugMode } from '../../../shared.js';

	let { data } = $props();

	let changesMade = $state(false);

	const { form, constraints, errors, enhance } = superForm(data.form, {
		dataType: 'json',
		SPA: true,
		resetForm: false,
		validators: zod(teacherWrite),
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
	{#if data.teacherId}
		Редактирование преподавателя
	{:else}
		Добавление преподавателя
	{/if}
</h1>

<form action="POST" use:enhance>
	<div class="grid">
		<label for="first-name">
			Имя*
			<input
				type="text"
				name="first-name"
				id="first-name"
				aria-invalid={Object.keys($errors).length !== 0
					? $errors.name && $errors.name.first !== undefined
					: undefined}
				aria-describedby="first-name-message"
				bind:value={$form.name.first}
				oninput={() => {
					changesMade = true;
				}}
				{...$constraints.name?.first}
			/>
			<small id="first-name-message">{$errors.name?.first}</small>
		</label>

		<label for="last-name">
			Фамилия*
			<input
				type="text"
				name="last-name"
				id="last-name"
				aria-invalid={Object.keys($errors).length !== 0
					? $errors.name && $errors.name.last !== undefined
					: undefined}
				aria-describedby="last-name-message"
				bind:value={$form.name.last}
				oninput={() => {
					changesMade = true;
				}}
				{...$constraints.name?.last}
			/>
			<small id="last-name-message">{$errors.name?.last}</small>
		</label>

		<label for="middle-name">
			Отчество
			<input
				type="text"
				name="middle-name"
				id="middle-name"
				aria-invalid={Object.keys($errors).length !== 0
					? $errors.name && $errors.name.middle !== undefined
					: undefined}
				aria-describedby="middle-name-message"
				bind:value={$form.name.middle}
				oninput={() => {
					changesMade = true;
				}}
				{...$constraints.name?.middle}
			/>
			<small id="middle-name-message">{$errors.name?.middle}</small>
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
						changesMade = true;
					}}
					{...$constraints.gender}
				/>
				Мужской
			</label>
		</div>
	</fieldset>

	<button type="submit" disabled={!changesMade}>
		{#if data.teacherId}
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
			Добавить преподавателя
		{/if}
	</button>
</form>

{#if debugMode}
	<SuperDebug data={$form}></SuperDebug>
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
