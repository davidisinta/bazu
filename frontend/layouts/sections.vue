<template>
  <div class="h-fit">
    <A11yNavSkipLink />
    <PageNavbar />
    <main
      class="relative border-x-2 border-gray-400 w-[90vw] mx-auto h-screen"
      name="main-content"
      id="main-content"
    >
      <div
        class="grid grid-cols-4 gap-[10px] h-[85vh] w-full items-start relative ml-2"
      >
        <div class="col-span-1 h-full">
          <br />
          <slot name="list"> Default List here </slot>
        </div>
        <div
          class="col-span-3 pl-10 pt-4 h-[85vh] overflow-y-scroll scrollbar-thin scrollbar-thumb-sky-700 scrollbar-track-slate-200"
        >
          <div
            v-if="!useRoute().params.id"
            class="col-span-3 h-full grid items-center"
          >
            <p class="w-full text-center text-3xl">
              <slot name="noneSelected">Default empty selection</slot>
            </p>
          </div>
          <slot />
        </div>
      </div>
    </main>
  </div>
</template>
