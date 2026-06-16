<script lang="ts">
  let email = $state('')
  let status = $state<'idle' | 'loading' | 'success' | 'error'>('idle')
  let errorMsg = $state('')

  async function submit(e: Event) {
    e.preventDefault()
    const trimmed = email.trim()
    if (!trimmed) return
    status = 'loading'
    try {
      const res = await fetch('/api/subscribe', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email: trimmed }),
      })
      const data = await res.json()
      if (data.ok) {
        status = 'success'
      } else {
        status = 'error'
        errorMsg = data.error || 'Something went wrong'
      }
    } catch {
      status = 'error'
      errorMsg = 'Could not connect. Try again later.'
    }
  }
</script>

{#if status === 'success'}
  <div class="text-center py-6 animate-fade-in">
    <div class="inline-flex items-center justify-center w-12 h-12 rounded-full bg-brand-500/20 mb-3">
      <svg class="w-6 h-6 text-brand-400" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
        <path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7" />
      </svg>
    </div>
    <p class="text-brand-400 font-medium text-sm">You're subscribed!</p>
    <p class="text-surface-500 text-xs mt-1">We'll send you the good stuff.</p>
  </div>
{:else}
  <form onsubmit={submit} class="flex items-center gap-3">
    <div class="flex-1 relative">
      <input
        type="email"
        bind:value={email}
        placeholder="your@email.com"
        required
        disabled={status === 'loading'}
        class="w-full px-5 py-3 rounded-xl bg-white dark:bg-surface-900 border border-surface-300 dark:border-surface-700 text-gray-900 dark:text-white placeholder:text-surface-400 dark:placeholder:text-surface-600 text-sm focus:outline-none focus:border-brand-500 transition-colors disabled:opacity-50"
      />
    </div>
    <button
      type="submit"
      disabled={status === 'loading'}
      class="proximity-btn relative px-6 py-3 rounded-xl bg-brand-600 dark:bg-brand-500 hover:bg-brand-700 dark:hover:bg-brand-400 text-white dark:text-black font-semibold text-sm transition-all duration-200 whitespace-nowrap disabled:opacity-50"
    >
      {status === 'loading' ? 'Subscribing...' : 'Subscribe'}
    </button>
  </form>
  {#if status === 'error'}
    <p class="text-red-400 text-xs mt-2">{errorMsg}</p>
  {/if}
{/if}
