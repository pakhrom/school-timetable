<script lang="ts">
	import { slide } from 'svelte/transition';

	let isTeachersDetailsOpen: boolean = $state(false);
	let isSubjectsDetailsOpen: boolean = $state(false);
	let isTimetableListDetailsOpen: boolean = $state(false);

	// DEBUG
	let loadingTeachers = $state(true);
	let loadingSubjects = $state(true);
	let loadingTimetableList = $state(true);

	function loadTeachers() {
		setTimeout(() => {
			loadingTeachers = false;
		}, 300);
	}

	function loadSubjects() {
		setTimeout(() => {
			loadingSubjects = false;
		}, 300);
	}

	function loadTimetableList() {
		setTimeout(() => {
			loadingTimetableList = false;
		}, 300);
	}
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
<h1>Панель администратора</h1>

<details
	bind:open={isTeachersDetailsOpen}
	ontoggle={() => {
		if (!isTeachersDetailsOpen) loadTeachers();
	}}
>
	<summary> Учителя </summary>
	{#if loadingTeachers}
		<progress></progress>
	{:else}
		{#each { length: 3 }}
			<article>
				<h4>Фамилия Имя Отчество</h4>
				БЛА БЛА БЛА БЛА БЛА
			</article>
		{/each}
	{/if}
</details>

<details
	bind:open={isSubjectsDetailsOpen}
	ontoggle={() => {
		if (!isSubjectsDetailsOpen) loadSubjects();
	}}
>
	<summary> Предметы </summary>
	{#if loadingSubjects}
		<progress></progress>
	{:else}
		{#each { length: 3 }}
			<article>
				<div>
					<b>Математика</b>
				</div>
				БЛА БЛА БЛА БЛА БЛА
			</article>
		{/each}
	{/if}
</details>

<details
	bind:open={isTimetableListDetailsOpen}
	ontoggle={() => {
		if (!isTimetableListDetailsOpen) loadTimetableList();
	}}
>
	<summary> Расписания </summary>
	{#if loadingTimetableList}
		<progress></progress>
	{:else}
		{#each { length: 3 }}
			<article>
				<h4>Класс</h4>
				БЛА БЛА БЛА БЛА БЛА
			</article>
		{/each}
	{/if}
</details>

<style>
	a {
		display: inline-flex;
		align-items: center;
		gap: 0.25em;

		text-decoration: none;
	}

	details {
		margin-top: 2em;
	}
</style>
