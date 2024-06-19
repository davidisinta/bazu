<template>
  <div class="h-full w-[90%]">
    <div v-for="message in sampleMessages">
      <div  class="w-1/2  p-4 rounded-md mb-4" :class="`${message.role == 'user'?'ml-auto mr-0 bg-slate-300':'ml-0 mr-auto border-2 bg-slate-100'}`" >
        {{ message.message }}
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
interface message {
  role: "user" | "assistant";
  message: string;
}
interface chatProps {
  messages?: string;
}
const props = defineProps<chatProps>();

const { messages } = toRefs(props);
const sampleMessages = ref<Array<message>>([
  { role: "user", message: "lorem ipsum" },
  { role: "assistant", message: "lorem ipsum" },
  { role: "user", message: "lorem ipsum" },
  { role: "assistant", message: "lorem ipsum" },
  { role: "user", message: "lorem ipsum" },
  { role: "assistant", message: "lorem ipsum" },
  { role: "user", message: "lorem ipsum" },
  { role: "assistant", message: "lorem ipsum" },
  { role: "user", message: "lorem ipsum" },
  { role: "assistant", message: "lorem ipsum" },
]);
</script>
