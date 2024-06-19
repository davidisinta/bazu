<template>
  <form @submit.prevent="submitDetails" class="w-full flex justify-between">
    <input
      v-model="content"
      type="text"
      :placeholder="props.placeholder"
      class="p-2 bg-white rounded-lg border-2 border-gray-400 w-[90%]"
    />
    <div class="h-full grid place-items-center"><slot /></div>
    <button type="submit"><slot name="submitIcon"></slot></button>
  </form>
</template>

<script setup lang="ts">
interface inputProps {
  placeholder: string;
}
const content = defineModel("");
const props = defineProps<inputProps>();
const emit = defineEmits(["submit"]);

function submitDetails() {
  console.log(`Submit emitted`);
  emit("submit", content.value);
}
</script>
