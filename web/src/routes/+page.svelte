<script lang="ts">
	import ModalAlert from '$lib/components/modal-alert.svelte';
	import { slide } from 'svelte/transition';

	const classes = [
		'8А',
		'8Б',
		'8В',
		'8Г',
		'9А',
		'9Б',
		'9В',
		'9Г',
		'10А',
		'10Б',
		'10В',
		'10Г',
		'11А',
		'11Б',
		'11В',
		'11Г'
	];

	const timetable = {
		class: '10Б',
		days: [
			[
				{
					title: 'Информатика',
					groups: [
						{ teacher: 'Поздняков А.В.', classroom: '307' },
						{ teacher: 'Безруких О.Ю.', classroom: '203л' }
					]
				},
				{
					title: 'Информатика',
					groups: [
						{ teacher: 'Поздняков А.В.', classroom: '307' },
						{ teacher: 'Безруких О.Ю.', classroom: '203л' }
					]
				},
				{
					title: 'Литература',
					groups: [{ teacher: 'Штаркер С.А.', classroom: '106' }]
				},
				{
					title: 'Литература',
					groups: [{ teacher: 'Штаркер С.А.', classroom: '106' }]
				},
				{
					title: 'Биология',
					groups: [{ teacher: 'Заворохина М.В.', classroom: '405' }]
				},
				{
					title: 'Физика',
					groups: [{ teacher: 'Прокофьева Л.В.', classroom: '407' }]
				}
			],
			[
				{
					title: 'Математика',
					groups: [{ teacher: 'Журавлева Е.Ю.', classroom: '105' }]
				},
				{
					title: 'Математика',
					groups: [{ teacher: 'Журавлева Е.Ю.', classroom: '105' }]
				},
				{
					title: 'Математика',
					groups: [{ teacher: 'Журавлева Е.Ю.', classroom: '105' }]
				},
				{
					title: 'Физика',
					groups: [{ teacher: 'Прокофьева Л.В.', classroom: '407' }]
				},
				{
					title: 'Физика',
					groups: [{ teacher: 'Прокофьева Л.В.', classroom: '407' }]
				},
				{
					title: 'Физика',
					groups: [{ teacher: 'Прокофьева Л.В.', classroom: '407' }]
				},
				{
					title: 'Обществознание',
					groups: [{ teacher: 'Халикова З.Г.', classroom: '405' }]
				},
				null,
				{
					title: 'Астрономия ВНД',
					groups: [{ teacher: '', classroom: '212л' }]
				},
				{
					title: 'Астрономия ВНД',
					groups: [{ teacher: '', classroom: '212л' }]
				}
			],
			[
				{
					title: 'Физика',
					groups: [{ teacher: 'Прокофьева Л.В.', classroom: '407' }]
				},
				{
					title: 'Физика',
					groups: [{ teacher: 'Прокофьева Л.В.', classroom: '407' }]
				},
				{
					title: 'Математика',
					groups: [{ teacher: 'Журавлева Е.Ю.', classroom: '105' }]
				},
				{
					title: 'Математика',
					groups: [{ teacher: 'Журавлева Е.Ю.', classroom: '105' }]
				},
				{
					title: 'Английский язык',
					groups: [
						{ teacher: 'Артемова И.Ю.', classroom: '404' },
						{ teacher: 'Сергеева О.Е.', classroom: '203' }
					]
				},
				{
					title: 'Английский язык',
					groups: [
						{ teacher: 'Артемова И.Ю.', classroom: '404' },
						{ teacher: 'Сергеева О.Е.', classroom: '203' }
					]
				},
				{
					title: 'Информатика',
					groups: [
						{ teacher: 'Поздняков А.В.', classroom: '307' },
						{ teacher: 'Безруких О.Ю.', classroom: '203л' }
					]
				},
				{
					title: 'Информатика',
					groups: [
						{ teacher: 'Поздняков А.В.', classroom: '307' },
						{ teacher: 'Безруких О.Ю.', classroom: '203л' }
					]
				},
				{
					title: 'Черчение',
					groups: [{ teacher: 'Дмитриенко Г.А.', classroom: '301' }]
				},
				{
					title: 'Черчение',
					groups: [{ teacher: 'Дмитриенко Г.А.', classroom: '301' }]
				}
			],
			[
				{ title: 'ОБЗР', groups: [{ teacher: 'Бруннер А.Н.', classroom: '207л' }] },
				{
					title: 'Литература',
					groups: [{ teacher: 'Штаркер С.А.', classroom: '106' }]
				},
				{
					title: 'Русский язык',
					groups: [{ teacher: 'Штаркер С.А.', classroom: '106' }]
				},
				{
					title: 'Русский язык',
					groups: [{ teacher: 'Штаркер С.А.', classroom: '106' }]
				},
				{
					title: 'История',
					groups: [{ teacher: 'Турчанов Е.В.', classroom: '303' }]
				},
				{
					title: 'Физическая культура',
					groups: [{ teacher: '', classroom: 'СЗ' }]
				},
				{
					title: 'Химия',
					groups: [{ teacher: 'Селезова Е.В.', classroom: '406' }]
				},
				{
					title: 'Проектная деятельность',
					groups: [{ teacher: 'Абакумов А.Д.', classroom: '105' }]
				}
			],
			[
				{
					title: 'Физическая культура',
					groups: [{ teacher: '', classroom: 'СЗ' }]
				},
				{
					title: 'История',
					groups: [{ teacher: 'Турчанов Е.В.', classroom: '303' }]
				},
				{
					title: 'Английский язык',
					groups: [
						{ teacher: 'Артемова И.Ю.', classroom: '404' },
						{ teacher: 'Сергеева О.Е.', classroom: '203' }
					]
				},
				{
					title: 'Математика',
					groups: [{ teacher: 'Журавлева Е.Ю.', classroom: '105' }]
				},
				{
					title: 'Математика',
					groups: [{ teacher: 'Журавлева Е.Ю.', classroom: '105' }]
				},
				{
					title: 'Математика',
					groups: [{ teacher: 'Журавлева Е.Ю.', classroom: '105' }]
				},
				{
					title: 'Информатика СК',
					groups: [
						{ teacher: 'Поздняков А.В.', classroom: '307' },
						{ teacher: 'Безруких О.Ю.', classroom: '203л' }
					]
				},
				{
					title: 'Информатика СК',
					groups: [
						{ teacher: 'Поздняков А.В.', classroom: '307' },
						{ teacher: 'Безруких О.Ю.', classroom: '203л' }
					]
				},
				{
					title: 'Математика ВНД',
					groups: [{ teacher: 'Журавлева Е.Ю.', classroom: '105' }]
				},
				{
					title: 'Математика ВНД',
					groups: [{ teacher: 'Журавлева Е.Ю.', classroom: '105' }]
				}
			],
			[
				{
					title: 'Билет в будущее',
					groups: [{ teacher: 'Прокофьева Л.В.', classroom: '407' }]
				},
				{
					title: 'Физика ВНД',
					groups: [{ teacher: 'Прокофьева Л.В.', classroom: '407' }]
				},
				{
					title: 'Физика ВНД',
					groups: [{ teacher: 'Прокофьева Л.В.', classroom: '407' }]
				},
				{
					title: 'Физическая культура',
					groups: [{ teacher: '', classroom: 'СЗ' }]
				},
				{
					title: 'География',
					groups: [{ teacher: 'Лемешкова В.В.', classroom: '403' }]
				},
				{
					title: 'Обществознание',
					groups: [{ teacher: 'Халикова З.Г.', classroom: '405' }]
				}
			]
		],
		lastUpdated: new Date(2024, 11, 17)
	};

	const DAYS_OF_THE_WEEK = ['', 'Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота'];
	const LESSON_TIMING = [
		[
			[8, 30],
			[9, 10]
		],
		[
			[9, 30],
			[10, 10]
		],
		[
			[10, 20],
			[11, 0]
		],
		[
			[11, 10],
			[11, 50]
		],
		[
			[12, 15],
			[12, 55]
		],
		[
			[13, 20],
			[14, 0]
		],
		[
			[14, 10],
			[14, 50]
		],
		[
			[15, 5],
			[15, 45]
		],
		[
			[16, 0],
			[16, 40]
		],
		[
			[16, 50],
			[17, 30]
		]
	];

	const now = new Date();
	const dayPrioritized =
		now.getHours() >= 17 ? (now.getDay() > 5 ? 1 : now.getDay() + 1) : now.getDay(); // Sunday is 0, Monday is 1
	const days: Array<HTMLDivElement | undefined> = [
		undefined,
		undefined,
		undefined,
		undefined,
		undefined,
		undefined
	];

	let customizationDetailsElement: HTMLDetailsElement;
	let showCustomizationDetails = $state(false);
	let customizationChanged = $state(false);

	let lessonInformationTitle = $state('');
	let showLessonInformationModal = $state(false);
	function openLessonInfo(lessonTitle: string) {
		lessonInformationTitle = lessonTitle;
		showLessonInformationModal = true;
	}

	// DEBUG
	let loadingToday = $state(true);
	let loadingTimetable = $state(true);

	function loadWebsite() {
		customizationChanged = false;
		loadingToday = true;
		loadingTimetable = true;

		scrollTo(0, 0);
		setTimeout(() => {
			loadingToday = false;
		}, 300);
		setTimeout(() => {
			loadingTimetable = false;
		}, 1000);
	}

	loadWebsite();
