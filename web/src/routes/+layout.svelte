<script lang="ts">
	import '$lib/styles/pico.blue.min.css';
	import type { Snippet } from 'svelte';

	let { children }: { children: Snippet } = $props();
</script>

{@render children()}
