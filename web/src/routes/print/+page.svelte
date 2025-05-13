<script lang="ts">
	import { UAParser } from 'ua-parser-js';

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

	const userAgent = navigator.userAgent;
	const { browser } = UAParser(userAgent);

	let isGuideOpen: boolean | undefined = $state();
	let isGuideOpenJSON = localStorage.getItem('is-printing-guide-open');
	if (isGuideOpenJSON) {
		isGuideOpen = JSON.parse(isGuideOpenJSON).open;
	} else {
		isGuideOpen = true;
	}

	let classToAdd1: string = $state('');
	let classToAdd2: string = $state('');

	let isBeforePrint = $state(false);

	$effect(() => {
		localStorage.setItem('is-printing-guide-open', JSON.stringify({ open: isGuideOpen }));
	});
</script>

<svelte:window
	onbeforeprint={() => {
		isBeforePrint = true;
	}}
	onafterprint={() => {
		isBeforePrint = false;
		classToAdd1 = '';
		classToAdd2 = '';
	}}
/>

<svelte:head>
	{#if isBeforePrint}
		<title>
			Расписание {timetable.class} и {timetable.class} классов
		</title>
	{:else}
		<title>Печать расписания</title>
	{/if}
</svelte:head>

<div id="no-print">
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
	<h1>Печать расписания</h1>
	<details bind:open={isGuideOpen}>
		<summary>
			<mark><i>Инструкция по печати</i></mark>
		</summary>
		<article>
			<details
				open={browser.name === 'Chrome' || browser.name === 'Yandex' || browser.name === 'Edge'}
			>
				<summary>
					<i>
						Инструкция для браузеров, основанных на <b>Chromium</b> (Chrome, Microsoft Edge, Яндекс Браузер
						и другие)
					</i>
				</summary>
				<ol>
					<li>
						Выберите классы, расписания которых вы хотите распечатать. Можно напечатать от 1 до 2
						расписаний за раз.
					</li>
					<li>
						Нажмите синую кнопку внизу «Печать». Если кнопка недоступна, проверьте, что пункт «Класс
						для печати №1» не пустой.
					</li>
					<li>
						После нажатия кнопки у вас должно появиться на экране окно с параметрами печати. Для
						правильного вывода содержимого в документ вам необходимо настроить здесь пару пунктов:
						<ul>
							<li>
								Ориентация: <b>Горизонтально</b>. <br />
							</li>
						</ul>

						Следующие пункты в меню
						<b>«Дополнительные настройки»</b>:
						<ul>
							<li>
								Размер бумаги: <b>А4</b>. <br />
							</li>
							<li>
								Число страниц на бумаге: <b>1</b>.
							</li>
							<li>
								Поля: <b>Нет</b>.
							</li>
							<li>
								Масштаб: <b>Персонализированные</b> и в появившемся ниже поле <b>100</b>.
							</li>
							<li>
								Параметры: Оставьте галочку на пункте
								<b>«Фон»</b> или
								<b>«Фоновые цвета и изображения»</b>, если вы используете Яндекс Браузер.
							</li>
						</ul>
					</li>
				</ol>
			</details>
			<details style="margin-bottom: 0;" open={browser.name === 'Firefox'}>
				<summary>
					<i>Инструкция для браузеров, основанных на <b>Firefox</b></i>
				</summary>
				<ol>
					<li>
						Выберите классы, расписания которых вы хотите распечатать. Можно напечатать от 1 до 2
						расписаний за раз.
					</li>
					<li>
						Нажмите синую кнопку внизу «Печать». Если кнопка недоступна, проверьте, что пункт «Класс
						для печати №1» не пустой.
					</li>
					<li>
						После нажатия кнопки у вас должно появиться на экране окно с параметрами печати. Для
						правильного вывода содержимого в документ вам необходимо настроить здесь пару пунктов:
						<ul>
							<li>
								Ориентация: <b>Альбомная</b>.
							</li>
						</ul>
						Следующие пункты в меню
						<b>«Все настройки»</b>:

						<ul>
							<li>
								Размер бумаги: <b>А4</b>. <br />
							</li>
							<li>
								Масштаб: <b>Масштаб</b> и в поле справа <b>100</b>.
							</li>
							<li>
								Страниц на одном листе: <b>1</b>.
							</li>
							<li>
								Поля: <b>Нет</b>.
							</li>
							<li>
								Формат: <b>Оригинал</b>.
							</li>
							<li>
								Настройки: Уберите галочку на пункте
								<b>«Печатать колонтитулы»</b> и оставьте галочку на пункте
								<b>«Печатать фон»</b>.
							</li>
						</ul>
					</li>
				</ol>
			</details>
			Данную настройку необходимо сделать всего один раз, в будущем вам не придётся заново настраивать
			печать.
		</article>
	</details>

	<div class="grid">
		<label for="class-1">
			Класс для печати №1
			<!-- svelte-ignore a11y_no_redundant_roles -->
			<select name="class-1" id="class-1" bind:value={classToAdd1}>
				{#each classes as class_}
					<option value={class_}>{class_}</option>
				{/each}
			</select>
		</label>
		<label for="class-2">
			Класс для печати №2
			<!-- svelte-ignore a11y_no_redundant_roles -->
			<select name="class-2" id="class-2" bind:value={classToAdd2} disabled={!classToAdd1}>
				{#each classes as class_}
					<option value={class_}>{class_}</option>
				{/each}
			</select>
		</label>
	</div>
	{#if window.screen.width / window.screen.height <= 1}
		<div class="warning">
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
			Печать расписания не поддерживается на мобильных устройствах. Будьте готовы к неправильному отображению
			элементов в документе.
		</div>
	{/if}
	<button
		type="button"
		class="wide"
		onclick={() => {
			window.print();
		}}
		disabled={!classToAdd1}
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
			class="icon icon-tabler icons-tabler-outline icon-tabler-printer"
		>
			<path stroke="none" d="M0 0h24v24H0z" fill="none" />
			<path d="M17 17h2a2 2 0 0 0 2 -2v-4a2 2 0 0 0 -2 -2h-14a2 2 0 0 0 -2 2v4a2 2 0 0 0 2 2h2" />
			<path d="M17 9v-4a2 2 0 0 0 -2 -2h-6a2 2 0 0 0 -2 2v4" />
			<path d="M7 13m0 2a2 2 0 0 1 2 -2h6a2 2 0 0 1 2 2v4a2 2 0 0 1 -2 2h-6a2 2 0 0 1 -2 -2z" />
		</svg>
		Печать
	</button>
</div>

<div id="print">
	<h2 id="title">Расписание {timetable.class} класса</h2>
	<table class="striped">
		<thead>
			<tr>
				<th scope="col">№</th>
				<th scope="col">Время</th>
				<th scope="col">Понедельник</th>
				<th scope="col">Вторник</th>
				<th scope="col">Среда</th>
				<th scope="col">Четверг</th>
				<th scope="col">Пятница</th>
				<th scope="col">Суббота</th>
			</tr>
		</thead>
		<tbody>
			<tr>
				<th scope="row">1</th>
				<td>8:30 - 9:10</td>
				{#each timetable.days as day}
					<td>
						{#if day[0]}
							<span>
								{day[0].title}
							</span>
							{#if day[0].groups.length === 1}
								<sup>
									<b>{day[0].groups[0].classroom}</b>
								</sup>
							{:else if day[0].groups.length === 2}
								<div class="column">
									{day[0].groups[0].teacher}
									<b>{day[0].groups[0].classroom}</b> <br />
									{day[0].groups[1].teacher}
									<b>{day[0].groups[1].classroom}</b>
								</div>
							{/if}
						{/if}
					</td>
				{/each}
			</tr>
			<tr>
				<th scope="row">2</th>
				<td>9:30 - 10:10</td>
				{#each timetable.days as day}
					<td>
						{#if day[1]}
							{day[1].title}
							{#if day[1].groups.length === 1}
								<sup>
									<b>{day[1].groups[0].classroom}</b>
								</sup>
							{:else if day[1].groups.length === 2}
								<div class="column">
									{day[1].groups[0].teacher}
									<b>{day[1].groups[0].classroom}</b> <br />
									{day[1].groups[1].teacher}
									<b>{day[1].groups[1].classroom}</b>
								</div>
							{/if}
						{/if}
					</td>
				{/each}
			</tr>
			<tr>
				<th scope="row">3</th>
				<td>10:20 - 11:00</td>
				{#each timetable.days as day}
					<td>
						{#if day[2]}
							{day[2].title}
							{#if day[2].groups.length === 1}
								<sup>
									<b>{day[2].groups[0].classroom}</b>
								</sup>
							{:else if day[2].groups.length === 2}
								<div class="column">
									{day[2].groups[0].teacher}
									<b>{day[2].groups[0].classroom}</b> <br />
									{day[2].groups[1].teacher}
									<b>{day[2].groups[1].classroom}</b>
								</div>
							{/if}
						{/if}
					</td>
				{/each}
			</tr>
			<tr>
				<th scope="row">4</th>
				<td>11:10 - 11:50</td>
				{#each timetable.days as day}
					<td>
						{#if day[3]}
							{day[3].title}
							{#if day[3].groups.length === 1}
								<sup>
									<b>{day[3].groups[0].classroom}</b>
								</sup>
							{:else if day[3].groups.length === 2}
								<div class="column">
									{day[3].groups[0].teacher}
									<b>{day[3].groups[0].classroom}</b> <br />
									{day[3].groups[1].teacher}
									<b>{day[3].groups[1].classroom}</b>
								</div>
							{/if}
						{/if}
					</td>
				{/each}
			</tr>
			<tr>
				<th scope="row">5</th>
				<td>12:15 - 12:55</td>
				{#each timetable.days as day}
					<td>
						{#if day[4]}
							{day[4].title}
							{#if day[4].groups.length === 1}
								<sup>
									<b>{day[4].groups[0].classroom}</b>
								</sup>
							{:else if day[4].groups.length === 2}
								<div class="column">
									{day[4].groups[0].teacher}
									<b>{day[4].groups[0].classroom}</b> <br />
									{day[4].groups[1].teacher}
									<b>{day[4].groups[1].classroom}</b>
								</div>
							{/if}
						{/if}
					</td>
				{/each}
			</tr>
			<tr>
				<th scope="row">6</th>
				<td>13:20 - 14:00</td>
				{#each timetable.days as day}
					<td>
						{#if day[5]}
							{day[5].title}
							{#if day[5].groups.length === 1}
								<sup>
									<b>{day[5].groups[0].classroom}</b>
								</sup>
							{:else if day[5].groups.length === 2}
								<div class="column">
									{day[5].groups[0].teacher}
									<b>{day[5].groups[0].classroom}</b> <br />
									{day[5].groups[1].teacher}
									<b>{day[5].groups[1].classroom}</b>
								</div>
							{/if}
						{/if}
					</td>
				{/each}
			</tr>
			<tr>
				<th scope="row">7</th>
				<td>14:10 - 14:50</td>
				{#each timetable.days as day}
					<td>
						{#if day[6]}
							{day[6].title}
							{#if day[6].groups.length === 1}
								<sup>
									<b>{day[6].groups[0].classroom}</b>
								</sup>
							{:else if day[6].groups.length === 2}
								<div class="column">
									{day[6].groups[0].teacher}
									<b>{day[6].groups[0].classroom}</b> <br />
									{day[6].groups[1].teacher}
									<b>{day[6].groups[1].classroom}</b>
								</div>
							{/if}
						{/if}
					</td>
				{/each}
			</tr>
			<tr>
				<th scope="row">8</th>
				<td>15:05 - 15:45</td>
				{#each timetable.days as day}
					<td>
						{#if day[7]}
							{day[7].title}
							{#if day[7].groups.length === 1}
								<sup>
									<b>{day[7].groups[0].classroom}</b>
								</sup>
							{:else if day[7].groups.length === 2}
								<div class="column">
									{day[7].groups[0].teacher}
									<b>{day[7].groups[0].classroom}</b> <br />
									{day[7].groups[1].teacher}
									<b>{day[7].groups[1].classroom}</b>
								</div>
							{/if}
						{/if}
					</td>
				{/each}
			</tr>
			<tr>
				<th scope="row">9</th>
				<td>16:00 - 16:40</td>
				{#each timetable.days as day}
					<td>
						{#if day[8]}
							{day[8].title}
							{#if day[8].groups.length === 1}
								<sup>
									<b>{day[8].groups[0].classroom}</b>
								</sup>
							{:else if day[8].groups.length === 2}
								<div class="column">
									{day[8].groups[0].teacher}
									<b>{day[8].groups[0].classroom}</b> <br />
									{day[8].groups[1].teacher}
									<b>{day[8].groups[1].classroom}</b>
								</div>
							{/if}
						{/if}
					</td>
				{/each}
			</tr>
			<tr>
				<th scope="row">10</th>
				<td>16:50 - 17:30</td>
				{#each timetable.days as day}
					<td>
						{#if day[9]}
							{day[9].title}
							{#if day[9].groups.length === 1}
								<sup>
									<b>{day[9].groups[0].classroom}</b>
								</sup>
							{:else if day[9].groups.length === 2}
								<div class="column">
									{day[9].groups[0].teacher}
									<b>{day[9].groups[0].classroom}</b> <br />
									{day[9].groups[1].teacher}
									<b>{day[9].groups[1].classroom}</b>
								</div>
							{/if}
						{/if}
					</td>
				{/each}
			</tr>
		</tbody>
	</table>
	<i class="last-updated">Последнее обновление: {timetable.lastUpdated.toLocaleDateString()}</i>
</div>

<style>
	a {
		display: inline-flex;
		align-items: center;
		gap: 0.25em;

		text-decoration: none;
	}

	ul {
		margin-bottom: 0.25em;
	}

	.grid {
		margin-bottom: 1em;
		row-gap: 0;
	}

	select {
		margin: 0.25em 0;
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

	button {
		display: flex;
		align-items: center;
		gap: 0.25em;
	}

	.wide {
		width: 100%;
		justify-content: center;
	}

	@media not print {
		#print {
			display: none;
		}
	}

	@media print {
		* {
			font-size: 0.9em;
		}

		#print {
			display: initial;
			zoom: 90%;
		}

		#no-print {
			display: none;
		}

		h2 {
			margin-top: 2em;

			font-size: 1.5em;
			text-align: center;
		}

		h2:first-of-type {
			margin-top: 1em;
		}

		table {
			margin-bottom: 0.25em;
		}

		td {
			vertical-align: center;
		}

		td,
		th {
			padding: 0.25em 0.25em;
		}

		th:first-of-type {
			padding-left: 0.75em;
		}

		.column {
			display: inline-block;
			font-size: 0.6em;
		}

		.last-updated {
			display: flex;
			justify-content: end;

			font-size: 0.5em;
			color: gray;
		}
	}
</style>
