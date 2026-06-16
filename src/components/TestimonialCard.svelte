<script lang="ts">
  interface Testimony {
    quote: string
    author: string
    role?: string
    stat?: string
    statLabel?: string
    link?: string
  }

  let { testimony }: { testimony: Testimony } = $props()
  let mx = $state(50)
  let my = $state(50)
</script>

<a
  href={testimony.link || '#'}
  class="proximity-glow block rounded-xl border border-surface-800 bg-surface-900/50 p-6 transition-all duration-200 h-full flex flex-col"
  style="--mx: {mx}%; --my: {my}%"
  onmousemove={(e) => {
    const rect = (e.currentTarget as HTMLElement).getBoundingClientRect()
    mx = ((e.clientX - rect.left) / rect.width) * 100
    my = ((e.clientY - rect.top) / rect.height) * 100
  }}
  role="presentation"
>
  <blockquote class="text-sm text-surface-300 dark:text-surface-300 leading-relaxed mb-4 flex-1">
    &ldquo;{testimony.quote}&rdquo;
  </blockquote>
  <div class="flex items-center justify-between mt-auto pt-3 border-t border-surface-800">
    <div>
      <div class="text-xs font-semibold text-surface-100 dark:text-surface-100">{testimony.author}</div>
      {#if testimony.role}
        <div class="text-[11px] text-surface-500 mt-0.5">{testimony.role}</div>
      {/if}
    </div>
    {#if testimony.stat}
      <div class="text-right flex-shrink-0 ml-3">
        <div class="text-sm font-bold text-brand-500 dark:text-brand-400">{testimony.stat}</div>
        {#if testimony.statLabel}
          <div class="text-[10px] text-surface-600">{testimony.statLabel}</div>
        {/if}
      </div>
    {/if}
  </div>
</a>
