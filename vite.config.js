import { defineConfig, loadEnv } from 'vite'
import vue from '@vitejs/plugin-vue'
import plugin, { Mode } from 'vite-plugin-markdown'

export default defineConfig(({ command, mode }) => {
  const env = loadEnv(mode, process.cwd(), '')
  return {
    plugins: [vue()],
    define: {
      __GIST_HASH__ : {
        value: env.GIST_HASH
      }
    }
  }
})

module.exports = {
  plugins: [vue(), plugin({ mode: [Mode.HTML, Mode.TOC, Mode.VUE] })]
}