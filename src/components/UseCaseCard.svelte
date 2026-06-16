<script lang="ts">
  import ProximityCard from './ProximityCard.svelte'

  let { href = '', category = '', badge = '', title = '', summary = '', author = '', badgeColor = 'emerald' }: {
    href: string
    category?: string
    badge?: string
    title: string
    summary?: string
    author?: string
    badgeColor?: string
  } = $props()

  const badgeColors: Record<string, string> = {
    emerald: 'bg-emerald-500/10 text-emerald-400',
    blue: 'bg-blue-500/10 text-blue-400',
    purple: 'bg-purple-500/10 text-purple-400',
    orange: 'bg-orange-500/10 text-orange-400',
    red: 'bg-red-500/10 text-red-400',
  }
  const badgeClass = $derived(badgeColors[badgeColor] || badgeColors.emerald)
</script>

<ProximityCard {href}>
  <div class="flex items-center gap-2 mb-4">
    {#if category}
      <span class="px-2.5 py-1 rounded-md {badgeClass} text-xs font-medium">{category}</span>
    {/if}
    {#if badge}
      <span class="px-2.5 py-1 rounded-md bg-brand-500/10 text-brand-400 text-xs font-medium">{badge}</span>
    {/if}
  </div>
  <h3 class="font-semibold text-lg mb-2 group-hover:text-brand-400 transition-colors">
    {title}
  </h3>
  {#if summary}
    <p class="text-surface-400 text-sm leading-relaxed mb-4">{summary}</p>
  {/if}
  <div class="flex items-center justify-between pt-3 border-t border-surface-800">
    {#if author}
      <span class="text-xs text-surface-600">{author}</span>
    {:else}
      <span class="hidden"></span>
    {/if}
    <span class="text-xs text-brand-500 font-medium">Read story →</span>
  </div>
</ProximityCard>
