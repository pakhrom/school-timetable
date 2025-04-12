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
<h1>Вход в аккаунт</h1>
<div class="grid">
	<label for="username">
		Логин
		<input type="text" name="username" id="username" />
	</label>
	<label for="password">
		Пароль
		<input type="password" name="password" id="password" />
	</label>
</div>
<button
	type="button"
	class="wide"
	onclick={() => {
		alert('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789');
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
		class="icon icon-tabler icons-tabler-outline icon-tabler-login"
	>
		<path stroke="none" d="M0 0h24v24H0z" fill="none" />
		<path d="M15 8v-2a2 2 0 0 0 -2 -2h-7a2 2 0 0 0 -2 2v12a2 2 0 0 0 2 2h7a2 2 0 0 0 2 -2v-2" />
		<path d="M21 12h-13l3 -3" />
		<path d="M11 15l-3 -3" />
	</svg>
	Войти
</button>

<button
	type="button"
	class="wide wrapper"
	onclick={() => {
		window.location.href = '/manage';
	}}
>
	Войти бесплатно, без регистрации и СМС
</button>

<style>
	a {
		display: inline-flex;
		align-items: center;
		gap: 0.25em;

		text-decoration: none;
	}

	.grid {
		margin-bottom: 1em;
		row-gap: 0;
	}

	input {
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

	.wrapper {
		background: repeating-linear-gradient(90deg in hsl longer hue, red 0 50%) 0/200%;
		animation: r 6s linear infinite;
		border: none;
	}
	@keyframes r {
		to {
			background-position: 100%;
		}
	}
</style>
