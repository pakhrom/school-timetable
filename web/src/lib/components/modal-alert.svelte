<script lang="ts">
	// Источник: Svelte playground

	import type { Snippet } from 'svelte';

	let {
		showModal = $bindable(),
		expand = false,
		children
	}: {
		showModal: boolean;
		expand?: boolean;
		children?: Snippet;
	} = $props();

	let dialog: HTMLDialogElement | undefined = $state();

	$effect(() => {
		if (showModal) dialog?.showModal();
		if (!showModal) dialog?.close();
	});
</script>

<!-- svelte-ignore a11y_click_events_have_key_events, a11y_no_noninteractive_element_interactions -->
<dialog
	bind:this={dialog}
	class={expand ? 'expand' : ''}
	aria-label="Modal Alert"
	onclose={() => {
		showModal = false;
	}}
	onclick={(event) => {
		if (event.target === dialog) dialog?.close();
	}}
>
	<article>
		{@render children?.()}
	</article>
</dialog>

<style>
	dialog {
		max-width: 32em;
		max-height: 90vh;
		padding: 0;

		background-color: transparent;
		border: none;
	}

	dialog.expand {
		width: 90%;
		max-width: none;
	}

	dialog::backdrop {
		background: rgba(0, 0, 0, 0.4);
		backdrop-filter: blur(0.08em);
	}

	dialog[open] {
		animation: zoom 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
	}
	@keyframes zoom {
		from {
			transform: scale(0.95);
		}
		to {
			transform: scale(1);
		}
	}
	dialog[open]::backdrop {
		animation: fade 0.2s ease-out;
	}
	@keyframes fade {
		from {
			opacity: 0;
		}
		to {
			opacity: 1;
		}
	}
</style>
