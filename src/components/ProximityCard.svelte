<script lang="ts">
  import type { Snippet } from 'svelte'

  interface Props {
    href?: string
    class?: string
    children?: Snippet
  }

  let { href, class: className = '', children }: Props = $props()
  let mx = $state(50)
  let my = $state(50)

  function handleMouse(e: MouseEvent) {
    const rect = (e.currentTarget as HTMLElement).getBoundingClientRect()
    mx = ((e.clientX - rect.left) / rect.width) * 100
    my = ((e.clientY - rect.top) / rect.height) * 100
  }
</script>

{#if href}
  <a
    {href}
    class="proximity-glow rounded-2xl bg-surface-900/50 border border-surface-800 p-6 cursor-pointer group block {className}"
    style="--mx: {mx}%; --my: {my}%"
    onmousemove={handleMouse}
  >
    {@render children?.()}
  </a>
{:else}
  <div
    class="proximity-glow rounded-2xl bg-surface-900/50 border border-surface-800 p-6 {className}"
    style="--mx: {mx}%; --my: {my}%"
    onmousemove={handleMouse}
    role="presentation"
  >
    {@render children?.()}
  </div>
{/if}
