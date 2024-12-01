<template>
  <div id="app">
    <router-view />
  </div>
</template>

<script>
  import Index from '@/components/Index.vue'

  export default {
    name: 'App',
    components: {
      Index
    },
    data() {
      return {
      }
    }
  }
</script>
