<script lang="ts">
	import { onMount } from 'svelte';
	import { currentTab } from './shared.svelte';

	let mobileLayout: boolean = $state(window.innerWidth < 576);

	let replacementsTab: HTMLButtonElement;
	let timetablesTab: HTMLButtonElement;
	let callScheduleTab: HTMLButtonElement;
	let groupsTab: HTMLButtonElement;
	let subjectsTab: HTMLButtonElement;
	let teachersTab: HTMLButtonElement;

	let groupsGroupBy: 'subject' | 'teacher' | 'none' = $state('subject');

	onMount(() => {
		switch (currentTab.tab) {
			case 'replacements':
				replacementsTab.scrollIntoView({ inline: 'center' });
				break;
			case 'timetables':
				timetablesTab.scrollIntoView({ inline: 'center' });
				break;
			case 'callSchedule':
				callScheduleTab.scrollIntoView({ inline: 'center' });
				break;
			case 'groups':
				groupsTab.scrollIntoView({ inline: 'center' });
				break;
			case 'subjects':
				subjectsTab.scrollIntoView({ inline: 'center' });
				break;
			case 'teachers':
				teachersTab.scrollIntoView({ inline: 'center' });
				break;
		}
	});

	// template data
	interface Teacher {
		id: string;
		name: { first: string; last: string; middle?: string };
		gender: string;
	}
	interface Subject {
		id: string;
		name: string;
		shortName: string;
		optional: boolean;
	}
	interface Group {
		id: string;
		subject: Subject;
		teacher: Teacher;
		classroom: string;
		attendPeriodicity: number;
	}

	const teachers: Teacher[] = [
		{
			id: 'tea-1',
			name: {
				first: 'Андрей',
				last: 'Поздняков',
				middle: 'Владимирович'
			},
			gender: 'male'
		},
		{
			id: 'tea-2',
			name: {
				first: 'Андрей2',
				last: 'Поздняков2',
				middle: 'Владимирович2'
			},
			gender: 'female'
		},
		{
			id: 'tea-3',
			name: {
				first: 'Светлана',
				last: 'Штаркер',
				middle: 'Анатольевна'
			},
			gender: 'female'
		},
		{
			id: 'tea-4',
			name: {
				first: 'Мария',
				last: 'Заворохина',
				middle: 'Вадимовна'
			},
			gender: 'female'
		},
		{
			id: 'tea-5',
			name: {
				first: 'Любовь',
				last: 'Прокофьева',
				middle: 'Валентиновна'
			},
			gender: 'female'
		},
		{
			id: 'tea-6',
			name: {
				first: 'Евгений',
				last: 'Турчанов',
				middle: 'Валентинович'
			},
			gender: 'male'
		}
	];
	const subjects: Subject[] = [
		{
			id: 'sub-1',
			name: 'Информатика',
			shortName: 'Информ.',
			optional: false
		},
		{
			id: 'sub-2',
			name: 'Литература',
			shortName: '',
			optional: false
		},
		{
			id: 'sub-3',
			name: 'Биология',
			shortName: '',
			optional: false
		},
		{
			id: 'sub-4',
			name: 'Физика СК',
			shortName: '',
			optional: false
		},
		{
			id: 'sub-5',
			name: 'История ВНД',
			shortName: '',
			optional: true
		}
	];
	const groups: Group[] = [
		{
			id: 'grp-1',
			subject: {
				id: 'sub-1',
				name: 'Информатика',
				shortName: 'Информ.',
				optional: false
			},
			teacher: {
				id: 'tea-1',
				name: {
					first: 'Андрей',
					last: 'Поздняков',
					middle: 'Владимирович'
				},
				gender: 'male'
			},
			classroom: '307',
			attendPeriodicity: 1
		},
		{
			id: 'grp-2',
			subject: {
				id: 'sub-1',
				name: 'Информатика',
				shortName: 'Информ.',
				optional: false
			},
			teacher: {
				id: 'tea-2',
				name: {
					first: 'Андрей2',
					last: 'Поздняков2',
					middle: 'Владимирович2'
				},
				gender: 'female'
			},
			classroom: '203л',
			attendPeriodicity: 1
		},
		{
			id: 'grp-3',
			subject: {
				id: 'sub-2',
				name: 'Литература',
				shortName: '',
				optional: false
			},
			teacher: {
				id: 'tea-3',
				name: {
					first: 'Светлана',
					last: 'Штаркер',
					middle: 'Анатольевна'
				},
				gender: 'female'
			},
			classroom: '106',
			attendPeriodicity: 1
		},
		{
			id: 'grp-4',
			subject: {
				id: 'sub-3',
				name: 'Биология',
				shortName: '',
				optional: false
			},
			teacher: {
				id: 'tea-4',
				name: {
					first: 'Мария',
					last: 'Заворохина',
					middle: 'Вадимовна'
				},
				gender: 'female'
			},
			classroom: '201',
			attendPeriodicity: 1
		},
		{
			id: 'grp-5',
			subject: {
				id: 'sub-4',
				name: 'Физика СК',
				shortName: '',
				optional: false
			},
			teacher: {
				id: 'tea-5',
				name: {
					first: 'Любовь',
					last: 'Прокофьева',
					middle: 'Валентиновна'
				},
				gender: 'female'
			},
			classroom: '407',
			attendPeriodicity: 1
		},
		{
			id: 'grp-6',
			subject: {
				id: 'sub-5',
				name: 'История ВНД',
				shortName: '',
				optional: true
			},
			teacher: {
				id: 'tea-6',
				name: {
					first: 'Евгений',
					last: 'Турчанов',
					middle: 'Валентинович'
				},
				gender: 'male'
			},
			classroom: '303',
			attendPeriodicity: 1
		}
	];
	const groupsBySubject: {
		[subjectId: string]: Group[];
	} = {
		'sub-1': [
			{
				id: 'grp-1',
				subject: {
					id: 'sub-1',
					name: 'Информатика',
					shortName: 'Информ.',
					optional: false
				},
				teacher: {
					id: 'tea-1',
					name: {
						first: 'Андрей',
						last: 'Поздняков',
						middle: 'Владимирович'
					},
					gender: 'male'
				},
				classroom: '307',
				attendPeriodicity: 1
			},
			{
				id: 'grp-2',
				subject: {
					id: 'sub-1',
					name: 'Информатика',
					shortName: 'Информ.',
					optional: false
				},
				teacher: {
					id: 'tea-2',
					name: {
						first: 'Андрей2',
						last: 'Поздняков2',
						middle: 'Владимирович2'
					},
					gender: 'female'
				},
				classroom: '203л',
				attendPeriodicity: 1
			}
		],
		'sub-2': [
			{
				id: 'grp-3',
				subject: {
					id: 'sub-2',
					name: 'Литература',
					shortName: '',
					optional: false
				},
				teacher: {
					id: 'tea-3',
					name: {
						first: 'Светлана',
						last: 'Штаркер',
						middle: 'Анатольевна'
					},
					gender: 'female'
				},
				classroom: '106',
				attendPeriodicity: 1
			}
		],
		'sub-3': [
			{
				id: 'grp-4',
				subject: {
					id: 'sub-3',
					name: 'Биология',
					shortName: '',
					optional: false
				},
				teacher: {
					id: 'tea-4',
					name: {
						first: 'Мария',
						last: 'Заворохина',
						middle: 'Вадимовна'
					},
					gender: 'female'
				},
				classroom: '201',
				attendPeriodicity: 1
			}
		],
		'sub-4': [
			{
				id: 'grp-5',
				subject: {
					id: 'sub-4',
					name: 'Физика СК',
					shortName: '',
					optional: false
				},
				teacher: {
					id: 'tea-5',
					name: {
						first: 'Любовь',
						last: 'Прокофьева',
						middle: 'Валентиновна'
					},
					gender: 'female'
				},
				classroom: '407',
				attendPeriodicity: 1
			}
		],
		'sub-5': [
			{
				id: 'grp-6',
				subject: {
					id: 'sub-5',
					name: 'История ВНД',
					shortName: '',
					optional: true
				},
				teacher: {
					id: 'tea-6',
					name: {
						first: 'Евгений',
						last: 'Турчанов',
						middle: 'Валентинович'
					},
					gender: 'male'
				},
				classroom: '303',
				attendPeriodicity: 1
			}
		]
	};
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
<h1>Панель управления</h1>

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
		class={['secondary', 'tab', currentTab.tab === 'callSchedule' ? '' : 'outline']}
		bind:this={callScheduleTab}
		onclick={() => {
			currentTab.tab = 'callSchedule';
			callScheduleTab.scrollIntoView({ inline: 'center', behavior: 'smooth' });
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
			class="icon icon-tabler icons-tabler-outline icon-tabler-bell"
			><path stroke="none" d="M0 0h24v24H0z" fill="none" /><path
				d="M10 5a2 2 0 1 1 4 0a7 7 0 0 1 4 6v3a4 4 0 0 0 2 3h-16a4 4 0 0 0 2 -3v-3a7 7 0 0 1 4 -6"
			/><path d="M9 17v1a3 3 0 0 0 6 0v-1" /></svg
		>
		Звонки
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

{#if currentTab.tab === 'replacements'}
	<!-- REPLACEMENTS TAB -->
{:else if currentTab.tab === 'timetables'}
	<!-- TIMETABLES TAB -->
	<a role="button" href="/manage/timetable">
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
	{#each { length: 3 } as _, timetableId}
		<article>
			<header class="resource-header">
				<span><b>10А</b></span>
				<a href={'/manage/timetable/' + timetableId} aria-label="Редактировать">
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
					{#if !mobileLayout}
						Редактировать
					{/if}
				</a>
			</header>
			<div>
				<span>Пол: Харчишин</span>
			</div>
		</article>
	{/each}
{:else if currentTab.tab === 'callSchedule'}
	<!-- CALL SCHEDULE -->
{:else if currentTab.tab === 'groups'}
	<!-- GROUPS TAB -->
	<div class="filter">
		<div class="filter-left">
			<select name="group-by" bind:value={groupsGroupBy} id="group-by">
				<option value="subject">По предметам</option>
				<option value="teacher">По преподавателям</option>
				<!-- <option value="none">Не группировать</option> -->
			</select>
		</div>
		<div class="filter-right">
			<a role="button" href="/manage/group" class="icon-button">
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
				{#if !mobileLayout}
					Добавить группу
				{/if}
			</a>
		</div>
	</div>
	{#if groupsGroupBy === 'subject'}
		{#each Object.keys(groupsBySubject) as subjectId (subjectId)}
			<details open>
				<summary><b>{groupsBySubject[subjectId][0].subject.name}</b></summary>
				{#each groupsBySubject[subjectId] as group, groupId (group.id)}
					<article>
						<header class="resource-header">
							<span>
								Группа «<b>{group.id}</b>»
							</span>
							<a href={'/manage/group/' + groupId} aria-label="Редактировать">
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
								{#if !mobileLayout}
									Редактировать
								{/if}
							</a>
						</header>
						<div>
							<ul>
								<li>
									Предмет:
									<a href={'/manage/subject/' + group.subject.id}>
										<b>
											{#if mobileLayout && group.subject.shortName && group.subject.shortName.length !== 0}
												{group.subject.shortName}
											{:else}
												{group.subject.name}
											{/if}
										</b>
									</a>
								</li>
								<li>
									Преподаватель:
									<a href={'/manage/teacher/' + group.teacher.id}>
										<b>
											{#if mobileLayout}
												{group.teacher.name.last}
												{group.teacher.name.first[0]}.
												{group.teacher.name.middle ? group.teacher.name.middle[0] : ''}.
											{:else}
												{group.teacher.name.last}
												{group.teacher.name.first}
												{group.teacher.name.middle}
											{/if}
										</b>
									</a>
								</li>
								<li>
									Кабинет:
									<b>
										{group.classroom}
									</b>
								</li>
								{#if group.attendPeriodicity > 1}
									<li>
										Посещение каждые
										<b>
											{group.attendPeriodicity} недели
										</b>
									</li>
								{/if}
							</ul>
						</div>
					</article>
				{/each}
			</details>
		{/each}
	{:else if groupsGroupBy === 'teacher'}
		<!-- TODO: Сделать визуализацию данных при группировке по учителям -->
	{:else if groupsGroupBy === 'none'}
		<!-- TODO: Сделать визуализацию данных при отсутствии группировки групп -->
	{/if}
{:else if currentTab.tab === 'subjects'}
	<!-- SUBJECTS TAB -->
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
	{#each subjects as subject, subjectId (subject.id)}
		{#if mobileLayout}
			<article>
				{#if subject.shortName || subject.optional}
					<header class="resource-header">
						<b>{subject.name}</b>
						<a href={'/manage/subject/' + subjectId} aria-label="Редактировать">
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
						</a>
					</header>
					<div>
						<ul>
							{#if subject.shortName}
								<li>
									Сокращённое название: <b>{subject.shortName}</b>
								</li>
							{/if}
							{#if subject.optional}
								<li>Посещение по желанию</li>
							{/if}
						</ul>
					</div>
				{:else}
					<span class="resource-header">
						<b>{subject.name}</b>
						<a href={'/manage/subject/' + subject.id} aria-label="Редактировать">
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
							{#if !mobileLayout}
								Редактировать
							{/if}
						</a>
					</span>
				{/if}
			</article>
		{:else}
			<article class="resource-header">
				<span>
					{#if subject.optional}
						<em data-tooltip="Посещение по желанию">{subject.name}</em>
					{:else}
						<b>{subject.name}</b>
					{/if}
					{#if subject.shortName}
						({subject.shortName})
					{/if}
				</span>
				<a href={'/manage/subject/' + subjectId} aria-label="Редактировать">
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
					{#if !mobileLayout}
						Редактировать
					{/if}
				</a>
			</article>
		{/if}
	{/each}
{:else if currentTab.tab === 'teachers'}
	<!-- TEACHERS TAB -->
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
	{#each teachers as teacher, teacherId (teacher.id)}
		<article>
			<div class="resource-header">
				<span>
					{#if mobileLayout}
						<b>{teacher.name.last}</b>
						{teacher.name.first[0]}. {teacher.name.middle ? teacher.name.middle[0] : ''}.
					{:else}
						{teacher.name.first} {teacher.name.middle} <b>{teacher.name.last}</b>
					{/if}
				</span>
				<a href={'/manage/teacher/' + teacherId} aria-label="Редактировать">
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
					{#if !mobileLayout}
						Редактировать
					{/if}
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

	.filter {
		display: grid;
		grid-template-columns: 1fr auto;
		gap: 0.5em;

		padding: 0.5em;
		margin-bottom: 1em;

		background-color: var(--pico-form-element-background-color);
		border-radius: var(--pico-border-radius);
	}

	.filter > .filter-left,
	.filter > .filter-right {
		display: flex;
		align-items: center;
		gap: 0.5em;
	}

	.filter-left > select {
		width: 20ch;
		padding: 0.5em;
		margin-bottom: 0;
	}

	.filter-right > a[role='button'] {
		width: max-content;
		padding: 0.5em;
		margin-bottom: 0;

		white-space: nowrap;
	}

	hr {
		margin-top: 0.25em;
		margin-bottom: 0.5em;
	}

	article {
		margin-bottom: 1em;
	}

	details {
		margin-bottom: 2em;
	}

	details > article {
		margin-bottom: 0.5em;
	}

	.resource-header {
		display: flex;
		justify-content: space-between;
	}

	ul {
		margin-bottom: 0;
	}
</style>
