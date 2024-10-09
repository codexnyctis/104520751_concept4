<template>
  <div :class="{'dark': darkMode}" class="min-h-screen">
    <div class="space-background p-4 min-h-screen">
      <header class="flex justify-between items-center mb-4">
        <h1 class="text-2xl font-bold text-purple-800 dark:text-purple-100">System Analytics Dashboard</h1>
      </header>
      <main class="grid grid-cols-3 gap-4 h-[calc(100vh-6rem)]">
        <div class="space-y-4 flex flex-col">
          <CyberSecurityTips class="flex-grow" style="height: 300px; overflow: hidden;"/>
          <ScanLog class="flex-grow" />
        </div>
        <div class="space-y-4 flex flex-col">
          <FileUpload class="flex-grow" @classificationResults="handleClassificationResults" />
          <MalwareDistribution :distribution="malwareDistribution" class="flex-grow" />
        </div>
        <div class="space-y-4 flex flex-col">
          <ProcessorUsagePrediction class="flex-grow" />
          <MalwareFamilyDistribution :results="classificationResults" class="flex-grow" />
        </div>
      </main>
    </div>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue'
import CyberSecurityTips from './components/CyberSecurityTips.vue'
import FileUpload from './components/FileUpload.vue'
import ScanLog from './components/ScanLog.vue'
import MalwareDistribution from './components/MalwareDistribution.vue'
import ProcessorUsagePrediction from './components/ProcessorUsagePrediction.vue'
import MalwareFamilyDistribution from './components/MalwareFamilyDistribution.vue'

const darkMode = ref(true)
const classificationResults = ref([])
const malwareDistribution = ref({})

const toggleDarkMode = () => {
  darkMode.value = !darkMode.value
}

const handleClassificationResults = (results) => {
  classificationResults.value = results.classification_results
  
  // Calculate malware distribution for the pie chart
  const distribution = results.classification_results.reduce((acc, result) => {
    acc[result['Predicted Class']] = (acc[result['Predicted Class']] || 0) + 1
    return acc
  }, {})
  malwareDistribution.value = distribution
}

watch(darkMode, (newValue) => {
  if (newValue) {
    document.documentElement.classList.add('dark')
  } else {
    document.documentElement.classList.remove('dark')
  }
}, { immediate: true })
</script>

<style>
.space-background {
  background: linear-gradient(to bottom, #0f0c29, #302b63, #24243e);
  position: relative;
  overflow: hidden;
}

.space-background::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-image: 
    radial-gradient(white, rgba(255,255,255,.2) 2px, transparent 40px),
    radial-gradient(white, rgba(255,255,255,.15) 1px, transparent 30px),
    radial-gradient(white, rgba(255,255,255,.1) 2px, transparent 40px);
  background-size: 550px 550px, 350px 350px, 250px 250px;
  background-position: 0 0, 40px 60px, 130px 270px;
  animation: twinkle 10s linear infinite;
}

@keyframes twinkle {
  0% { transform: translateY(0); }
  100% { transform: translateY(-550px); }
}

/* Light mode styles */
:root:not(.dark) .space-background {
  background: #f3e8ff;
}

:root:not(.dark) .space-background::before {
  opacity: 0;
}
</style>