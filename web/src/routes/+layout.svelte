<script lang="ts">
	import '$lib/styles/pico.blue.min.css';
	import '$lib/styles/custom.css';

	let { children } = $props();
</script>

<main class="container">
	{@render children()}
</main>

<style>
	.container {
		padding: 1em 0.5em;
	}
</style>
