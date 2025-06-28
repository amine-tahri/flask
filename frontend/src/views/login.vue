<template>
  <div class="login-container">
    <h2>Connexion</h2>
    <form @submit.prevent="validate">
      <input v-model="name" placeholder="Nom d'utilisateur" required />
      <input v-model="password" type="password" placeholder="Mot de passe" required />
      <button type="submit">Se connecter</button>
      <p v-if="error" class="error">{{ error }}</p>
    </form>
  </div>
</template>
<script>
export default {
  name: 'LoginPage',
  components: {},
  data: () => ({
    valid: true,
    name: '',
    password: '',
    usernameRules: [(v) => !!v || 'Obligatoire'],
    rules: {
      required: (value) => !!value || 'Obligatoire.',
      min: (v) => (v && v.length >= 4) || 'Minimaux 4 caractères',
    },
  }),
  methods: {
    async validate() {
      this.$store.dispatch('login', {
          name: this.name,
          password: this.password,
        })
        .then(() => {
          this.$router.push('/users').catch((error) => {
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

<style></style>
