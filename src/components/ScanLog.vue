<template>
  <div class="bg-white dark:bg-opacity-10 backdrop-filter backdrop-blur-lg rounded-lg shadow p-4 h-full flex flex-col">
    <h2 class="text-lg font-semibold mb-2 text-purple-800 dark:text-purple-100">Scan Log</h2>
    <div class="flex-grow overflow-auto">
      <table class="min-w-full divide-y divide-gray-200 dark:divide-gray-700">
        <thead class="bg-gray-50 dark:bg-gray-800">
          <tr>
            <th class="px-3 py-2 text-left text-xs font-medium text-gray-500 dark:text-gray-300 uppercase tracking-wider">File Name</th>
            <th class="px-3 py-2 text-left text-xs font-medium text-gray-500 dark:text-gray-300 uppercase tracking-wider">Status</th>
            <th class="px-3 py-2 text-left text-xs font-medium text-gray-500 dark:text-gray-300 uppercase tracking-wider">Date</th>
          </tr>
        </thead>
        <tbody class="bg-white dark:bg-gray-900 divide-y divide-gray-200 dark:divide-gray-700">
          <tr v-for="log in scanLogs" :key="log.filename">
            <td class="px-3 py-2 whitespace-nowrap text-xs text-gray-900 dark:text-gray-300">{{ log.filename }}</td>
            <td class="px-3 py-2 whitespace-nowrap text-xs text-gray-900 dark:text-gray-300">{{ log.status }}</td>
            <td class="px-3 py-2 whitespace-nowrap text-xs text-gray-900 dark:text-gray-300">{{ log.date }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>


<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const scanLogs = ref([])

const fetchScanLogs = async () => {
  try {
    const response = await axios.get('http://localhost:5000/api/scan_log')
    scanLogs.value = response.data
  } catch (error) {
    console.error('Error fetching scan logs:', error)
  }
}

onMounted(fetchScanLogs)
</script>