<script lang="ts">
	import { onMount } from 'svelte';
	import { currentTab } from '../shared.svelte';
	import ModalAlert from '$lib/components/modal-alert.svelte';
	import SuperDebug from 'sveltekit-superforms';
	import { baseUrl } from '$lib/secrets/secrets';
	import { debugMode } from '../../shared';
	import { replaceState } from '$app/navigation';

	let { data } = $props();

	let mobileLayout: boolean = $state(window.innerWidth < 768);

	let groupsPromise = fetch(baseUrl + '/groups').then((result) => result.json());
	let groupsBySubjectsPromise = fetch(baseUrl + '/groups?groupBy=subjects').then((result) =>
		result.json()
	);
	let groupsByTeachersPromise = fetch(baseUrl + '/groups?groupBy=teachers').then((result) =>
		result.json()
	);
	let subjectsPromise = fetch(baseUrl + '/subjects').then((result) => result.json());
	let teachersPromise = fetch(baseUrl + '/teachers').then((result) => result.json());

	let tabBar: HTMLDivElement;
	let replacementsTab: HTMLButtonElement;
	let timetablesTab: HTMLButtonElement;
	/* let callScheduleTab: HTMLButtonElement; */
	let groupsTab: HTMLButtonElement;
	let subjectsTab: HTMLButtonElement;
	let teachersTab: HTMLButtonElement;

	let showDeletionConfirmationModal: boolean = $state(false);
	let deletionConfirmation: {
		resourceType:
			| 'replacement'
			| 'timetable'
			| 'callSchedule'
			| 'group'
			| 'subject'
			| 'teacher'
			| undefined;
		resource: any;
	} = $state({
		resourceType: undefined,
		resource: undefined
	});
	let deletionPromise: Promise<void> | undefined = $state();
	let deletionMessage: string = $state('');

	let groupsGroupBy: 'subject' | 'teacher' | 'none' = $state('subject');

	interface Group {
		objId: string;
		updateDate: string;
		subject: Subject;
		teacher: Teacher;
		cabinet: string;
		attendPeriodicity: number;
	}
	interface GroupsBySubjects {
		[subjectId: string]: Group[];
	}
	interface GroupsByTeachers {
		[teacherId: string]: Teacher[];
	}
	interface Subject {
		objId: string;
		updateDate: string;
		shortName: string;
		fullName: string;
		optional: boolean;
	}
	interface Teacher {
		objId: string;
		updateDate: string;
		fullname: {
			first: string;
			last: string;
			middle: string;
		};
		gender: 'female' | 'male';
	}

	onMount(() => {
		if (data.tab) {
			currentTab.tab = data.tab;
		}

		switch (currentTab.tab) {
			case 'replacements':
				replacementsTab.scrollIntoView({ inline: 'center' });
				break;
			case 'timetables':
				timetablesTab.scrollIntoView({ inline: 'center' });
				break;
			/* case 'callSchedule':
				callScheduleTab.scrollIntoView({ inline: 'center' });
				break; */
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

	function scrollTabBar(event: WheelEvent): void {
		event.preventDefault();
		tabBar.scrollBy({ left: event.deltaY < 0 ? -30 : 30 });
	}
</script>

<svelte:window
	onresize={() => {
		mobileLayout = window.innerWidth < 768;
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

<div class="tabs-container" bind:this={tabBar} onwheel={scrollTabBar}>
	<button
		class={['secondary', 'tab', currentTab.tab === 'replacements' ? '' : 'outline']}
		bind:this={replacementsTab}
		onclick={() => {
			currentTab.tab = 'replacements';
			replacementsTab.scrollIntoView({ inline: 'center', block: 'nearest', behavior: 'smooth' });
			replaceState('/manage/replacements', {});
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
			timetablesTab.scrollIntoView({ inline: 'center', block: 'nearest', behavior: 'smooth' });
			replaceState('/manage/timetables', {});
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
	<!-- <button
		class={['secondary', 'tab', currentTab.tab === 'callSchedule' ? '' : 'outline']}
		bind:this={callScheduleTab}
		onclick={() => {
			currentTab.tab = 'callSchedule';
			callScheduleTab.scrollIntoView({ inline: 'center', block: 'nearest', behavior: 'smooth' });
			replaceState('/manage/callSchedule', {});
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
	</button> -->
	<button
		class={['secondary', 'tab', currentTab.tab === 'groups' ? '' : 'outline']}
		bind:this={groupsTab}
		onclick={() => {
			currentTab.tab = 'groups';
			groupsTab.scrollIntoView({ inline: 'center', block: 'nearest', behavior: 'smooth' });
			replaceState('/manage/groups', {});
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
			subjectsTab.scrollIntoView({ inline: 'center', block: 'nearest', behavior: 'smooth' });
			replaceState('/manage/subjects', {});
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
			teachersTab.scrollIntoView({ inline: 'center', block: 'nearest', behavior: 'smooth' });
			replaceState('/manage/teachers', {});
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
	{/each}<!--
{:else if currentTab.tab === 'callSchedule'}
	<!- CALL SCHEDULES TAB -->
{:else if currentTab.tab === 'groups'}
	<!-- GROUPS TAB -->
	{#if !debugMode}
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
			Добавить группу
		</a>
	{:else}
		<div class="filter">
			<div class="filter-left">
				<select name="group-by" bind:value={groupsGroupBy} id="group-by">
					<option value="subject">По предметам</option>
					<option value="teacher">По преподавателям</option>
					<option value="none">Не группировать</option>
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
	{/if}
	{#if groupsGroupBy === 'subject'}
		<!-- GROUPS BY SUBJECTS -->
		{#if groupsBySubjectsPromise}
			{#await groupsBySubjectsPromise}
				<p aria-busy="true">Загрузка групп с сервера...</p>
			{:then groupsBySubjects: GroupsBySubjects}
				{#if Object.entries(groupsBySubjects).length !== 0}
					{#each Object.keys(groupsBySubjects) as subjectId (subjectId)}
						<details open>
							<summary><b>{groupsBySubjects[subjectId][0].subject.fullName}</b></summary>
							{#each groupsBySubjects[subjectId] as group (group.objId)}
								<article>
									<header class="resource-header">
										<span>
											Группа «<b>{group.objId}</b>»
										</span>
										<div>
											<a href={'/manage/group/' + group.objId} aria-label="Редактировать">
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
											<button
												class="link-button"
												aria-label="Удалить"
												onclick={() => {
													deletionConfirmation.resourceType = 'group';
													deletionConfirmation.resource = group;
													showDeletionConfirmationModal = true;
												}}
											>
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
													class="icon icon-tabler icons-tabler-outline icon-tabler-trash"
													><path stroke="none" d="M0 0h24v24H0z" fill="none" /><path
														d="M4 7l16 0"
													/><path d="M10 11l0 6" /><path d="M14 11l0 6" /><path
														d="M5 7l1 12a2 2 0 0 0 2 2h8a2 2 0 0 0 2 -2l1 -12"
													/><path d="M9 7v-3a1 1 0 0 1 1 -1h4a1 1 0 0 1 1 1v3" /></svg
												>
											</button>
										</div>
									</header>
									<div>
										<ul>
											<li>
												{#if !mobileLayout}
													Предмет:
												{/if}
												<a href={'/manage/subject/' + group.subject.objId}>
													<b>
														{#if mobileLayout && group.subject.shortName && group.subject.shortName.length !== 0}
															{group.subject.shortName}
														{:else}
															{group.subject.fullName}
														{/if}
													</b>
												</a>
											</li>
											<li>
												{#if !mobileLayout}
													Преподаватель:
												{/if}
												<a href={'/manage/teacher/' + group.teacher.objId}>
													<b>
														{#if mobileLayout}
															{group.teacher.fullname.last}
															{group.teacher.fullname.first[0]}.
															{group.teacher.fullname.middle
																? group.teacher.fullname.middle[0]
																: ''}.
														{:else}
															{group.teacher.fullname.last}
															{group.teacher.fullname.first}
															{group.teacher.fullname.middle}
														{/if}
													</b>
												</a>
											</li>
											<li>
												Кабинет:
												<b>
													{group.cabinet}
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
				{:else}
					Группы отсутствуют. Вы можете добавить новую группу,
					<a href="/manage/group">нажав сюда</a>.
				{/if}
			{:catch err}
				<SuperDebug data={err}></SuperDebug>
			{/await}
		{/if}
	{:else if groupsGroupBy === 'teacher'}
		<!-- GROUPS BY TEACHERS -->
		<!-- TODO: Сделать визуализацию данных при группировке по учителям -->
		{#if groupsByTeachersPromise}
			{#await groupsByTeachersPromise}
				<p aria-busy="true">Загрузка групп с сервера...</p>
			{:catch err}
				<SuperDebug data={err}></SuperDebug>
			{/await}
		{/if}
	{:else if groupsGroupBy === 'none'}
		<!-- ALL GROUPS -->
		<!-- TODO: Сделать визуализацию данных при отсутствии группировки групп -->
		{#if groupsPromise}
			{#await groupsPromise}
				<p aria-busy="true">Загрузка групп с сервера...</p>
			{:then groups: Group[]}
				{#if groups.length !== 0}
					{#each groups as group (group.objId)}
						<article>
							<div class="resource-header">
								<span><b>{group.subject.fullName}</b> - {group.teacher.fullname.last}</span>
								<a href={'/manage/group/' + group.objId} aria-label="Редактировать">
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
							</div>
						</article>
					{/each}
				{:else}
					Группы отсутствуют. Вы можете добавить новую группу,
					<a href="/manage/group">нажав сюда</a>.
				{/if}
				<SuperDebug data={groups}></SuperDebug>
			{:catch err}
				<SuperDebug data={err}></SuperDebug>
			{/await}
		{/if}
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
	{#if subjectsPromise}
		{#await subjectsPromise}
			<p aria-busy="true">Загрузка предметов с сервера...</p>
		{:then subjects: Subject[]}
			{#if subjects.length !== 0}
				{#each subjects as subject (subject.objId)}
					{#if mobileLayout}
						<article>
							{#if subject.shortName || subject.optional}
								<header class="resource-header">
									<b>{subject.fullName}</b>
									<div>
										<a href={'/manage/subject/' + subject.objId} aria-label="Редактировать">
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
										<button
											class="link-button"
											aria-label="Удалить"
											onclick={() => {
												deletionConfirmation.resourceType = 'subject';
												deletionConfirmation.resource = subject;
												showDeletionConfirmationModal = true;
											}}
										>
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
												class="icon icon-tabler icons-tabler-outline icon-tabler-trash"
												><path stroke="none" d="M0 0h24v24H0z" fill="none" /><path
													d="M4 7l16 0"
												/><path d="M10 11l0 6" /><path d="M14 11l0 6" /><path
													d="M5 7l1 12a2 2 0 0 0 2 2h8a2 2 0 0 0 2 -2l1 -12"
												/><path d="M9 7v-3a1 1 0 0 1 1 -1h4a1 1 0 0 1 1 1v3" /></svg
											>
										</button>
									</div>
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
									<b>{subject.fullName}</b>
									<div>
										<a href={'/manage/subject/' + subject.objId} aria-label="Редактировать">
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
										<button
											class="link-button"
											aria-label="Удалить"
											onclick={() => {
												deletionConfirmation.resourceType = 'subject';
												deletionConfirmation.resource = subject;
												showDeletionConfirmationModal = true;
											}}
										>
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
												class="icon icon-tabler icons-tabler-outline icon-tabler-trash"
												><path stroke="none" d="M0 0h24v24H0z" fill="none" /><path
													d="M4 7l16 0"
												/><path d="M10 11l0 6" /><path d="M14 11l0 6" /><path
													d="M5 7l1 12a2 2 0 0 0 2 2h8a2 2 0 0 0 2 -2l1 -12"
												/><path d="M9 7v-3a1 1 0 0 1 1 -1h4a1 1 0 0 1 1 1v3" /></svg
											>
										</button>
									</div>
								</span>
							{/if}
						</article>
					{:else}
						<article class="resource-header">
							<span>
								{#if subject.optional}
									<em data-tooltip="Посещение по желанию">{subject.fullName}</em>
								{:else}
									<b>{subject.fullName}</b>
								{/if}
								{#if subject.shortName}
									({subject.shortName})
								{/if}
							</span>
							<div>
								<a href={'/manage/subject/' + subject.objId} aria-label="Редактировать">
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
								<button
									class="link-button"
									aria-label="Удалить"
									onclick={() => {
										deletionConfirmation.resourceType = 'subject';
										deletionConfirmation.resource = subject;
										showDeletionConfirmationModal = true;
									}}
								>
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
										class="icon icon-tabler icons-tabler-outline icon-tabler-trash"
										><path stroke="none" d="M0 0h24v24H0z" fill="none" /><path d="M4 7l16 0" /><path
											d="M10 11l0 6"
										/><path d="M14 11l0 6" /><path
											d="M5 7l1 12a2 2 0 0 0 2 2h8a2 2 0 0 0 2 -2l1 -12"
										/><path d="M9 7v-3a1 1 0 0 1 1 -1h4a1 1 0 0 1 1 1v3" /></svg
									>
								</button>
							</div>
						</article>
					{/if}
				{/each}
			{:else}
				Предметы отсутствуют. Вы можете добавить новый предмет,
				<a href="/manage/subject">нажав сюда</a>.
			{/if}
			<SuperDebug data={subjects}></SuperDebug>
		{:catch err}
			<SuperDebug data={err}></SuperDebug>
		{/await}
	{/if}
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
	{#await teachersPromise}
		<p aria-busy="true">Загрузка преподавателей с сервера...</p>
	{:then teachers: Teacher[]}
		{#if teachers.length !== 0}
			{#each teachers as teacher (teacher.objId)}
				<article>
					<div class="resource-header">
						<span>
							{#if mobileLayout}
								<b>{teacher.fullname.last}</b>
								{teacher.fullname.first[0]}. {teacher.fullname.middle
									? teacher.fullname.middle[0]
									: ''}.
							{:else}
								<b>{teacher.fullname.last}</b> {teacher.fullname.first} {teacher.fullname.middle}
							{/if}
						</span>
						<div>
							<a href={'/manage/teacher/' + teacher.objId} aria-label="Редактировать">
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
							<button
								class="link-button"
								aria-label="Удалить"
								onclick={() => {
									deletionConfirmation.resourceType = 'teacher';
									deletionConfirmation.resource = teacher;
									showDeletionConfirmationModal = true;
								}}
							>
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
									class="icon icon-tabler icons-tabler-outline icon-tabler-trash"
									><path stroke="none" d="M0 0h24v24H0z" fill="none" /><path d="M4 7l16 0" /><path
										d="M10 11l0 6"
									/><path d="M14 11l0 6" /><path
										d="M5 7l1 12a2 2 0 0 0 2 2h8a2 2 0 0 0 2 -2l1 -12"
									/><path d="M9 7v-3a1 1 0 0 1 1 -1h4a1 1 0 0 1 1 1v3" /></svg
								>
							</button>
						</div>
					</div>
				</article>
			{/each}
		{:else}
			Преподаватели отсутствуют. Вы можете добавить нового преподавателя,
			<a href="/manage/teacher">нажав сюда</a>.
		{/if}
		<SuperDebug data={teachers}></SuperDebug>
	{:catch error}
		<SuperDebug data={error}></SuperDebug>
	{/await}
{:else}
	Хватит приложение ломать
{/if}

<ModalAlert bind:showModal={showDeletionConfirmationModal}>
	<header>
		Удалить
		{#if deletionConfirmation.resourceType === 'subject'}
			предмет?
		{:else if deletionConfirmation.resourceType === 'teacher'}
			преподавателя?
		{/if}
	</header>
	<p>
		{#if deletionConfirmation.resourceType === 'subject'}
			<b>{deletionConfirmation.resource.fullName}</b>
		{:else if deletionConfirmation.resourceType === 'teacher'}
			<b>{deletionConfirmation.resource.fullname.last}</b>
			{deletionConfirmation.resource.fullname.first}
			{deletionConfirmation.resource.fullname.middle}
		{/if}
	</p>
	{#if deletionMessage}
		<p class="form-message error">
			{deletionMessage}
		</p>
	{/if}
	<details>
		<summary>Информация для отладки</summary>
		<SuperDebug data={deletionConfirmation}></SuperDebug>
	</details>
	<footer>
		<button
			class="secondary"
			disabled={deletionPromise !== undefined}
			aria-busy={deletionPromise !== undefined}
			onclick={() => {
				deletionMessage = '';
				switch (deletionConfirmation.resourceType) {
					case 'group':
						deletionPromise = fetch(baseUrl + '/groups/' + deletionConfirmation.resource.objId, {
							method: 'DELETE',
							headers: {
								token: data.token
							}
						})
							.then(async (res) => {
								if (res.ok) {
									deletionPromise = undefined;
									deletionMessage = '';
									showDeletionConfirmationModal = false;
									window.location.href = '/manage/groups';
								} else {
									const responseData = await res.json();
									if (responseData.error_type && responseData.error_type === 'JWTDecodeError') {
										localStorage.removeItem('token');
										window.location.href = '/login?invalid_token=';
										throw new Error(`Ваш токен устарел. Пожалуйста, войдите в аккаунт снова.`);
									} else {
										throw new Error(`Неизвестная ошибка ${res.status}: ${res.statusText}.`);
									}
								}
							})
							.catch((err) => {
								deletionPromise = undefined;
								deletionMessage = `Не удалось удалить объект типа "${deletionConfirmation.resourceType}": ${err.message}`;
							});
						break;

					case 'subject':
						deletionPromise = fetch(baseUrl + '/subjects/' + deletionConfirmation.resource.objId, {
							method: 'DELETE',
							headers: {
								token: data.token
							}
						})
							.then(async (res) => {
								if (res.ok) {
									deletionPromise = undefined;
									deletionMessage = '';
									showDeletionConfirmationModal = false;
									window.location.href = '/manage/subjects';
								} else {
									const responseData = await res.json();
									if (responseData.error_type && responseData.error_type === 'JWTDecodeError') {
										localStorage.removeItem('token');
										window.location.href = '/login?invalid_token=';
										throw new Error(`Ваш токен устарел. Пожалуйста, войдите в аккаунт снова.`);
									} else {
										throw new Error(`Неизвестная ошибка ${res.status}: ${res.statusText}.`);
									}
								}
							})
							.catch((err) => {
								deletionPromise = undefined;
								deletionMessage = `Не удалось удалить объект типа "${deletionConfirmation.resourceType}": ${err.message}`;
							});
						break;

					case 'teacher':
						deletionPromise = fetch(baseUrl + '/teachers/' + deletionConfirmation.resource.objId, {
							method: 'DELETE',
							headers: {
								token: data.token
							}
						})
							.then(async (response) => {
								if (response.ok) {
									deletionPromise = undefined;
									deletionMessage = '';
									showDeletionConfirmationModal = false;
									window.location.href = '/manage/teachers';
								} else {
									const responseData = await response.json();
									if (responseData.error_type && responseData.error_type === 'JWTDecodeError') {
										localStorage.removeItem('token');
										window.location.href = '/login?invalid_token=';
										throw new Error(`Ваш токен устарел. Пожалуйста, войдите в аккаунт снова.`);
									} else {
										throw new Error(
											`Неизвестная ошибка ${response.status}: ${response.statusText}.`
										);
									}
								}
							})
							.catch((error) => {
								deletionPromise = undefined;
								deletionMessage = `Не удалось удалить объект типа "${deletionConfirmation.resourceType}": ${error.message}`;
							});
						break;

					default:
						break;
				}
			}}
		>
			{#if deletionPromise === undefined}
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
					class="icon icon-tabler icons-tabler-outline icon-tabler-trash"
					><path stroke="none" d="M0 0h24v24H0z" fill="none" /><path d="M4 7l16 0" /><path
						d="M10 11l0 6"
					/><path d="M14 11l0 6" /><path d="M5 7l1 12a2 2 0 0 0 2 2h8a2 2 0 0 0 2 -2l1 -12" /><path
						d="M9 7v-3a1 1 0 0 1 1 -1h4a1 1 0 0 1 1 1v3"
					/></svg
				>
			{/if}
			Удалить
		</button>
		<button
			onclick={() => {
				deletionConfirmation.resource = undefined;
				deletionConfirmation.resourceType = undefined;
				deletionMessage = '';
				showDeletionConfirmationModal = false;
			}}
		>
			Отмена
		</button>
	</footer>
</ModalAlert>

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

	.resource-header > div {
		display: flex;
		justify-content: flex-end;
		gap: 0.5em;

		flex-grow: 1;
	}

	ul {
		margin-bottom: 0;
	}

	footer {
		display: flex;
		justify-content: flex-end;
	}
</style>
