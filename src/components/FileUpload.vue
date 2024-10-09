<template>
  <div class="bg-white dark:bg-opacity-10 backdrop-filter backdrop-blur-lg rounded-lg shadow p-4 h-full flex flex-col">
    <h2 class="text-lg font-semibold mb-2 text-purple-800 dark:text-purple-100">UPLOAD A FILE</h2>
    <div class="flex-grow flex items-center justify-center w-full">
      <label for="dropzone-file" class="flex flex-col items-center justify-center w-full h-24 border-2 border-gray-300 dark:border-gray-600 border-dashed rounded-lg cursor-pointer bg-gray-50 dark:bg-gray-700 hover:bg-gray-100 dark:hover:bg-gray-600">
        <div class="flex flex-col items-center justify-center pt-5 pb-6">
          <svg class="w-8 h-8 mb-2 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12"></path></svg>
          <p class="mb-1 text-sm text-gray-500 dark:text-gray-400"><span class="font-semibold">Click to upload</span> or drag and drop</p>
          <p class="text-xs text-gray-500 dark:text-gray-400">.CSV file only</p>
        </div>
        <input id="dropzone-file" type="file" class="hidden" @change="handleFileChange" accept=".csv" />
      </label>
    </div>
    <div class="mt-4 flex items-center space-x-4">
      <button @click="handleUploadAndClassify" class="px-4 py-2 bg-purple-600 text-white rounded-md hover:bg-purple-700 text-sm" :disabled="!file || isUploading">
        {{ isUploading ? 'Uploading & Classifying...' : 'Upload & Classify' }}
      </button>
      <div v-if="isUploading" class="flex-grow">
        <div class="w-full bg-gray-200 rounded-full h-2.5 dark:bg-gray-700">
          <div class="bg-purple-600 h-2.5 rounded-full" :style="{ width: `${uploadProgress}%` }"></div>
        </div>
        <p class="text-xs text-gray-600 dark:text-gray-300 mt-1">{{ uploadProgress }}% Uploaded</p>
      </div>
      <button @click="handleDownloadTemplate" class="px-4 py-2 bg-green-500 text-white rounded-md hover:bg-green-600 flex items-center text-sm">
        <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"></path></svg>
        Download template
      </button>
    </div>
    <p class="mt-2 text-xs text-gray-600 dark:text-gray-300">{{ uploadStatus }}</p>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

const file = ref(null)
const uploadStatus = ref('')
const isUploading = ref(false)
const uploadProgress = ref(0)
const emit = defineEmits(['classificationResults'])

const handleFileChange = (event) => {
  file.value = event.target.files[0]
}

const handleUploadAndClassify = async () => {
  if (!file.value) {
    uploadStatus.value = 'Please select a file first.'
    return
  }

  const formData = new FormData()
  formData.append('file', file.value)

  isUploading.value = true
  uploadProgress.value = 0

  try {
    const response = await axios.post('http://localhost:5000/classify', formData, {
      headers: { 'Content-Type': 'multipart/form-data' },
      onUploadProgress: (progressEvent) => {
        uploadProgress.value = Math.round((progressEvent.loaded * 100) / progressEvent.total)
      }
    })
    uploadStatus.value = 'File uploaded and classified successfully!'
    emit('classificationResults', response.data)
  } catch (error) {
    uploadStatus.value = 'Error uploading or classifying file. Please try again.'
    console.error('Error:', error)
  } finally {
    isUploading.value = false
  }
}

const handleDownloadTemplate = () => {
  // Implement template download logic here
}
</script>