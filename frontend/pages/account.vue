<template>
  <div class="flex flex-col h-[90vh] w-full">
    <div class="h-[20%] px-5 flex items-center">
      <div class="w-[20%] h-full grid place-items-center">
        <PrimeAvatar
          size="xlarge"
          icon="pi pi-user"
          aria-label="Profile Badge"
          :pt="{}"
        />
      </div>
      <div class="grid grid-cols-2 grid-rows-2 gap-0 h-1/2">
        <AccountDetail
          detail="Name"
          :value="`${name.first_name + ` ` + name.last_name}`"
        />
        <AccountDetail detail="Email" :value="email" />
        <AccountDetail detail="Profession" :value="profession" />
        <AccountDetail detail="Organization" :value="organization" />
      </div>
    </div>
    <hr class=" bg-sky-700 h-[2px]"/>
    <div class="h-[35%] pt-4 w-[80%] grid grid-cols-3 mx-auto">
      <AccountComponent title="Interviews">
        <span class="font-bold text-2xl">{{ interviews }}</span>
      </AccountComponent>
      <AccountComponent title="Overall Rating">
        <span class="font-bold text-2xl">{{ interviewRating }}</span>
      </AccountComponent>
      <AccountComponent title="Metrics">
        <div class="w-full my-2">
          <span>Confidence: </span
          ><span class="font-semibold">{{ metrics.confidence }}</span>
        </div>
        <div class="w-full my-2">
          <span>Brevity: </span
          ><span class="font-semibold">{{ metrics.brevity }}</span>
        </div>
        <div class="w-full my-2">
          <span>Fluency: </span>
          <span class="font-semibold"> {{ metrics.fluency }}</span>
        </div>
      </AccountComponent>
    </div>
  </div>
</template>

<script setup lang="ts">
const name = ref({ first_name: "Ron", last_name: "Pile" });
const email = ref("ron.pile@yale.edu");
const profession = ref("Computer Science");
const organization = ref("Yale University");

const initials = computed(
  () => `${name.value.first_name[0] + name.value.last_name[0]}`
);
const interviews = ref(25);
const interviewRating = ref(3.5);
const metrics = ref({
  confidence: 0.5,
  brevity: 0.8,
  fluency: 1,
});
</script>
