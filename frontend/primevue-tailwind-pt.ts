import Tailwind from "primevue/passthrough/tailwind";
import { usePassThrough } from "primevue/passthrough";
const TRANSITIONS = {
  overlay: {
    enterFromClass: "opacity-0 scale-75",
    enterActiveClass:
      "transition-transform transition-opacity duration-150 ease-in",
    leaveActiveClass: "transition-opacity duration-150 ease-linear",
    leaveToClass: "opacity-0",
  },
};

const PrimevueTailwindPT = usePassThrough(
  Tailwind,
  {},
  { mergeSections: true, mergeProps: false }
);

export default PrimevueTailwindPT;
