<script lang="ts">
  import { onMount } from 'svelte'

  let dark = $state(false)

  function toggle() {
    dark = !dark
    if (dark) {
      document.documentElement.classList.add('dark')
      localStorage.setItem('theme', 'dark')
    } else {
      document.documentElement.classList.remove('dark')
      localStorage.setItem('theme', 'light')
    }
  }

  onMount(() => {
    dark = document.documentElement.classList.contains('dark')
  })
</script>

<button
  onclick={toggle}
  class="p-2 rounded-lg hover:bg-surface-800 dark:hover:bg-surface-800 bg-surface-100 dark:bg-transparent transition-colors"
  aria-label={dark ? 'Switch to light mode' : 'Switch to dark mode'}
>
  {#if dark}
    <!-- Sun icon -->
    <svg class="w-4 h-4 text-surface-400" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
      <circle cx="12" cy="12" r="5" />
      <path stroke-linecap="round" d="M12 1v2M12 21v2M4.22 4.22l1.42 1.42M18.36 18.36l1.42 1.42M1 12h2M21 12h2M4.22 19.78l1.42-1.42M18.36 5.64l1.42-1.42" />
    </svg>
  {:else}
    <!-- Moon icon -->
    <svg class="w-4 h-4 text-surface-500" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
      <path stroke-linecap="round" d="M21 12.79A9 9 0 1111.21 3 7 7 0 0021 12.79z" />
    </svg>
  {/if}
</button>
