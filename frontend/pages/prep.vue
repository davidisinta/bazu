<template>
  <div>
    <NuxtLayout name="sections">
      <template #list>
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
            dataKey: 'id',
            selectionMessage:
              'Press Tab to explore the chat. To return, press escape and continue browsing other chats in this list.',
            emptySelectionMessage: 'No chat selected',
            emptyMessage: 'Loading Chats. ',
            emptyFilterMessage:
              'No Chats Found. Try using chat tags relating to the chat',
            filterMessage:
              '{0} chats found. Use arrow keys to browse the result. ',
            filterPlaceholder: 'Search Chat',
          }"
          @update-selection="updateCurrChat"
        >
          <template #previewSlot="slotProps">
            <ChatPreview
              :heading="slotProps.option.title"
              :timestamp="slotProps.option.created_at"
            />
          </template>
        </List>
      </template>
      <template #noneSelected>
        <div class="w-[80%] h-[80%] flex flex-col  justify-between">
          <h2>Quick Actions based on your profile</h2>
          <div class="w-[90%] grid grid-cols-3 gap-4">
            <PrepQuickactions
              v-for="{  action } in actions"
              :action="action"
              class="col-span-1"
           
            />
          </div>
          <Inputbox
            placeholder="Ask me anything you need prep for"
            v-model="prepQuestion"
            @submit="askQuestion"
          >
            <template #submitIcon>
              <Icon name="mdi:send-outline" size="32" />
            </template>
          </Inputbox>
        </div>
      </template>
      <div>
        <NuxtPage :page-key="(route) => route.fullPath" :keepalive="false" />
      </div>
    </NuxtLayout>
  </div>
</template>

<script setup lang="ts">
interface previewChat extends Chats {
  label: string;
}
// const { chats, chat, isError, isLoading } = storeToRefs(useChatsStore());
const isError = ref(false);
const isLoading = ref(false);
const prepQuestion = ref("");
const labelledChats = ref<Array<previewChat>>([
  {
    id: 1,
    label: "Behavioural Interview",
    title: "Behavioural Interview",
    created_at: "2024-02-09 22:01:47.67+00",
    creator: "Ron Pile",
  },
  {
    id: 2,
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
  console.log(`selected`, val);
  navigateTo(`/prep/${val.id}`);
}

const actions = ref([
  { title: "Microsoft Prep Interview", action: "Microsoft Prep Interview" },
  { action: "Technical jargon during interview" },
  { action: "How to buy time during interview" },
]);

function askQuestion() {
  console.log(`submit event to ask prep question`);
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
  layout: false,
});
</script>
