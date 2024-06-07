<template>
  <div
    class="grid grid-cols-4 gap-[10px] h-[90%] w-full items-start relative ml-2"
  >
    <List
      :is-error="isError"
      :selected-option="currentChat"
      error-label="Error Loading Chats"
      loading-label="Loading chats."
      :is-loading="isLoading"
      :create-mode="createMode"
      :options="(labelledChats as Array<any>)"
      :list-props="{
        optionValue: 'id',
        filter: true,
        filterFields: ['title'],
        optionLabel: 'label',
        dataKey: 'id',
        selectionMessage:
          'Press Tab to explore the chat. To return, press escape and continue browsing other chats in this list.',
        emptySelectionMessage: 'No chat selected',
        emptyMessage: 'Loading Chats. ',
        emptyFilterMessage:
          'No Chats Found. Try using chat tags relating to the chat',
        filterMessage: '{0} chats found. Use arrow keys to browse the result. ',
        filterPlaceholder: 'Search Chat',
      }"
      @update-selection="updateCurrChat"
    >
      <template #previewSlot="slotProps">
        <ChatPreview
          @update-aria="
            (ariaUpdate) => {
              if (labelledChats?.length) {
                labelledChats[slotProps.index].label = ariaUpdate;
              }
            }
          "
          :heading="slotProps.option.title"
          :timestamp="slotProps.option.created_at"
        />
      </template>
    </List>

    <div
      class="col-span-3 h-screen overflow-y-scroll scrollbar-thin scrollbar-thumb-sky-700 scrollbar-track-slate-200"
    >
      <NuxtPage :page-key="(route) => route.fullPath" :keepalive="false" />
    </div>
  </div>
</template>

<script setup lang="ts">
interface previewChat extends Chats {
  label: string;
}
// const { chats, chat, isError, isLoading } = storeToRefs(useChatsStore());
const isError = ref(false);
const isLoading = ref(false);
const labelledChats = ref<Array<previewChat>>([
  {
    id:1,
    label: "Behavioural Interview",
    title: "Behavioural Interview",
    created_at: "2024-02-09 22:01:47.67+00",
    creator: "Ron Pile",
  },
  {
    id:2,
    label: "Tecnical Interview",
    title: "Tecnical Interview",
    created_at: "2024-02-23 03:50:33.929+00",
    creator: "David Isinta",
  },
]);
const currentChat = ref<Chats | undefined>();

const mountedState = ref(false);
const createMode = ref(false);
async function updateCurrChat(val: any) {
  currentChat.value = val;

  // console.log(`selected`, val);
}

// watchEffect(() => {
//   if (chats.value) {

//     labelledChats.value = chats.value?.map((chat) => {
//       return { label: "", ...chat };
//     });
//     // console.log(`changing chats in store`);
//   }
// });
// watchEffect(() => {
//   if (currentChat.value) {
//     chat.value = currentChat.value;
//     createMode.value = false;
//     // console.log(`Changing current post`);
//   }
// });

// function addChat(payload: Chats) {
//   useChatsStore().chats.push(payload);

//   createMode.value = false;
// }
// function cancelChat() {
//   createMode.value = false;
// }
// await useChatsStore().fetchAllChats();

definePageMeta({
  keepalive: true,
});
</script>
