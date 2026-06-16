<script lang="ts">
  interface Metric {
    value: string
    label: string
    sublabel?: string
  }

  let { metric }: { metric: Metric } = $props()
  let mx = $state(50)
  let my = $state(50)
</script>

<div
  class="proximity-glow rounded-xl border border-surface-800 bg-surface-900/50 p-5"
  style="--mx: {mx}%; --my: {my}%"
  onmousemove={(e) => {
    const rect = (e.currentTarget as HTMLElement).getBoundingClientRect()
    mx = ((e.clientX - rect.left) / rect.width) * 100
    my = ((e.clientY - rect.top) / rect.height) * 100
  }}
  role="presentation"
>
  <div class="text-xs text-surface-500 uppercase tracking-wider font-medium mb-1">{metric.label}</div>
  <div class="stat-number text-2xl font-bold text-brand-500 dark:text-brand-400">{metric.value}</div>
  {#if metric.sublabel}
    <div class="text-xs text-surface-600 mt-1">{metric.sublabel}</div>
  {/if}
</div>
