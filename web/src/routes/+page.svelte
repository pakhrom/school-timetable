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
		id: 'ttb-1',
		title: '10Б',
		days: [
			[
				{
					id: 'sub-1',
					title: 'Информатика',
					shortTitle: 'Информ.',
					groups: [
						{ id: 'gro-1', teacher: 'Поздняков А.В.', classroom: '307' },
						{ id: 'gro-2', teacher: 'Безруких О.Ю.', classroom: '203л' }
					]
				},
				{
					id: 'sub-1',
					title: 'Информатика',
					shortTitle: 'Информ.',
					groups: [
						{ id: 'gro-1', teacher: 'Поздняков А.В.', classroom: '307' },
						{ id: 'gro-2', teacher: 'Безруких О.Ю.', classroom: '203л' }
					]
				},
				{
					id: 'sub-3',
					title: 'Литература',
					shortTitle: '',
					groups: [{ id: 'gro-3', teacher: 'Штаркер С.А.', classroom: '106' }]
				},
				{
					id: 'sub-3',
					title: 'Литература',
					shortTitle: '',
					groups: [{ id: 'gro-3', teacher: 'Штаркер С.А.', classroom: '106' }]
				},
				{
					id: 'sub-4',
					title: 'Биология',
					shortTitle: '',
					groups: [{ id: 'gro-4', teacher: 'Заворохина М.В.', classroom: '405' }]
				},
				{
					id: 'sub-5',
					title: 'Физика',
					shortTitle: '',
					groups: [{ id: 'gro-5', teacher: 'Прокофьева Л.В.', classroom: '407' }]
				}
			],
			[
				{
					id: 'sub-9',
					title: 'Математика',
					shortTitle: '',
					groups: [{ id: 'gro-9', teacher: 'Журавлева Е.Ю.', classroom: '105' }]
				},
				{
					id: 'sub-9',
					title: 'Математика',
					shortTitle: '',
					groups: [{ id: 'gro-9', teacher: 'Журавлева Е.Ю.', classroom: '105' }]
				},
				{
					id: 'sub-9',
					title: 'Математика',
					shortTitle: '',
					groups: [{ id: 'gro-9', teacher: 'Журавлева Е.Ю.', classroom: '105' }]
				},
				{
					id: 'sub-5',
					title: 'Физика',
					shortTitle: '',
					groups: [{ id: 'gro-5', teacher: 'Прокофьева Л.В.', classroom: '407' }]
				},
				{
					id: 'sub-5',
					title: 'Физика',
					shortTitle: '',
					groups: [{ id: 'gro-5', teacher: 'Прокофьева Л.В.', classroom: '407' }]
				},
				{
					id: 'sub-5',
					title: 'Физика',
					shortTitle: '',
					groups: [{ id: 'gro-5', teacher: 'Прокофьева Л.В.', classroom: '407' }]
				},
				{
					id: 'sub-15',
					title: 'Обществознание',
					shortTitle: 'Обществ.',
					groups: [{ id: 'gro-14', teacher: 'Халикова З.Г.', classroom: '405' }]
				},
				null,
				{
					id: 'sub-16',
					title: 'Астрономия ВНД',
					shortTitle: 'Астро. ВНД',
					groups: [{ id: 'gro-15', teacher: '', classroom: '212л' }]
				},
				{
					id: 'sub-16',
					title: 'Астрономия ВНД',
					shortTitle: 'Астро. ВНД',
					groups: [{ id: 'gro-15', teacher: '', classroom: '212л' }]
				}
			],
			[
				{
					id: 'sub-5',
					title: 'Физика',
					shortTitle: '',
					groups: [{ id: 'gro-5', teacher: 'Прокофьева Л.В.', classroom: '407' }]
				},
				{
					id: 'sub-5',
					title: 'Физика',
					shortTitle: '',
					groups: [{ id: 'gro-5', teacher: 'Прокофьева Л.В.', classroom: '407' }]
				},
				{
					id: 'sub-9',
					title: 'Математика',
					shortTitle: '',
					groups: [{ id: 'gro-10', teacher: 'Журавлева Е.Ю.', classroom: '302' }]
				},
				{
					id: 'sub-9',
					title: 'Математика',
					shortTitle: '',
					groups: [{ id: 'gro-10', teacher: 'Журавлева Е.Ю.', classroom: '302' }]
				},
				{
					id: 'sub-14',
					title: 'Английский язык',
					shortTitle: 'Англ. яз.',
					groups: [
						{ id: 'gro-16', teacher: 'Артемова И.Ю.', classroom: '404' },
						{ id: 'gro-17', teacher: 'Сергеева О.Е.', classroom: '203' }
					]
				},
				{
					id: 'sub-14',
					title: 'Английский язык',
					shortTitle: 'Англ. яз.',
					groups: [
						{ id: 'gro-16', teacher: 'Артемова И.Ю.', classroom: '404' },
						{ id: 'gro-17', teacher: 'Сергеева О.Е.', classroom: '203' }
					]
				},
				{
					id: 'sub-1',
					title: 'Информатика',
					shortTitle: 'Информ.',
					groups: [
						{ id: 'gro-1', teacher: 'Поздняков А.В.', classroom: '307' },
						{ id: 'gro-2', teacher: 'Безруких О.Ю.', classroom: '203л' }
					]
				},
				{
					id: 'sub-1',
					title: 'Информатика',
					shortTitle: 'Информ.',
					groups: [
						{ id: 'gro-1', teacher: 'Поздняков А.В.', classroom: '307' },
						{ id: 'gro-2', teacher: 'Безруких О.Ю.', classroom: '203л' }
					]
				},
				{
					id: 'sub-17',
					title: 'Черчение',
					shortTitle: '',
					groups: [{ id: 'gro-18', teacher: 'Дмитриенко Г.А.', classroom: '301' }]
				},
				{
					id: 'sub-17',
					title: 'Черчение',
					shortTitle: '',
					groups: [{ id: 'gro-18', teacher: 'Дмитриенко Г.А.', classroom: '301' }]
				}
			],
			[
				{ title: 'ОБЗР', groups: [{ id: 'gro-19', teacher: 'Бруннер А.Н.', classroom: '207л' }] },
				{
					id: 'sub-3',
					title: 'Литература',
					shortTitle: '',
					groups: [{ id: 'gro-3', teacher: 'Штаркер С.А.', classroom: '106' }]
				},
				{
					id: 'sub-18',
					title: 'Русский язык',
					shortTitle: 'Рус. язык',
					groups: [{ id: 'gro-20', teacher: 'Штаркер С.А.', classroom: '106' }]
				},
				{
					id: 'sub-18',
					title: 'Русский язык',
					shortTitle: 'Рус. язык',
					groups: [{ id: 'gro-20', teacher: 'Штаркер С.А.', classroom: '106' }]
				},
				{
					id: 'sub-11',
					title: 'История',
					shortTitle: '',
					groups: [{ id: 'gro-22', teacher: 'Турчанов Е.В.', classroom: '303' }]
				},
				{
					id: 'sub-8',
					title: 'Физическая культура',
					shortTitle: 'Физ. культура',
					groups: [{ id: 'gro-8', teacher: '', classroom: 'СЗ' }]
				},
				{
					id: 'sub-12',
					title: 'Химия',
					shortTitle: '',
					groups: [{ id: 'gro-21', teacher: 'Селезова Е.В.', classroom: '406' }]
				},
				{
					id: 'sub-13',
					title: 'Проектная деятельность',
					shortTitle: 'Проект. деят.',
					groups: [{ id: 'gro-23', teacher: 'Абакумов А.Д.', classroom: '105' }]
				}
			],
			[
				{
					id: 'sub-8',
					title: 'Физическая культура',
					shortTitle: 'Физ. культура',
					groups: [{ id: 'gro-8', teacher: '', classroom: 'СЗ' }]
				},
				{
					id: 'sub-11',
					title: 'История',
					shortTitle: '',
					groups: [{ id: 'gro-22', teacher: 'Турчанов Е.В.', classroom: '303' }]
				},
				{
					id: 'sub-14',
					title: 'Английский язык',
					shortTitle: 'Англ. яз.',
					groups: [
						{ id: 'gro-16', teacher: 'Артемова И.Ю.', classroom: '404' },
						{ id: 'gro-17', teacher: 'Сергеева О.Е.', classroom: '203' }
					]
				},
				{
					id: 'sub-9',
					title: 'Математика',
					shortTitle: '',
					groups: [{ id: 'gro-11', teacher: 'Журавлева Е.Ю.', classroom: '106' }]
				},
				{
					id: 'sub-9',
					title: 'Математика',
					shortTitle: '',
					groups: [{ id: 'gro-11', teacher: 'Журавлева Е.Ю.', classroom: '106' }]
				},
				{
					id: 'sub-9',
					title: 'Математика',
					shortTitle: '',
					groups: [{ id: 'gro-11', teacher: 'Журавлева Е.Ю.', classroom: '106' }]
				},
				{
					id: 'sub-2',
					title: 'Информатика СК',
					shortTitle: 'Информ. СК',
					groups: [
						{ id: 'gro-1', teacher: 'Поздняков А.В.', classroom: '307' },
						{ id: 'gro-2', teacher: 'Безруких О.Ю.', classroom: '203л' }
					]
				},
				{
					id: 'sub-2',
					title: 'Информатика СК',
					shortTitle: 'Информ. СК',
					groups: [
						{ id: 'gro-1', teacher: 'Поздняков А.В.', classroom: '307' },
						{ id: 'gro-2', teacher: 'Безруких О.Ю.', classroom: '203л' }
					]
				},
				{
					id: 'sub-10',
					title: 'Математика ВНД',
					shortTitle: '',
					groups: [{ id: 'gro-12', teacher: 'Журавлева Е.Ю.', classroom: '105' }]
				},
				{
					id: 'sub-10',
					title: 'Математика ВНД',
					shortTitle: '',
					groups: [{ id: 'gro-12', teacher: 'Журавлева Е.Ю.', classroom: '105' }]
				}
			],
			[
				{
					id: 'sub-6',
					title: 'Билет в будущее',
					shortTitle: 'Билет в буд.',
					groups: [{ id: 'gro-7', teacher: 'Прокофьева Л.В.', classroom: '407' }]
				},
				{
					id: 'sub-7',
					title: 'Физика ВНД',
					shortTitle: '',
					groups: [{ id: 'gro-6', teacher: 'Прокофьева Л.В.', classroom: '407' }]
				},
				{
					id: 'sub-7',
					title: 'Физика ВНД',
					shortTitle: '',
					groups: [{ id: 'gro-6', teacher: 'Прокофьева Л.В.', classroom: '407' }]
				},
				{
					id: 'sub-8',
					title: 'Физическая культура',
					shortTitle: 'Физ. культура',
					groups: [{ id: 'gro-8', teacher: '', classroom: 'СЗ' }]
				},
				{
					title: 'География',
					groups: [{ id: 'gro-13', teacher: 'Лемешкова В.В.', classroom: '403' }]
				},
				{
					id: 'sub-15',
					title: 'Обществознание',
					shortTitle: 'Обществ.',
					groups: [{ id: 'gro-14', teacher: 'Халикова З.Г.', classroom: '405' }]
				}
			]
		],
		lastUpdated: new Date(2024, 11, 17)
	};
	let subjectsWithMultipleGroups: any[] = [];
	let subjectsWithMultipleGroupsIds: string[] = [];

	timetable.days.forEach((day) => {
		day.forEach((lesson) => {
			if (
				lesson &&
				lesson.id &&
				!subjectsWithMultipleGroupsIds.includes(lesson.id) &&
				lesson.groups.length > 1
			) {
				if (lesson.id) subjectsWithMultipleGroupsIds.push(lesson.id);
				subjectsWithMultipleGroups.push(lesson);
			}
		});
	});

	const replacementsReturned = [
		{
			id: 'rep-1',
			date: '2025-04-15T11:17:55+07:00',
			groups: [
				{
					replaced: 'gro-5',
					replacement: ''
				}
			]
		},
		{
			id: 'rep-2',
			date: '2025-04-14T11:17:55+07:00',
			groups: [
				{
					replaced: 'gro-2',
					replacement: 'gro-1'
				}
			]
		}
	];
	let replacements = [];
	replacementsReturned.forEach((replacementReturned) => {
		let replacementDate = new Date(replacementReturned.date);
		replacements.push({
			dayIndex: replacementDate.getDay() - 1
		});
	});

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
	const days: Array<HTMLDivElement | undefined> = $state([
		undefined,
		undefined,
		undefined,
		undefined,
		undefined,
		undefined
	]);

	let customizationDetailsElement: HTMLDetailsElement;
	let showCustomizationDetails = $state(false);
	let customizationChanged = $state(false);

	let showLessonInformationModal = $state(false);
	let lessonInformation: any = $state({});
	function openLessonInfo(dayIndex: number, lessonIndex: number) {
		if (timetable.days[dayIndex][lessonIndex]) {
			lessonInformation = timetable.days[dayIndex][lessonIndex];
			showLessonInformationModal = true;
		} else
			console.error('User tried opening the lesson information modal with a non-existent lesson');
	}

	// PERSONALIZATION

	// SETTINGS
	const defaultSettingsList = $state([
		{
			type: 'boolean',
			id: 'full-subject-names',
			title: 'Всегда показывать полные названия предметов',
			defaultValue: false
		}
	]);

	let settings: { id: string; value: boolean }[] = $state([]);
	let settingsLoaded = localStorage.getItem('settings');
	if (settingsLoaded) {
		settings = JSON.parse(settingsLoaded);
		defaultSettingsList.forEach((defaultSetting, defaultSettingIndex) => {
			if (
				defaultSetting.id !== settings[defaultSettingIndex].id ||
				typeof defaultSetting.defaultValue !== typeof settings[defaultSettingIndex].value
			) {
				resetSettings();
				console.log(
					'Настройки были сброшены до значений по умолчанию по причине обновления списка настроек или повреждения сохраненных настроек'
				);
			}
		});
	} else {
		resetSettings();
	}

	function resetSettings() {
		settings = [];
		defaultSettingsList.forEach((setting) => {
			settings.push({ id: setting.id, value: setting.defaultValue });
		});
		saveSettings();
	}
	function saveSettings() {
		localStorage.setItem('settings', JSON.stringify(settings));
	}

	let settingsDetailsElement: HTMLDetailsElement;

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
	<a href="https://shk24.ru">
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
			class="icon icon-tabler icons-tabler-outline icon-tabler-school"
		>
			<path stroke="none" d="M0 0h24v24H0z" fill="none" />
			<path d="M22 9l-10 -4l-10 4l10 4l10 -4v6" />
			<path d="M6 10.6v5.4a6 3 0 0 0 12 0v-5.4" />
		</svg>
		Электронный дневник
	</a>
	<h1 id="title">Расписание уроков</h1>
	<!-- <img src="новодворская-кирпич.gif" alt="a" style="width: 100%" /> -->
	<article class="warning">
		<svg
			xmlns="http://www.w3.org/2000/svg"
			width="24"
			height="24"
			viewBox="0 0 24 24"
			fill="currentColor"
			class="icon icon-tabler icons-tabler-filled icon-tabler-alert-triangle"
		>
			<path stroke="none" d="M0 0h24v24H0z" fill="none" />
			<path
				d="M12 1.67c.955 0 1.845 .467 2.39 1.247l.105 .16l8.114 13.548a2.914 2.914 0 0 1 -2.307 4.363l-.195 .008h-16.225a2.914 2.914 0 0 1 -2.582 -4.2l.099 -.185l8.11 -13.538a2.914 2.914 0 0 1 2.491 -1.403zm.01 13.33l-.127 .007a1 1 0 0 0 0 1.986l.117 .007l.127 -.007a1 1 0 0 0 0 -1.986l-.117 -.007zm-.01 -7a1 1 0 0 0 -.993 .883l-.007 .117v4l.007 .117a1 1 0 0 0 1.986 0l.007 -.117v-4l-.007 -.117a1 1 0 0 0 -.993 -.883z"
			/>
		</svg>
		<div>
			Для правильного отображения местоположения уроков выберите свои группы уроков в разделе <a
				href="#customization"
				class="inline-link">«Расписание»</a
			>.
		</div>
	</article>
	<div class="grid">
		{#each { length: 6 }, dayIndex}
			<div class="day-container" bind:this={days[dayIndex]}>
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
				<hr class={dayPrioritized - 1 === dayIndex ? 'prioritized-line' : ''} />
				<article
					class={['day', dayPrioritized - 1 === dayIndex ? 'prioritized' : null]}
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
								<li class="lesson-container">
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
												openLessonInfo(dayIndex, lessonIndex);
											}}
										>
											{lessonIndex + 1}.
											<span class={false ? 'replacement' : ''}>
												{#if settings[0].value === false && lesson.shortTitle}
													{lesson.shortTitle}
												{:else}
													{lesson.title}
												{/if}
												<sup class="classroom">
													<b>
														{lesson.groups[0].classroom}{#if lesson.groups.length > 1}/...{/if}
														<!-- {#each lesson.groups as group, groupIndex}
															{group.classroom}{#if groupIndex !== lesson.groups.length - 1}/{/if}
														{/each} -->
													</b>
												</sup>
											</span>
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
				customizationDetailsElement.scrollIntoView({
					behavior: 'smooth'
				});
			}
		}}
	>
		<summary class={{ highlight: customizationChanged }} id="customization">
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
			<h5>Класс</h5>
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
		<h5>Группы предметов</h5>
		{#each subjectsWithMultipleGroups as subject}
			<article>
				<h6>{subject.title}</h6>
				<fieldset>
					<legend>Выберите свою группу</legend>
					{#each subject.groups as group}
						<label>
							<input
								type="radio"
								name={subject.id}
								onchange={() => {
									customizationChanged = true;
								}}
							/>
							{group.teacher} ➔ <b>{group.classroom}</b>
						</label>
					{/each}
				</fieldset>
			</article>
		{/each}

		{#if customizationChanged}
			<button
				type="button"
				class="wide"
				onclick={() => {
					customizationDetailsElement.open = false;
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
					class="icon icon-tabler icons-tabler-outline icon-tabler-device-floppy"
				>
					<path stroke="none" d="M0 0h24v24H0z" fill="none" />
					<path d="M6 4h10l4 4v10a2 2 0 0 1 -2 2h-12a2 2 0 0 1 -2 -2v-12a2 2 0 0 1 2 -2" />
					<path d="M12 14m-2 0a2 2 0 1 0 4 0a2 2 0 1 0 -4 0" />
					<path d="M14 4l0 4l-6 0l0 -4" />
				</svg>
				Сохранить изменения
			</button>
		{/if}
	</details>

	<details
		bind:this={settingsDetailsElement}
		ontoggle={() => {
			if (settingsDetailsElement.open)
				settingsDetailsElement.scrollIntoView({
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
		{#each defaultSettingsList as settingInfo, settingIndex}
			<label>
				{#if settingInfo.type === 'boolean'}
					<input
						type="checkbox"
						name={settingInfo.id}
						id={settingInfo.id}
						onchange={() => {
							saveSettings();
						}}
						bind:checked={settings[settingIndex].value}
					/>
					{settingInfo.title}
				{/if}
			</label>
		{/each}
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
	<header>{lessonInformation.title}</header>
	Группы:
	<ul>
		{#each lessonInformation.groups as group}
			<li>
				<div>
					{group.teacher} ➔ <b>{group.classroom}</b>
				</div>
			</li>
		{/each}
	</ul>
</ModalAlert>

<style>
	a:not(.inline-link) {
		display: inline-flex;
		align-items: center;
		gap: 0.25em;

		text-decoration: none;
	}

	.warning {
		display: flex;
		gap: 1em;

		padding: 0.5em 1em;
		margin-bottom: 1em;

		background-color: var(--pico-mark-background-color);
		border-radius: 0.25em;
	}

	.warning > svg {
		min-width: 1.5em;
		margin: 0.25em 0;
	}

	h4 {
		margin: 0 0.25em;
		text-align: center;
	}

	.wide {
		width: 100%;
		justify-content: center;
	}

	.icon-button {
		display: inline-flex;
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

	article {
		margin-bottom: 0.5em;
	}

	.day:not([aria-busy='true']) {
		padding: 1em 0.5em 0.25em 0;
		margin-bottom: 0;

		border: 2px solid rgba(255, 255, 255, 0);
	}

	.day.prioritized {
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

	.lesson-container {
		display: flex;
		align-items: flex-start;
		gap: 1em;

		padding-right: 0.25em;
	}

	.day-container {
		padding: 1em 0.25em 0;
	}

	.day-marker {
		color: var(--pico-secondary);
	}

	.prioritized-line {
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

	.classroom {
		white-space-collapse: discard;
	}

	.replacement {
		padding: 0.15em 0.25em;

		border-radius: 0.25em;

		/* Taken from pico css */
		background-color: var(--pico-mark-background-color);
		color: var(--pico-mark-color);
		vertical-align: baseline;
	}

	h5 {
		margin-bottom: 0.5em;
	}

	select {
		margin-top: 0;
	}

	ul {
		margin-bottom: 0.25em;
	}

	fieldset {
		margin-bottom: 0;
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
