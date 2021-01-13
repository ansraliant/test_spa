<template>
  <h2>This is the response from the backend: {{ message }}</h2>
</template>

<script>
import axios from "axios"

export default {
  name: "Page1",
  data: function() {
    return {
      message: "Nothing Yet"
    }
  },
  async beforeMount() {
    let $axios = axios.create({
        baseURL: "/api/",
        headers: { "Content-Type": "application/json" }
    })
    await $axios.get("users").then(response => {
      this.message = response.data.msg
    })
  }
}
</script>