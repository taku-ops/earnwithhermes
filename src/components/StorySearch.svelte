<script lang="ts">
  interface UseCase {
    id: string
    title: string
    description: string
    tags: string[]
    categories: string[]
    author?: string
    income?: string
    storySource?: string
  }

  let { stories }: { stories: UseCase[] } = $props()

  let query = $state('')

  // Organize categories for the no-search view
  const categoryLabels = [
    'Trading & Markets', 'Agency & Consulting',
    'Content Monetization', 'Building Products', 'Cost Savings',
  ]

  // Derive slug from category name
  function slugify(s: string) {
    return s.toLowerCase().replace(/[&\s]+/g, '-')
  }

  // Filtered results
  let filtered = $derived.by(() => {
    const q = query.trim().toLowerCase()
    if (!q) return null // null means "show category view"
    return stories.filter(s => {
      const haystack = [
        s.title, s.description, s.author || '',
        ...s.tags, ...s.categories, s.storySource || '',
      ].join(' ').toLowerCase()
      return haystack.includes(q)
    })
  })

  // Active-category tracking for the no-search view
  let activeCategory = $state('')
</script>

<div class="mb-10">
  <!-- Search input -->
  <div class="relative mb-6">
    <svg class="absolute left-3.5 top-1/2 -translate-y-1/2 w-4 h-4 text-surface-400 dark:text-surface-500 pointer-events-none" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
      <path stroke-linecap="round" stroke-linejoin="round" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
    </svg>
    <input
      type="search"
      bind:value={query}
      placeholder="Search stories by title, author, tag, keyword..."
      class="w-full pl-10 pr-4 py-2.5 rounded-xl border border-surface-300 dark:border-surface-700 bg-white dark:bg-surface-900 text-sm text-surface-950 dark:text-surface-50 placeholder:text-surface-400 dark:placeholder:text-surface-500 focus:outline-none focus:border-brand-500 focus:ring-1 focus:ring-brand-500/30 transition-all"
    />
    {#if query}
      <button
        onclick={() => query = ''}
        class="absolute right-3.5 top-1/2 -translate-y-1/2 w-4 h-4 text-surface-400 dark:text-surface-500 hover:text-surface-600 dark:hover:text-surface-300 transition-colors"
        aria-label="Clear search"
      >
        <svg fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
          <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
        </svg>
      </button>
    {/if}
  </div>

  {#if filtered !== null}
    <!-- Search results view -->
    {#if filtered.length === 0}
      <div class="text-center py-16">
        <p class="text-surface-500">No stories match <span class="text-surface-300 font-medium">"{query}"</span></p>
        <button
          onclick={() => query = ''}
          class="mt-3 text-sm text-brand-400 hover:text-brand-300 transition-colors"
        >Clear search</button>
      </div>
    {:else}
      <div class="flex items-center gap-2 mb-6">
        <span class="text-xs text-surface-500">{filtered.length} {filtered.length === 1 ? 'story' : 'stories'} found</span>
      </div>
      <div class="space-y-2">
        {#each filtered as uc (uc.id)}
          <a
            href={`/use-cases/${uc.id}/`}
            class="proximity-glow block rounded-xl border border-surface-800 bg-surface-900/50 p-4 transition-all duration-200"
          >
            <div class="flex items-center gap-4">
              <div class="flex-1 min-w-0">
                <h3 class="font-semibold text-sm truncate">{uc.title}</h3>
                <p class="text-xs text-surface-500 truncate mt-0.5">{uc.description}</p>
              </div>
              <div class="flex-shrink-0 text-right hidden sm:block">
                {#if uc.income}
                  <div class="text-sm font-bold text-brand-400">{uc.income}</div>
                {/if}
                {#if uc.author}
                  <div class="text-[10px] text-surface-600 mt-0.5">{uc.author}</div>
                {/if}
              </div>
              <svg class="flex-shrink-0 w-4 h-4 text-surface-500" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                <path stroke-linecap="round" stroke-linejoin="round" d="M9 5l7 7-7 7" />
              </svg>
            </div>
          </a>
        {/each}
      </div>
    {/if}
  {:else}
    <!-- Category filter pills (same as before) -->
    <div class="flex flex-wrap gap-2 mb-10">
      {#each categoryLabels as cat}
        <a href={`#${slugify(cat)}`}
          class="px-3 py-1.5 rounded-full text-xs font-medium border border-surface-700 text-surface-400 hover:bg-brand-600 dark:hover:bg-brand-500 hover:text-white dark:hover:text-black hover:border-brand-600 dark:hover:border-brand-500 transition-all duration-200"
        >
          {cat}
        </a>
      {/each}
    </div>

    <!-- Category sections -->
    {#each categoryLabels as cat}
      {@const slug = slugify(cat)}
      {@const catStories = stories.filter(uc => {
        const c = uc.categories?.[0]?.toLowerCase().replace(/[&\s]+/g, '-') || ''
        return c === slug
      })}
      {#if catStories.length > 0}
        <div class="mb-12" id={slug}>
          <div class="flex items-center justify-between mb-4">
            <h2 class="text-lg font-bold">{cat}</h2>
            <span class="text-xs text-surface-500">{catStories.length} stories</span>
          </div>
          <div class="space-y-2">
            {#each catStories as uc (uc.id)}
              <a
                href={`/use-cases/${uc.id}/`}
                class="proximity-glow block rounded-xl border border-surface-800 bg-surface-900/50 p-4 transition-all duration-200"
              >
                <div class="flex items-center gap-4">
                  <div class="flex-1 min-w-0">
                    <h3 class="font-semibold text-sm truncate">{uc.title}</h3>
                    <p class="text-xs text-surface-500 truncate mt-0.5">{uc.description}</p>
                  </div>
                  <div class="flex-shrink-0 text-right hidden sm:block">
                    {#if uc.income}
                      <div class="text-sm font-bold text-brand-400">{uc.income}</div>
                    {/if}
                    {#if uc.author}
                      <div class="text-[10px] text-surface-600 mt-0.5">{uc.author}</div>
                    {/if}
                  </div>
                  <svg class="flex-shrink-0 w-4 h-4 text-surface-500" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M9 5l7 7-7 7" />
                  </svg>
                </div>
              </a>
            {/each}
          </div>
        </div>
      {/if}
    {/each}
  {/if}
</div>
