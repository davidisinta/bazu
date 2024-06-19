<template>
  <div class="min-h-screen w-full">
    <div class="w-[90%] mx-auto pt-4">
      <button @click="interviewMode = !interviewMode">
        {{ interviewMode ? "Stop" : "Start" }}
      </button>
    </div>
    <div class="grid grid-cols-4 h-screen w-[90%] mx-auto">
      <div class="col-span-1 pt-4">
        <h3>
          AI Audio
          <button
            @click="isAudioOn = !isAudioOn"
            :class="`${isAudioOn ? 'bg-green-400' : 'bg-red-600'}`"
          >
            {{ isAudioOn ? "On" : "Off" }}
            <Icon
              :name="`${
                isAudioOn ? 'iconoir:voice-check' : 'iconoir:voice-xmark'
              }`"
              size="32"
            />
          </button>
        </h3>

        <div class="my-2">AI questions populated here:</div>
        <div class="my-2">User here: {{ result }}</div>
      </div>
      <div class="col-span-2 flex gap-4 flex-col h-full p-2">
        <div
          class="bg-white h-[60%] rounded-lg border-2 border-gray-400 grid place-items-center"
        >
          <p>User Video Here</p>
        </div>
        <Inputbox placeholder="Type Something" @submit="submitAnswer" v-model="input">
         <span class="px-3 py-2 rounded-lg  text-sky-800 font-bold h-fit" @click="controlSpeech">
            <Icon
              :name="`${
                isListening
                  ? 'ic:round-settings-voice'
                  : 'ic:round-keyboard-voice'
              }`"
              size="32"
            />
            </span class="">
           <template #submitIcon> 
              <Icon name="mdi:send-outline" size="32" />
           </template>
        </Inputbox>
      </div>
      <div class="col-span-1">
        <span>Time: {{ timeSpent }}</span>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
const interviewMode = ref(false);
const isAudioOn = ref(false);
const timeSpent = ref(0);
const speech = useSpeechRecognition({
  lang: "en-US",
  continuous: true,
  interimResults: true,
});
const input=ref('')
const { isListening, result, start, stop, isSupported, isFinal, error } =
  speech;
const { pause, resume, isActive } = useIntervalFn(
  () => {
    timeSpent.value += 1;
  },
  1000,
  { immediate: false }
);

function submitAnswer(){

}

function controlSpeech() {
  result.value = "";
  if (isListening.value) {
    stop();
  } else {
    start();
  }
}
watchEffect(() => {
  console.log(`Is listening`, isListening.value);
});

watchEffect(() => {
  if (interviewMode.value) {
    resume();
  } else {
    pause();
  }
});
</script>

<style scoped></style>
