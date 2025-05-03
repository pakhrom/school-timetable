<script lang="ts">
	import { currentTab } from './shared.svelte';

	let mobileLayout: boolean = $state(window.innerWidth < 576);
</script>

<svelte:window
	onresize={() => {
		mobileLayout = window.innerWidth < 576;
	}}
/>

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

<div class="tabs-container">
	<button
		class={['secondary', 'tab', currentTab.tab === 'timetables' ? '' : 'outline']}
		onclick={() => {
			currentTab.tab = 'timetables';
		}}
	>
		Расписания
	</button>
	<button
		class={['secondary', 'tab', currentTab.tab === 'subjects' ? '' : 'outline']}
		onclick={() => {
			currentTab.tab = 'subjects';
		}}
	>
		Предметы
	</button>
	<button
		class={['secondary', 'tab', currentTab.tab === 'teachers' ? '' : 'outline']}
		onclick={() => {
			currentTab.tab = 'teachers';
		}}
	>
		Преподаватели
	</button>
	<span class="tab hidden">I</span>
</div>
<hr />

{#if currentTab.tab === 'timetables'}
	<a role="button" href="/manage/subject">
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
		Добавить расписание
	</a>
	{#each { length: 3 } as _, subjectId}
		<article>
			<header class="resource-header">
				<span><b>10А</b></span>
				<a href={'/manage/timetable/' + subjectId}>
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
						class="icon icon-tabler icons-tabler-outline icon-tabler-edit"
						><path stroke="none" d="M0 0h24v24H0z" fill="none" /><path
							d="M7 7h-1a2 2 0 0 0 -2 2v9a2 2 0 0 0 2 2h9a2 2 0 0 0 2 -2v-1"
						/><path
							d="M20.385 6.585a2.1 2.1 0 0 0 -2.97 -2.97l-8.415 8.385v3h3l8.385 -8.415z"
						/><path d="M16 5l3 3" /></svg
					>
					Редактировать
				</a>
			</header>
			<div>
				<span>Пол: Харчишин</span>
			</div>
		</article>
	{/each}
{:else if currentTab.tab === 'subjects'}
	<a role="button" href="/manage/subject">
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
	</a>
	{#each { length: 3 } as _, subjectId}
		<article>
			<header class="resource-header">
				<span><b>Математика</b></span>
				<a href={'/manage/subject/' + subjectId}>
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
						class="icon icon-tabler icons-tabler-outline icon-tabler-edit"
						><path stroke="none" d="M0 0h24v24H0z" fill="none" /><path
							d="M7 7h-1a2 2 0 0 0 -2 2v9a2 2 0 0 0 2 2h9a2 2 0 0 0 2 -2v-1"
						/><path
							d="M20.385 6.585a2.1 2.1 0 0 0 -2.97 -2.97l-8.415 8.385v3h3l8.385 -8.415z"
						/><path d="M16 5l3 3" /></svg
					>
					Редактировать
				</a>
			</header>
			<div>
				<span>Пол: Харчишин</span>
			</div>
		</article>
	{/each}
{:else if currentTab.tab === 'teachers'}
	<a role="button" href="/manage/teacher">
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
	</a>
	{#each { length: 3 } as _, teacherId}
		<article>
			<header class="resource-header">
				<span>
					<b>
						{#if mobileLayout}
							Фамилия И.О.
						{:else}
							Фамилия Имя Отчество
						{/if}
					</b>
				</span>
				<a href={'/manage/teacher/' + teacherId}>
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
						class="icon icon-tabler icons-tabler-outline icon-tabler-edit"
						><path stroke="none" d="M0 0h24v24H0z" fill="none" /><path
							d="M7 7h-1a2 2 0 0 0 -2 2v9a2 2 0 0 0 2 2h9a2 2 0 0 0 2 -2v-1"
						/><path
							d="M20.385 6.585a2.1 2.1 0 0 0 -2.97 -2.97l-8.415 8.385v3h3l8.385 -8.415z"
						/><path d="M16 5l3 3" /></svg
					>
					Редактировать
				</a>
			</header>
			<div>
				<span>Пол: Харчишин</span>
			</div>
		</article>
	{/each}
{:else}
	Хватит приложение ломать
{/if}

<style>
	.tabs-container {
		display: inline-flex;
		justify-content: flex-start;
		align-items: center;
		gap: 0.5em;

		height: 2em;
	}

	.tab {
		padding: 0.1em 0.5em;

		border-color: transparent;

		transition: all 0.2s;
	}

	.tab.outline {
		font-size: 0.9em;
	}

	.tab:hover {
		border-color: var(--pico-secondary-border);
	}

	.hidden {
		visibility: hidden;
	}

	hr {
		margin-top: 0.25em;
		margin-bottom: 0.5em;
	}

	article {
		margin-bottom: 1em;
	}

	.resource-header {
		display: flex;
		justify-content: space-between;
	}
</style>
