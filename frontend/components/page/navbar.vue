<template>
  <header
    class="w-full h-[90px] bg-white dark:bg-slate-700 border-b border-sky-500 sticky top-0 z-40"
    role="banner"
  >
    <PrimeMenubar
      aria-label="Main Navigation"
      :model="menu"
      class="w-full gap-3 items-center overflow-y h-[90px]"
      :pt="{
        menuitem: ({ context }) => ({
          class: [
            '  text-black  dark:text-white hover:rounded-lg hover:text-white hover:bg-sky-600 h-fit mt-auto',
            {
              'bg-sky-500 text-white rounded-lg': context.active,
              'bg-sky-600 text-white rounded-lg ': context.focused,
            },
          ],
          'aria-current': `${
            isCurrentPath(context.item.item.route ?? context.item.item.url)
              ? 'page'
              : 'false'
          }`,
        }),
        icon: ({ context }) => ({
          class: [
            'text-sky-700 dark:text-white text-3xl mr-1 ',
            {
              'text-white': context.focused,
              'text-white ': context.active,
            },
          ],
        }),

        menu: 'flex justify-around gap-5 h-[60px] mt-auto  outline-none focus-within:border-2 border-b-0 border-sky-500 rounded-t-lg',
        root: 'flex justify-between max-w-[1280px]  mx-auto  ',
        end: 'w-[90px] !ml-0 mr-[30px] ',
        label: 'font-semibold w-fit pr-2 text-lg ',
        submenu:
          'w-max bg-white dark:bg-slate-800 text-black  rounded-b-lg border-2 border-solid border-sky-800 border-t-0 mt-0',
        content: 'w-fit',
      }"
    >
      <template #start>
        <NuxtLink
          to="/"
          class="w-[200px] h-fit flex gap-[5px] items-center ml-3"
        >
          <img
            class="m-2 mb-3 mr-1 h-16 w-fit "
            :src="Logo"
            alt="Bazu Logo"
            aria-hidden="true"
          />
          <h1 class="font-bold text-2xl dark:text-white">InterviewMe</h1>
        </NuxtLink>
      </template>
      <template
        #item="{ label, item, hasSubmenu, props, root }"
        aria-current="false"
      >
        <NuxtLink
          v-if="item.route"
          v-slot="routerProps"
          :to="item.route"
          custom
        >
          <a
            :href="routerProps.href"
            v-bind="props.action"
            class="group px-4 pt-2"
            :class="[
              {
                'border-b-4 rounded-b-sm border-sky-700 dark:border-white':
                  isCurrentPath(item.route),
              },
            ]"
            @click="(e:Event) => {
                //using navigateTo() rather than default link behaviour because it flashes every time rather than change browser location
              //  console.log('preventing default href behaviour')
                e.preventDefault()
                if(!hasSubmenu){ 
                  navigateTo(`${routerProps.href}`
                )}
                
                }"
          >
            <span
              v-bind="props.icon"
              class="group-hover:text-white group-active:text-white"
            ></span>
            <span
              v-bind="props.label"
              class="group-hover:text-white group-active:text-white"
              >{{ label }}</span
            >
            <span
              :class="[
                hasSubmenu &&
                  (root ? 'pi pi-fw pi-angle-down' : 'pi pi-fw pi-angle-right'),
              ]"
              v-bind="props.submenuicon"
            ></span>
          </a>
        </NuxtLink>

        <a
          v-else
          :href="item.url"
          :target="item.target"
          v-bind="props.action"
          :class="[
            `group/${groupName(item.label)}`,
            {
              'border-l-8 rounded-l-none   border-sky-700': isCurrentPath(
                item.url
              ),
            },
          ]"
          class="px-4 pt-2"
          @click="(e:Event) => {
              
                e.preventDefault()
                if(!hasSubmenu){ 
                  navigateTo(`${item.url}`
                )}
                
                }"
        >
          <span
            v-bind="props.icon"
            :class="`group-hover/${groupName(
              item.label
            )}:text-white   group-active/${groupName(item.label)}:!text-white`"
          ></span>
          <span
            v-bind="props.label"
            :class="`group-hover/${groupName(item.label)}:text-white `"
            >{{ label }}</span
          >
          <span
            :class="[
              hasSubmenu &&
                (root ? 'pi pi-fw pi-angle-down' : 'pi pi-fw pi-angle-right'),
            ]"
            v-bind="props.submenuicon"
          ></span>
        </a>
      </template>
      <template #end>
        <div aria-hidden="true">
          <button @click="toggleDark()" tabindex="-1">
            {{ isDarkMode ? "Light" : "Dark" }}
            <span
              :class="[
                isDarkMode
                  ? 'icon--mdi icon--mdi--white-balance-sunny'
                  : 'icon--mdi icon--mdi--weather-night',
                'text-blue',
              ]"
            ></span>
          </button>
        </div>
      </template>
    </PrimeMenubar>
  </header>
</template>

<script setup lang="ts">
import Logo from "../../assets/logo/bazu.png";
import { useToggle, useDark } from "@vueuse/core";

const isDarkMode = useDark();
const toggleDark = useToggle(isDarkMode);
const isFocused = ref(false);
const menu = ref([
  {
    label: "Past Interviews",
    icon: "iconify mdi--record-player",
    route: "/past-interviews",
  },
  {
    label: "Prep",
    icon: "iconify game-icons--read",
    route: "/prep",
  },
  {
    label: "Profile",
    // icon: "icon--mdi-light icon--mdi-light--account",
    icon:'iconify mdi--account',
    route: "/account",
  },
]);

type menuLabel = string | undefined | ((...args: any) => string);

function groupName(label: menuLabel) {
  let stringified = label as string;
  let regex = /\s+/g;
  let dashString = stringified.replace(regex, "_");
  return dashString;
}

const route = useRoute();

type itemRoute = string | undefined;

function isCurrentPath(label: itemRoute) {
  let stringified = (label as string).toLocaleLowerCase();
  //since the route here can be shorter than the argument proovided route, i.e when the route has a hash link, I have sliced the provided route to the first two charaters only
  if (route.path.includes(stringified)) {
    //  console.log(route.path, "contains", stringified);
    return true;
  }
  //  console.log(route.path, "doesn't contain", stringified);

  return false;
}

</script>
