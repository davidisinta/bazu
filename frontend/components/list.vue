<template>
  <div class="ml-2  col-span-1 h-full">

    <div
      class="sticky h-[90%] inset-0 w-full overflow-y-scroll scrollbar-thin scrollbar-thumb-sky-700 scrollbar-track-slate-200"
    >
      <Loading
        v-if="isLoading"
        :label="loadingLabel"
        class="mx-auto"
        cont-class="h-full w-full"
        tabindex="0"
      />
      <Error
        v-else-if="isError"
        :label="errorLabel"
        cont-class="w-full h-fit m-auto"
      />

      <!-- ! Build stronger search filter?? Current one has tab order issues. But implement it to be almost the same, with results annouced by an aria-live  -->
      <PrimeListbox
     
        v-else
        :model-value="selectedOption"
        @update:model-value="updateSelection"
        :options="options"
        :select-on-focus="false"
        :filter="listProps.filter"
        :filter-fields="listProps.filterFields"
        :option-label="listProps.optionLabel"
        :data-key="listProps.dataKey"
        :selection-message="listProps.selectionMessage"
        :empty-selection-message="listProps.emptySelectionMessage"
        :empty-message="listProps.emptyMessage"
        :empty-filter-message="listProps.emptyFilterMessage"
        :filter-message="listProps.filterMessage"
        :filter-placeholder="listProps.filterPlaceholder"
        
        :pt-options="{ mergeSections: false, mergeProps: false }"

        :pt="{
          root:'w-full h-fit ',
          wrapper: 'h-fit',
          item: ({ context, state, instance, props }) => ({
            class: [
              {
                'border-2 border-sky-700 dark:border-white rounded-md dark:bg-white dark:text-black':
                  context.focused,
                'bg-sky-600 text-white rounded-sm': context.selected,
              },
            ],
            /*  'aria-label':`${state.focusedOptionIndex && labelledPosts?labelledPosts[state.focusedOptionIndex -1].label:''}` */
          }),
          filterInput:
            'bg-slate-50 p-2 w-[90%] border-2 rounded-sm focus:outline-2 text-black font-medium',
          filterIcon: 'ml-2',
          filterContainer: 'w-full p-2',
        }"
      >
        <template #option="slotProps" >
          <slot  name="previewSlot" v-bind="slotProps"></slot>
        </template>
      </PrimeListbox>
    </div>
  </div>
</template>

<script setup lang="ts">
interface props {
  isLoading: boolean;
  isError: any;
  options: Array<any>;
  loadingLabel: string;
  errorLabel: string;
  selectedOption: any;
  createMode: boolean;
  listProps: {
    /**choose to have a search box or not */
    filter: boolean;
    /** which fields in the array object would you like to search. example: ["heading", "content","tags"] */
    filterFields: Array<string>;
    optionValue?: string;
    /**label - the object field with the label */
    optionLabel: string;
    /**data key of the element. example: post_id */
    dataKey: string;
    /**"example: Press Tab to explore the post. To return, press escape and continue browsing other post in this list." */
    selectionMessage: string;
    /**"example: No post selected */
    emptySelectionMessage: string;
    /**Loading posts */
    emptyMessage: string;
    /**"No Posts Found. Try using post tags relating to the post"; */
    emptyFilterMessage: string;
    /**"{0} posts found. Use arrow keys to browse the result. " */
    filterMessage: string;
    /** "Search Post" */
    filterPlaceholder: string;
  };
}
const props = defineProps<props>();
const emits = defineEmits(["update-selection"]);
const {
  isLoading,
  isError,
  options,
  listProps,
  loadingLabel,
  errorLabel,
  selectedOption,
  createMode,
} = toRefs(props);

function updateSelection(val: any) {
  // console.log(`Updating Selection, emiting value`);
  emits("update-selection", val);
}
</script>
