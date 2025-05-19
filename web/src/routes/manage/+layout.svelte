<script lang="ts">
	import { goto } from '$app/navigation';
	import type { LayoutProps } from './$types';

	let { children, data }: LayoutProps = $props();

	if (!data.token) {
		goto('/');
	}
</script>

{@render children()}
