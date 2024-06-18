<template>
    <div class="w-[250px] my-auto p-4 rounded-lg border-gray-400 bg-cyan-900 text-white">
     <h2 class="w-full underline text-center my-2">
      {{  props.title}}
     </h2>
     <div class="w-[80%] mx-auto grid place-items-center">
     <slot >
        Default content
     </slot>
     </div>
    </div>
</template>

<script setup lang="ts">
const props=defineProps<{title:string,}>()
</script>
