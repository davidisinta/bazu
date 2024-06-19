<template>
  <div class="w-full rounded-sm p-2 border-y ">
    <h3>{{ heading }}</h3>
    <div class="w-[90%] flex gap-4 justify-between">
    <span>{{ humanTime }}</span> 
    
    <PrimeRating v-model="rating" readonly :cancel="false" :pt="{
      onIcon:'text-amber-400',
      offIcon:'text-black'
    }" />
    </div>
  </div>
</template>

<script setup lang="ts">
const props = defineProps<{
  timestamp: string;
  heading: string;
  rating: number;
}>();
const { timestamp, heading, rating } = toRefs(props);
const humanTime = computed(() => useTimeAgo(timestamp.value).value);

</script>
