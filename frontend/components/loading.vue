<template>
  <div
    class="grid place-items-center w-full h-full"
    :class="props.contClass"
    :aria-label="props.label"
    tabindex="0"
  >
    <ClientOnly>
      <Icon name="eos-icons:loading" color="#0369a1" width="45" height="45" />
    </ClientOnly>
    <p aria-hidden="true">Loading</p>
  </div>
</template>

<script setup lang="ts">
const props = withDefaults(
  defineProps<{ label?: string; contClass?: string }>(),
  {
    label: "Hold still while we load your details.",
  }
);

// defineOptions({
//      suspensible:false
// })
</script>
