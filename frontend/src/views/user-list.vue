<template>
  <main>
    <h1>User list</h1>
    <li v-for="user in [1, 2, 3]" :key="user">
      {{ user }}
    </li>
  </main>
</template>
<script>
import { mapGetters } from 'vuex'

export default {
  name: 'UserList',

  data() {
    return {}
  },
  computed: {
    ...mapGetters(['users']),
  },

  mounted() {
    this.$store.dispatch('fetchUsers')
  },
  methods: {},
}
</script>
