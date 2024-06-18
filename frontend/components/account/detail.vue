<template>
  <div class="w-full p-2 ">
    <b class="">{{ props.detail }}</b> :{{ props.value }}
  </div>
</template>

<script setup lang="ts">
const props = defineProps<{ detail: string; value: string }>();
</script>