</script>

<svelte:head>
	<title>Расписание уроков</title>
</svelte:head>

<main aria-labelledby="title">
	<h1 id="title">Расписание уроков</h1>
	<img src="новодворская-кирпич.gif" alt="a" style="width: 100%" />
	<div class="grid">
		{#each { length: 6 }, dayIndex}
			<div class="day" bind:this={days[dayIndex]}>
				<h4>
					{#if now.getDay() - 1 === dayIndex}
						<span class="day-marker">Сегодня •</span>
					{:else if now.getDay() === dayIndex}
						<span class="day-marker">Завтра •</span>
					{:else if now.getDay() === 6 && dayIndex === 0}
						<span class="day-marker">Послезавтра •</span>
					{/if}
					{DAYS_OF_THE_WEEK[dayIndex + 1]}
				</h4>
				<hr class={dayPrioritized - 1 === dayIndex ? 'prioritized-day-line' : ''} />
				<article
					class={dayPrioritized - 1 === dayIndex ? 'prioritized-day' : null}
					aria-busy={loadingTimetable && !(dayPrioritized - 1 === dayIndex && !loadingToday)}
				>
					{#if !loadingTimetable || (dayPrioritized - 1 === dayIndex && !loadingToday)}
						<ol
							transition:slide={{ duration: 200 }}
							onintroend={() => {
								if (/* (!loadingToday && loadingTimetable) ||  */ !loadingTimetable) {
									days[dayPrioritized - 1]?.scrollIntoView({ behavior: 'smooth' });
								}
							}}
						>
							{#each timetable.days[dayIndex] as lesson, lessonIndex}
								<li>
									<div class="timing-container">
										<span class="timing">
											{LESSON_TIMING[lessonIndex][0][0]}:{LESSON_TIMING[lessonIndex][0][1] < 10
												? LESSON_TIMING[lessonIndex][0][1].toString() + '0'
												: LESSON_TIMING[lessonIndex][0][1]} - {LESSON_TIMING[
												lessonIndex
											][1][0]}:{LESSON_TIMING[lessonIndex][1][1] < 10
												? LESSON_TIMING[lessonIndex][1][1].toString() + '0'
												: LESSON_TIMING[lessonIndex][1][1]}
										</span>
									</div>

									{#if lesson}
										<button
											class="lesson"
											onclick={() => {
												openLessonInfo(lesson.title);
											}}
										>
											{lessonIndex + 1}.
											{#if Math.floor(Math.random() * 10) === 1}
												<mark> {lesson.title} <sup><b>{lesson.groups[0].classroom}</b></sup></mark>
											{:else}
												{lesson.title} <sup><b>{lesson.groups[0].classroom}</b></sup>
											{/if}
										</button>
									{:else}
										<button class="lesson" disabled>
											{lessonIndex + 1}. Пусто
										</button>
									{/if}
								</li>
							{/each}
						</ol>
					{/if}
				</article>
			</div>
		{/each}
	</div>

	<details
		bind:this={customizationDetailsElement}
		bind:open={showCustomizationDetails}
		ontoggle={() => {
			if (!customizationDetailsElement.open && customizationChanged) {
				loadWebsite();
			} else {
				document.documentElement.scrollTo({
					left: 0,
					top: document.documentElement.scrollHeight - document.documentElement.clientHeight,
					behavior: 'smooth'
				});
			}
		}}
	>
		<summary class={{ highlight: customizationChanged }}>
			{#if customizationChanged}
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
				>
					<path stroke="none" d="M0 0h24v24H0z" fill="none" />
					<path d="M6 4h10l4 4v10a2 2 0 0 1 -2 2h-12a2 2 0 0 1 -2 -2v-12a2 2 0 0 1 2 -2" />
					<path d="M12 14m-2 0a2 2 0 1 0 4 0a2 2 0 1 0 -4 0" />
					<path d="M14 4l0 4l-6 0l0 -4" />
				</svg>
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
					class="icon icon-tabler icons-tabler-outline icon-tabler-filter-edit"
				>
					<path stroke="none" d="M0 0h24v24H0z" fill="none" />
					<path
						d="M10.97 20.344l-1.97 .656v-8.5l-4.48 -4.928a2 2 0 0 1 -.52 -1.345v-2.227h16v2.172a2 2 0 0 1 -.586 1.414l-4.414 4.414v1.5"
					/>
					<path d="M18.42 15.61a2.1 2.1 0 0 1 2.97 2.97l-3.39 3.42h-3v-3l3.42 -3.39z" />
				</svg>
				Расписание
			{/if}
		</summary>
		<label for="class">
			Класс
			<select
				name="class"
				id="class"
				onchange={() => {
					customizationChanged = true;
				}}
			>
				{#each classes as class_}
					<option value={class_}>{class_}</option>
				{/each}
			</select>
		</label>
	</details>
	<details
		ontoggle={() => {
			document.documentElement.scrollTo({
				left: 0,
				top: document.documentElement.scrollHeight - document.documentElement.clientHeight,
				behavior: 'smooth'
			});
		}}
	>
		<summary>
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
				class="icon icon-tabler icons-tabler-outline icon-tabler-tools"
			>
				<path stroke="none" d="M0 0h24v24H0z" fill="none" />
				<path d="M3 21h4l13 -13a1.5 1.5 0 0 0 -4 -4l-13 13v4" />
				<path d="M14.5 5.5l4 4" />
				<path d="M12 8l-5 -5l-4 4l5 5" />
				<path d="M7 8l-1.5 1.5" />
				<path d="M16 12l5 5l-4 4l-5 -5" />
				<path d="M16 17l-1.5 1.5" />
			</svg>
			Настройки
		</summary>
		А
	</details>
</main>

<footer>
	<button class="icon-button" aria-label="Обновить расписание" onclick={loadWebsite}>
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
			class="icon icon-tabler icons-tabler-outline icon-tabler-reload"
		>
			<path stroke="none" d="M0 0h24v24H0z" fill="none" />
			<path d="M19.933 13.041a8 8 0 1 1 -9.925 -8.788c3.899 -1 7.935 1.007 9.425 4.747" />
			<path d="M20 4v5h-5" />
		</svg>
	</button>
	<a href="/print" aria-label="Распечатать расписание">
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
			class="icon icon-tabler icons-tabler-outline icon-tabler-printer"
		>
			<path stroke="none" d="M0 0h24v24H0z" fill="none" />
			<path d="M17 17h2a2 2 0 0 0 2 -2v-4a2 2 0 0 0 -2 -2h-14a2 2 0 0 0 -2 2v4a2 2 0 0 0 2 2h2" />
			<path d="M17 9v-4a2 2 0 0 0 -2 -2h-6a2 2 0 0 0 -2 2v4" />
			<path d="M7 13m0 2a2 2 0 0 1 2 -2h6a2 2 0 0 1 2 2v4a2 2 0 0 1 -2 2h-6a2 2 0 0 1 -2 -2z" />
		</svg>
	</a>
	<a href="/login" aria-label="Войти в аккаунт администратора">
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
	</a>
</footer>

<ModalAlert bind:showModal={showLessonInformationModal}>
	<header>{lessonInformationTitle}</header>
	Информация о уроке
</ModalAlert>

<style>
	#title {
		display: inline-flex;
		justify-content: center;
		align-items: baseline;
		gap: 0.5em;

		width: 100%;
	}

	h1,
	h4 {
		text-align: center;
	}

	h4 {
		margin: 0 0.25em;
	}

	.icon-button {
		padding: 0;
		margin: 0;

		color: var(--pico-primary);
		background-color: rgba(255, 255, 255, 0);
		border: none;
	}

	.grid {
		display: grid;
		grid-template-columns: repeat(auto-fit, minmax(20em, 1fr));
		gap: 0;

		margin-bottom: 2em;
	}

	article:not([aria-busy='true']) {
		padding: 1em 0.5em 0.25em 0;
		margin-bottom: 0;

		border: 2px solid rgba(255, 255, 255, 0);
	}

	article.prioritized-day {
		border-color: var(--pico-border-color);
	}

	hr {
		margin: 0.25em 0.5em 0.5em;
		border-top-width: 2px;
		border-bottom: 2px solid rgba(255, 255, 255, 0);
	}

	ol {
		padding-left: 0.5em;
	}

	li {
		display: flex;
		align-items: flex-start;
		gap: 1em;

		padding-right: 0.25em;
	}

	.day {
		padding: 1em 0.25em 0;
	}

	.day-marker {
		color: var(--pico-secondary);
	}

	.prioritized-day-line {
		border-top: 2px solid var(--pico-color);
		border-top: 2px solid var(--pico-color);
	}

	.timing-container {
		min-width: 6.2em;
		width: 6.2em;
		text-align: end;
	}

	.timing {
		padding: 0.05em 0.25em;
		border: 1px solid var(--pico-secondary);
		border-radius: 0.25em;

		font-size: 0.9em;
		user-select: none;
	}

	.lesson {
		padding: 0.05em 0 0 0.25em;

		color: var(--pico-contrast);
		background-color: rgba(255, 255, 255, 0);
		border: none;

		text-align: start;
		text-wrap-mode: nowrap;
		overflow-x: auto;
		overflow-y: hidden;
	}

	mark {
		padding: 0.15em 0.25em;

		border-radius: 0.25em;
	}

	button:not(.lesson):not(.icon-button) {
		display: flex;
		justify-content: center;
		align-items: center;
		gap: 0.25em;
	}

	summary {
		vertical-align: center;
	}

	footer {
		display: flex;
		justify-content: flex-end;
		align-items: center;
		gap: 0.5em;

		padding-top: 0.5em;

		border-top: 1px solid var(--pico-muted-border-color);
	}
</style>
