<template>
  <div class="min-h-screen h-fit" >
    <PageNavbar/>
    <main class=" relative border-x-2 border-gray-400 w-[90vw] mx-auto h-fit " name="main-content" id="main-content">
      <NuxtPage :page-key="(route) => route.fullPath" />
    </main>
  </div>
</template>