<script lang="ts">
  import { onMount } from 'svelte'

  let visible = $state(false)
  let progress = $state(0)

  function handleScroll() {
    const scrollTop = window.scrollY
    const docHeight = document.documentElement.scrollHeight - window.innerHeight
    progress = docHeight > 0 ? Math.min(scrollTop / docHeight * 100, 100) : 0
    visible = scrollTop > 300
  }

  function scrollTop() {
    window.scrollTo({ top: 0, behavior: 'smooth' })
  }

  onMount(() => {
    window.addEventListener('scroll', handleScroll, { passive: true })
    return () => window.removeEventListener('scroll', handleScroll)
  })
</script>

<button
  onclick={scrollTop}
  class="fixed bottom-6 right-6 z-40 flex items-center justify-center w-10 h-10 rounded-full bg-surface-800 border border-surface-700 hover:bg-surface-700 transition-all duration-300 {visible ? 'opacity-100 pointer-events-auto scale-100' : 'opacity-0 pointer-events-none scale-0'}"
  aria-label="Scroll to top"
>
  <svg class="w-4 h-4 text-surface-300" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
    <path stroke-linecap="round" stroke-linejoin="round" d="M5 10l7-7m0 0l7 7m-7-7v18" />
  </svg>
  <!-- Progress ring indicator -->
  <svg class="absolute inset-0 w-full h-full -rotate-90" viewBox="0 0 40 40">
    <circle cx="20" cy="20" r="18" fill="none" stroke="currentColor" stroke-width="1.5"
      class="text-surface-800" opacity="0.3" />
    <circle cx="20" cy="20" r="18" fill="none" stroke="currentColor" stroke-width="1.5"
      class="text-brand-500" stroke-dasharray="113.1"
      stroke-dashoffset={113.1 - (progress / 100) * 113.1}
      stroke-linecap="round" />
  </svg>
</button>
