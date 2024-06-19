<template>
    <div>
       <h2> Title for Interview id:{{ id }}</h2> <br><br>
        <ChatView/>
    </div>
</template>

<script setup lang="ts">
const id = useRoute().params.id
</script>
