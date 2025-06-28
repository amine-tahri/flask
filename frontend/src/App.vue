<template>
  <RouterView />
</template>

<script>
import { RouterView } from 'vue-router'
export default {
  name: 'LoginPage',
  components: {RouterView},
  data: () => ({
    valid: true,
    loginPassword: '',
    loginUsername: '',
    usernameRules: [(v) => !!v || 'Obligatoire'],
    rules: {
      required: (value) => !!value || 'Obligatoire.',
      min: (v) => (v && v.length >= 4) || 'Minimaux 4 caractères',
    },
  }),
  methods: {
    async validate() {
      this.$store
        .dispatch('login', {
          username: this.loginUsername,
          password: this.loginPassword,
        })
        .then(() => {
          this.$router.push('/').catch((error) => {
            if (error.name !== 'NavigationDuplicated') {
              throw error
            }
          })
        })
        .catch((error) => {
          console.log(error)
        })
    },
  },
}
</script>
