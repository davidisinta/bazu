<template>
  <div
    
    class="grid place-items-center w-full h-full "
    :class="props.contClass"
    :aria-label="`${props.label}. Please check your network or refresh your browser`"
    tabindex="0"
  >
   <ClientOnly>
    <Icon name="fluent-mdl2:status-circle-error-x" color="red" width="45" height="45" />
    </ClientOnly>
    <p aria-hidden="true">Please check your network or refresh your browser</p>
  </div>
</template>

<script setup lang="ts"> 
const props=withDefaults(defineProps<{label?:string,contClass?:string}>(),{
  label:"Error loading data."
})
</script>

