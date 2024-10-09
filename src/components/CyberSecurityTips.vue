<template>
  <div class="bg-white dark:bg-opacity-10 backdrop-filter backdrop-blur-lg rounded-lg shadow p-4 h-full flex flex-col">
    <h2 class="text-lg font-semibold mb-2 text-purple-800 dark:text-purple-100 text-center">Cybersecurity Tip</h2> <!-- Centered the title -->
    <p class="text-base text-gray-800 dark:text-gray-200 flex-grow text-center">{{ currentTip }}</p> <!-- Centered the content text -->
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import axios from 'axios'

const currentTip = ref('')

const fetchTip = async () => {
  try {
    const response = await axios.get('http://localhost:5000/api/tips')
    if (response.data && response.data.length > 0) {
      const randomIndex = Math.floor(Math.random() * response.data.length)
      currentTip.value = response.data[randomIndex]
    }
  } catch (error) {
    console.error('Error fetching tip:', error)
    currentTip.value = 'Always keep your software and systems up to date.'
  }
}

onMounted(() => {
  fetchTip()
  const interval = setInterval(fetchTip, 60000) // Fetch a new tip every minute
  onUnmounted(() => clearInterval(interval))
})
</script>
