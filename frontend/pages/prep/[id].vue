<template>
    <div>
        id:{{ id }}
    </div>
</template>

<script setup lang="ts">
const id = useRoute().params.id
</script>
