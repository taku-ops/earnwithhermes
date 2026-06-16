<script lang="ts">
  interface Testimony {
    quote: string
    author: string
    stat?: string
    statLabel?: string
    link?: string
  }

  let { testimonies }: { testimonies: Testimony[] } = $props()

  let current = $state(0)
  let transitioning = $state(false)

  const total = $derived(testimonies.length)

  function goTo(idx: number) {
    if (transitioning) return
    transitioning = true
    current = ((idx % total) + total) % total
    // Allow transition to finish before next interaction
    setTimeout(() => transitioning = false, 400)
  }

  function prev() { goTo(current - 1) }
  function next() { goTo(current + 1) }
</script>

<div class="relative">
  <!-- Card container with carousel behavior -->
  <div class="overflow-hidden rounded-xl border border-surface-800 bg-surface-900/50">
    <div
      class="flex transition-transform duration-300 ease-in-out"
      style="transform: translateX(-{current * 100}%)"
    >
      {#each testimonies as t, i}
        <a
          href={t.link || '#'}
          class="min-w-full p-8 md:p-10 flex flex-col"
          role="presentation"
        >
          <blockquote class="text-sm md:text-base text-surface-300 leading-relaxed mb-6 flex-1">
            &ldquo;{t.quote}&rdquo;
          </blockquote>
          <div class="flex items-center justify-between mt-auto pt-4 border-t border-surface-800">
            <div>
              <div class="text-sm font-semibold text-surface-100">{t.author}</div>
            </div>
            {#if t.stat}
              <div class="text-right flex-shrink-0 ml-3">
                <div class="text-base font-bold text-brand-500 dark:text-brand-400">{t.stat}</div>
                {#if t.statLabel}
                  <div class="text-[11px] text-surface-500">{t.statLabel}</div>
                {/if}
              </div>
            {/if}
          </div>
        </a>
      {/each}
    </div>
  </div>

  <!-- Prev / Next arrows -->
  <button
    onclick={prev}
    class="absolute left-3 top-1/2 -translate-y-1/2 w-8 h-8 rounded-full border border-surface-700 bg-surface-900/80 flex items-center justify-center text-surface-400 hover:text-surface-100 hover:border-surface-500 transition-all"
    aria-label="Previous testimony"
  >
    <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
      <path stroke-linecap="round" stroke-linejoin="round" d="M15 19l-7-7 7-7" />
    </svg>
  </button>
  <button
    onclick={next}
    class="absolute right-3 top-1/2 -translate-y-1/2 w-8 h-8 rounded-full border border-surface-700 bg-surface-900/80 flex items-center justify-center text-surface-400 hover:text-surface-100 hover:border-surface-500 transition-all"
    aria-label="Next testimony"
  >
    <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
      <path stroke-linecap="round" stroke-linejoin="round" d="M9 5l7 7-7 7" />
    </svg>
  </button>

  <!-- Dots -->
  {#if total > 1}
    <div class="flex items-center justify-center gap-2 mt-5">
      {#each Array(total) as _, i}
        <button
          onclick={() => goTo(i)}
          class="rounded-full transition-all duration-200 {i === current ? 'w-6 h-2 bg-brand-500' : 'w-2 h-2 bg-surface-700 hover:bg-surface-500'}"
          aria-label="Go to testimony {i + 1}"
        />
      {/each}
    </div>
  {/if}
</div>
