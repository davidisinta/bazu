<template>
  <div ref="el" class="w-full rounded-sm p-2 border-y">
    <h3>{{ heading }}</h3>
    <span>{{ humanTime }}</span>
  </div>
</template>

<script setup lang="ts">
const props = defineProps<{ timestamp: string; heading: string }>();
const { timestamp, heading } = toRefs(props);
const emit = defineEmits(["update-aria"]);
const humanTime = computed(() => useTimeAgo(timestamp.value).value);

const el = ref<HTMLElement | null>(null);
const isPosted = true;

watchEffect(() => {
  if (el.value) {
    const desc = `${heading.value}. ${humanTime.value}`;
    emit("update-aria", desc);
  }
});
</script>
