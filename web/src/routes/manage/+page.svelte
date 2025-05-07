<script lang="ts">
	import { onMount } from 'svelte';
	import { currentTab } from './shared.svelte';

	let mobileLayout: boolean = $state(window.innerWidth < 576);

	let replacementsTab: HTMLButtonElement;
	let timetablesTab: HTMLButtonElement;
	let groupsTab: HTMLButtonElement;
	let subjectsTab: HTMLButtonElement;
	let teachersTab: HTMLButtonElement;

	onMount(() => {
		switch (currentTab.tab) {
			case 'replacements':
				replacementsTab.scrollIntoView({ inline: 'center' });
				break;
			case 'timetables':
				timetablesTab.scrollIntoView({ inline: 'center' });
				break;
			case 'groups':
				groupsTab.scrollIntoView({ inline: 'center' });
				break;
			case 'subts':
				subtsTab.scrollIntoView({ inline: 'center' });
				break;
			case 'teachers':
				teachersTab.scrollIntoView({ inline: 'center' });
				break;
		}
	});
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
		class={['secondary', 'tab', currentTab.tab === 'replacements' ? '' : 'outline']}
		bind:this={replacementsTab}
		onclick={() => {
			currentTab.tab = 'replacements';
			replacementsTab.scrollIntoView({ inline: 'center', behavior: 'smooth' });
		}}
	>
		<svg
			xmlns="http://www.w3.org/2000/svg"
			width="20"
			height="20"
			viewBox="0 0 24 24"
			fill="none"
			stroke="currentColor"
			stroke-width="2"
			stroke-linecap="round"
			stroke-linejoin="round"
			class="icon icon-tabler icons-tabler-outline icon-tabler-replace-user"
			><path stroke="none" d="M0 0h24v24H0z" fill="none" /><path
				d="M21 11v-3c0 -.53 -.211 -1.039 -.586 -1.414c-.375 -.375 -.884 -.586 -1.414 -.586h-6m0 0l3 3m-3 -3l3 -3"
			/><path
				d="M3 13.013v3c0 .53 .211 1.039 .586 1.414c.375 .375 .884 .586 1.414 .586h6m0 0l-3 -3m3 3l-3 3"
			/><path
				d="M16 16.502c0 .53 .211 1.039 .586 1.414c.375 .375 .884 .586 1.414 .586c.53 0 1.039 -.211 1.414 -.586c.375 -.375 .586 -.884 .586 -1.414c0 -.53 -.211 -1.039 -.586 -1.414c-.375 -.375 -.884 -.586 -1.414 -.586c-.53 0 -1.039 .211 -1.414 .586c-.375 .375 -.586 .884 -.586 1.414z"
			/><path
				d="M4 4.502c0 .53 .211 1.039 .586 1.414c.375 .375 .884 .586 1.414 .586c.53 0 1.039 -.211 1.414 -.586c.375 -.375 .586 -.884 .586 -1.414c0 -.53 -.211 -1.039 -.586 -1.414c-.375 -.375 -.884 -.586 -1.414 -.586c-.53 0 -1.039 .211 -1.414 .586c-.375 .375 -.586 .884 -.586 1.414z"
			/><path
				d="M21 21.499c0 -.53 -.211 -1.039 -.586 -1.414c-.375 -.375 -.884 -.586 -1.414 -.586h-2c-.53 0 -1.039 .211 -1.414 .586c-.375 .375 -.586 .884 -.586 1.414"
			/><path
				d="M9 9.499c0 -.53 -.211 -1.039 -.586 -1.414c-.375 -.375 -.884 -.586 -1.414 -.586h-2c-.53 0 -1.039 .211 -1.414 .586c-.375 .375 -.586 .884 -.586 1.414"
			/></svg
		>
		Замены
	</button>
	<button
		class={['secondary', 'tab', currentTab.tab === 'timetables' ? '' : 'outline']}
		bind:this={timetablesTab}
		onclick={() => {
			currentTab.tab = 'timetables';
			timetablesTab.scrollIntoView({ inline: 'center', behavior: 'smooth' });
		}}
	>
		<svg
			xmlns="http://www.w3.org/2000/svg"
			width="20"
			height="20"
			viewBox="0 0 24 24"
			fill="none"
			stroke="currentColor"
			stroke-width="2"
			stroke-linecap="round"
			stroke-linejoin="round"
			class="icon icon-tabler icons-tabler-outline icon-tabler-calendar-time"
			><path stroke="none" d="M0 0h24v24H0z" fill="none" /><path
				d="M11.795 21h-6.795a2 2 0 0 1 -2 -2v-12a2 2 0 0 1 2 -2h12a2 2 0 0 1 2 2v4"
			/><path d="M18 18m-4 0a4 4 0 1 0 8 0a4 4 0 1 0 -8 0" /><path d="M15 3v4" /><path
				d="M7 3v4"
			/><path d="M3 11h16" /><path d="M18 16.496v1.504l1 1" /></svg
		>
		Расписания
	</button>
	<button
		class={['secondary', 'tab', currentTab.tab === 'groups' ? '' : 'outline']}
		bind:this={groupsTab}
		onclick={() => {
			currentTab.tab = 'groups';
			groupsTab.scrollIntoView({ inline: 'center', behavior: 'smooth' });
		}}
	>
		<svg
			xmlns="http://www.w3.org/2000/svg"
			width="20"
			height="20"
			viewBox="0 0 24 24"
			fill="none"
			stroke="currentColor"
			stroke-width="2"
			stroke-linecap="round"
			stroke-linejoin="round"
			class="icon icon-tabler icons-tabler-outline icon-tabler-users-group"
			><path stroke="none" d="M0 0h24v24H0z" fill="none" /><path
				d="M10 13a2 2 0 1 0 4 0a2 2 0 0 0 -4 0"
			/><path d="M8 21v-1a2 2 0 0 1 2 -2h4a2 2 0 0 1 2 2v1" /><path
				d="M15 5a2 2 0 1 0 4 0a2 2 0 0 0 -4 0"
			/><path d="M17 10h2a2 2 0 0 1 2 2v1" /><path d="M5 5a2 2 0 1 0 4 0a2 2 0 0 0 -4 0" /><path
				d="M3 13v-1a2 2 0 0 1 2 -2h2"
			/></svg
		>
		Группы
	</button>
	<button
		class={['secondary', 'tab', currentTab.tab === 'subjects' ? '' : 'outline']}
		bind:this={subjectsTab}
		onclick={() => {
			currentTab.tab = 'subjects';
			subjectsTab.scrollIntoView({ inline: 'center', behavior: 'smooth' });
		}}
	>
		<svg
			xmlns="http://www.w3.org/2000/svg"
			width="20"
			height="20"
			viewBox="0 0 24 24"
			fill="none"
			stroke="currentColor"
			stroke-width="2"
			stroke-linecap="round"
			stroke-linejoin="round"
			class="icon icon-tabler icons-tabler-outline icon-tabler-math"
			><path stroke="none" d="M0 0h24v24H0z" fill="none" /><path d="M19 5h-7l-4 14l-3 -6h-2" /><path
				d="M14 13l6 6"
			/><path d="M14 19l6 -6" /></svg
		>
		Предметы
	</button>
	<button
		class={['secondary', 'tab', currentTab.tab === 'teachers' ? '' : 'outline']}
		bind:this={teachersTab}
		onclick={() => {
			currentTab.tab = 'teachers';
			teachersTab.scrollIntoView({ inline: 'center', behavior: 'smooth' });
		}}
	>
		<svg
			xmlns="http://www.w3.org/2000/svg"
			width="20"
			height="20"
			viewBox="0 0 24 24"
			fill="none"
			stroke="currentColor"
			stroke-width="2"
			stroke-linecap="round"
			stroke-linejoin="round"
			class="icon icon-tabler icons-tabler-outline icon-tabler-school"
			><path stroke="none" d="M0 0h24v24H0z" fill="none" /><path
				d="M22 9l-10 -4l-10 4l10 4l10 -4v6"
			/><path d="M6 10.6v5.4a6 3 0 0 0 12 0v-5.4" /></svg
		>
		Преподаватели
	</button>
</div>
<hr />

{#if currentTab.tab === 'replacements'}{:else if currentTab.tab === 'timetables'}
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
{:else if currentTab.tab === 'groups'}{:else if currentTab.tab === 'subjects'}
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
				<b>Программирование</b>
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
				<ul>
					<li>
						Сокращённое название: <b>Прогр.</b>
					</li>
					<li>
						Обязательно к посящению: <b>Да</b>
					</li>
				</ul>
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
			<div class="resource-header">
				<b>
					{#if mobileLayout}
						Фамилия И.О.
					{:else}
						Фамилия Имя Отчество
					{/if}
				</b>
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
			</div>
		</article>
	{/each}
{:else}
	Хватит приложение ломать
{/if}

<style>
	.tabs-container {
		display: flex;
		justify-content: flex-start;
		align-items: center;
		gap: 0.5em;

		height: 2em;
		padding-left: 0.2em;
		padding-right: 0.2em;
		overflow-x: auto;

		-ms-overflow-style: none;
		scrollbar-width: none;
	}

	.tabs-container::-webkit-scrollbar {
		display: none;
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

	ul {
		margin-bottom: 0;
	}
</style>
