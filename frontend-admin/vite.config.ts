import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  server: {
    port: 5174,
    allowedHosts: ['mercha.kzelman.pl'],
    proxy: {
      '/api': process.env.VITE_API_URL || 'http://localhost:8000',
    },
  },
})
