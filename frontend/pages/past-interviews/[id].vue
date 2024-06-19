<template>
  <div class="h-4/5 w-[90%] mx-auto grid grid-cols-4 grid-rows-2 gap-x-4">
    <div class="grid row-span-2 col-span-1 grid-rows-2">
      <div>
        <h3>Interview Summary {{ id }}</h3>
        <br />
        <ul>
          <li>Time:</li>
          <li>Confidence:</li>
          <li>Fluency</li>
        </ul>
      </div>
      <div>
        <h3>Things to work on</h3>
        <br />
        <ul>
          <li>Brevity</li>
          <li>Organization of Ideas</li>
        </ul>
      </div>
    </div>
    <div
      class="row-span-2 col-span-3 overflow-y-scroll scrollbar-thin scrollbar-thumb-sky-700 scrollbar-track-slate-200"
    >
      <h3>Transcript</h3>
      <br />
      <div class="h-screen">
        <br /><br />
        <ChatView />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
const id = useRoute().params.id;
</script>
