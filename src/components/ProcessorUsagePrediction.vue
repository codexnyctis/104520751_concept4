<template>
  <div class="bg-white dark:bg-opacity-10 backdrop-filter backdrop-blur-lg rounded-lg shadow p-4 h-full flex flex-col">
    <h2 class="text-lg font-semibold mb-2 text-purple-800 dark:text-purple-100">Processor Usage Prediction</h2>
    <div class="flex items-center space-x-2 mb-2">
      <div>
        <label for="start-date" class="block text-xs font-medium text-gray-700 dark:text-gray-300">Start Date:</label>
        <input id="start-date" type="date" v-model="startDate" class="mt-1 block w-full text-xs rounded-md border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-700 text-gray-900 dark:text-gray-100 focus:border-purple-500 focus:ring focus:ring-purple-500 focus:ring-opacity-50">
      </div>
      <div>
        <label for="end-date" class="block text-xs font-medium text-gray-700 dark:text-gray-300">End Date:</label>
        <input id="end-date" type="date" v-model="endDate" class="mt-1 block w-full text-xs rounded-md border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-700 text-gray-900 dark:text-gray-100 focus:border-purple-500 focus:ring focus:ring-purple-500 focus:ring-opacity-50">
      </div>
      <button @click="handlePredict" class="px-3 py-1 bg-purple-600 text-white rounded-md hover:bg-purple-700 mt-5 text-sm">Predict</button>
    </div>
    <div v-if="error" class="text-red-500 text-sm mb-2">{{ error }}</div>
    <div class="flex-grow">
      <img v-if="plotData" :src="'data:image/png;base64,' + plotData" alt="Processor Usage Prediction" class="w-full h-full object-contain" />
      <Line v-else-if="chartData" :data="chartData" :options="chartOptions" />
      <div v-if="predictionData" class="mt-4">
        <h3 class="text-lg font-semibold mb-2 text-purple-800 dark:text-purple-100">Prediction Results</h3>
        <ul>
          <li v-for="(result, index) in predictionData" :key="index">
            <strong>{{ result.label }}:</strong> {{ result.value }}
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import axios from 'axios'
import { Line } from 'vue-chartjs'
import { Chart as ChartJS, CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend } from 'chart.js'

ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend)

const startDate = ref('')
const endDate = ref('')
const predictionData = ref(null)
const error = ref(null)
const plotData = ref(null)

const handlePredict = async () => {
  error.value = null
  plotData.value = null
  try {
    const response = await axios.post('http://localhost:5000/predict', { start_date: startDate.value, end_date: endDate.value })
    if (response.data.error) {
      error.value = response.data.error
    } else {
      predictionData.value = response.data.prediction_results
      plotData.value = response.data.plot
    }
  } catch (err) {
    console.error('Error predicting processor usage:', err)
    error.value = 'An error occurred while predicting processor usage.'
  }
}

const chartData = computed(() => {
  if (!predictionData.value || !predictionData.value.timestamps) return null
  
  return {
    labels: predictionData.value.timestamps,
    datasets: [
      {
        label: 'Actual',
        data: predictionData.value.actual,
        borderColor: '#6200EE',
        backgroundColor: 'rgba(98, 0, 238, 0.1)',
        fill: true,
      },
      {
        label: 'Predicted',
        data: predictionData.value.predicted,
        borderColor: '#03DAC6',
        backgroundColor: 'rgba(3, 218, 198, 0.1)',
        fill: true,
      },
    ],
  }
})

const chartOptions = {
  responsive: true,
  maintainAspectRatio: false,
  scales: {
    y: {
      beginAtZero: true,
      title: {
        display: true,
        text: 'Usage (%)',
        color: 'rgb(229, 231, 235)',
        font: { size: 12 }
      },
      ticks: {
        color: 'rgb(229, 231, 235)',
        font: { size: 10 }
      }
    },
    x: {
      title: {
        display: true,
        text: 'Timestamp',
        color: 'rgb(229, 231, 235)',
        font: { size: 12 }
      },
      ticks: {
        color: 'rgb(229, 231, 235)',
        font: { size: 10 }
      }
    }
  },
  plugins: {
    legend: {
      labels: {
        color: 'rgb(229, 231, 235)',
        font: { size: 12 }
      }
    }
  }
}
</script>