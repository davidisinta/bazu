<template>
  <PrimeCard @click="quickAction" class="hover:cursor-pointer">
    <template #content>
      <p>{{ props.action }}</p>
    </template>
  </PrimeCard>
</template>

<script setup lang="ts">
interface action {
  action: string;
 
}

const props = defineProps<action>();
function quickAction() {
  console.log(`Clicked card, sending AI request`);
}
</script>
