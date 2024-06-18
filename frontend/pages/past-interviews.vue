<template>
  <div class="">
    <NuxtLayout name="sections">
      <template #list>
        <List
          :is-error="isError"
          :selected-option="currentInterview"
          error-label="Error Loading Interviews"
          loading-label="Loading interviews."
          :is-loading="isLoading"
          :create-mode="createMode"
          :options="(labelledInterviews as Array<any>)"
          :list-props="{
            optionValue: 'id',
            filter: true,
            filterFields: ['title'],
            optionLabel: 'label',
            dataKey: 'id',
            selectionMessage:
              'Press Tab to explore the interview. To return, press escape and continue browsing other interviews in this list.',
            emptySelectionMessage: 'No interview selected',
            emptyMessage: 'Loading Interviews. ',
            emptyFilterMessage:
              'No Interviews Found. Try using interview tags relating to the interview',
            filterMessage:
              '{0} interviews found. Use arrow keys to browse the result. ',
            filterPlaceholder: 'Search Interview',
          }"
          @update-selection="updateCurrInterview"
        >
          <template #previewSlot="slotProps">
            <InterviewPreview
              @update-aria="
                (ariaUpdate) => {
                  if (labelledInterviews?.length) {
                    labelledInterviews[slotProps.index].label = ariaUpdate;
                  }
                }
              "
              :heading="slotProps.option.title"
              :timestamp="slotProps.option.created_at"
              :rating="slotProps.option.rating"
            />
          </template>
        </List>
      </template>
      <template #noneSelected>Select an interview to view it on this panel</template>
      <div>
        <NuxtPage :page-key="(route) => route.fullPath" :keepalive="false" />
      </div>
    </NuxtLayout>
  </div>
</template>

<script setup lang="ts">
interface previewInterview extends Interviews {
  label: string;
}
// const { interviews, interview, isError, isLoading } = storeToRefs(useInterviewsStore());
const isError = ref(false);
const isLoading = ref(false);
const labelledInterviews = ref<Array<previewInterview>>([
  {
    id: 1,
    label: "Behavioural Interview",
    title: "Behavioural Interview",
    created_at: "2024-02-09 22:01:47.67+00",
    rating: 4,
  },
  {
    id: 2,
    label: "Tecnical Interview",
    title: "Tecnical Interview",
    created_at: "2024-02-23 03:50:33.929+00",
    rating: 3,
  },
]);
const currentInterview = ref<Interviews | undefined>();

const createMode = ref(false);
async function updateCurrInterview(val: any) {
  currentInterview.value = val;

  console.log(`selected`, val);
  navigateTo(`/past-interviews/${val.id}`);
}

// watchEffect(() => {
//   if (interviews.value) {

//     labelledInterviews.value = interviews.value?.map((interview) => {
//       return { label: "", ...interview };
//     });
//     // console.log(`changing interviews in store`);
//   }
// });
// watchEffect(() => {
//   if (currentInterview.value) {
//     interview.value = currentInterview.value;
//     createMode.value = false;
//     // console.log(`Changing current post`);
//   }
// });

// function addInterview(payload: Interviews) {
//   useInterviewsStore().interviews.push(payload);

//   createMode.value = false;
// }
// function cancelInterview() {
//   createMode.value = false;
// }
// await useInterviewsStore().fetchAllInterviews();

definePageMeta({
  layout: false,
});
</script>
