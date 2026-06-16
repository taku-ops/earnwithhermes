<script lang="ts">
  import { onMount } from 'svelte'
  import DarkToggle from './DarkToggle.svelte'

  let scrolled = $state(false)
  let mobileOpen = $state(false)

  function handleScroll() {
    scrolled = window.scrollY > 20
  }

  onMount(() => {
    handleScroll()
    window.addEventListener('scroll', handleScroll, { passive: true })
    return () => window.removeEventListener('scroll', handleScroll)
  })
</script>

<nav
  class="sticky top-0 z-50 border-b transition-all duration-300 {scrolled ? 'border-white/5 bg-surface/80' : 'border-transparent bg-transparent'}"
>
  <div class="max-w-6xl mx-auto px-6 h-16 flex items-center justify-between">
    <!-- Logo -->
    <a href="/" class="flex items-center gap-2.5 group">
      <div class="w-7 h-7 rounded-lg bg-brand-500 flex items-center justify-center transition-transform duration-200 group-hover:scale-105">
        <span class="text-black font-bold text-sm">$</span>
      </div>
      <span class="font-semibold text-sm">Earn With Hermes</span>
      <span class="text-xs text-surface-500 hidden sm:inline">by Autonomics</span>
    </a>

    <!-- Desktop nav -->
    <div class="hidden md:flex items-center gap-2">
      <a href="/use-cases/" class="text-sm text-surface-400 transition-colors px-3">Use Cases</a>
      <a href="/learn/" class="text-sm text-surface-400 transition-colors px-3">Learn</a>
      <a href="/connect/" class="text-sm text-surface-400 transition-colors px-3">Connect</a>
      <DarkToggle />
    </div>

    <!-- Mobile toggle -->
    <button
      class="md:hidden p-2 rounded-lg hover:bg-surface-800 transition-colors"
      onclick={() => mobileOpen = !mobileOpen}
      aria-label="Toggle navigation"
    >
      <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
        {#if mobileOpen}
          <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
        {:else}
          <path stroke-linecap="round" stroke-linejoin="round" d="M4 6h16M4 12h16M4 18h16" />
        {/if}
      </svg>
    </button>
  </div>

  <!-- Mobile nav panel -->
  {#if mobileOpen}
    <div class="md:hidden border-t border-surface-700/20 dark:border-white/5 bg-surface/95 backdrop-blur-xl">
      <div class="px-6 py-4 flex flex-col gap-3">
        <a href="/use-cases/" class="text-sm text-surface-300 py-2 transition-colors" onclick={() => mobileOpen = false}>Use Cases</a>
        <a href="/learn/" class="text-sm text-surface-300 py-2 transition-colors" onclick={() => mobileOpen = false}>Learn</a>
        <a href="/connect/" class="text-sm text-surface-300 py-2 transition-colors" onclick={() => mobileOpen = false}>Connect</a>
      </div>
    </div>
  {/if}
</nav>
