<script lang="ts">
  import { onMount } from 'svelte'

  let { value = '', label = '', prefix = '', suffix = '', source = '' }: {
    value?: string
    label?: string
    prefix?: string
    suffix?: string
    source?: string
  } = $props()

  let visible = $state(false)

  function handleIntersect(entries: IntersectionObserverEntry[]) {
    if (entries[0]?.isIntersecting) {
      visible = true
    }
  }

  onMount(() => {
    const id = `stat-${label.replace(/\s+/g, '-')}`
    const el = document.getElementById(id)
    if (el) {
      const observer = new IntersectionObserver(handleIntersect, { threshold: 0.3 })
      observer.observe(el)
      return () => observer.disconnect()
    }
  })
</script>

<div
  id="stat-{label.replace(/\s+/g, '-')}"
  class="text-center {visible ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-4'} transition-all duration-700"
>
  <div class="stat-number text-2xl md:text-3xl font-bold text-brand-500 dark:text-brand-400">
    {prefix}{value}{suffix}
  </div>
  {#if label}
    <div class="text-xs text-surface-500 mt-1">{label}</div>
  {/if}
  {#if source}
    <div class="text-[10px] text-surface-600 mt-0.5 italic">— {source}</div>
  {/if}
</div>
