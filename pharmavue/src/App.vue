<template>
  
  <div id="nav">
    <VueSidebarMenuAkahon 
      menuTitle="pharmacopia"
      :menuItems="navItems"
      bgColor ="#4F9F60"
      profileName="Patient John Q"
      profileRole="Sample"
    />
  </div>

  <router-view/>
</template>

<script>
import VueSidebarMenuAkahon from "vue-sidebar-menu-akahon";
import navItems from "./components/NavBarItems";
  
export default {
  name: "App",
  components: {
    VueSidebarMenuAkahon
  },
  data () {
    return {
      navItems: navItems
    }
  }
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

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
