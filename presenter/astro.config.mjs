import { defineConfig } from "astro/config";
import tailwindcss from "@tailwindcss/vite";
import { watchExternalMarkdown } from "./src/integrations/watch-external-md.ts";

export default defineConfig({
  output: "static",
  integrations: [watchExternalMarkdown()],
  vite: {
    plugins: [tailwindcss()],
  },
});
