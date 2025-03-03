<template>
  <nav>
    <!-- <router-link to="/">Home</router-link> |
    <router-link to="/about"></router-link> -->
    <menuSite></menuSite>
  </nav>
  <router-view/>
</template>
<script>
// @ is an alias to /src


import menuSite from '@/components/menuSite.vue';

export default {
  name: 'App',
  components: {
    menuSite
  },


}
</script>
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}



nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
