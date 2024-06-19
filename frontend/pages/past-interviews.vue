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
            :heading="slotProps.option.title"
            :timestamp="slotProps.option.created_at"
            :rating="slotProps.option.rating" />
          </template>
        </List>
      </template>
      <template #noneSelected>
        <p class="w-full text-center text-3xl">
          Select an interview to view it on this panel
        </p>
      </template>
      <div class="h-[90vh] ">
        <NuxtPage :page-key="(route) => route.fullPath" :keepalive="false" />
      </div>
    </NuxtLayout>
  </div>
</template>

<script setup lang="ts">
interface previewInterview extends Interviews {
  label: string;
}

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

definePageMeta({
  layout: false,
  title: "Past Interviews",
});
</script>
