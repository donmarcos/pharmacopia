<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/pharmacopialogo.png">
    <amplify-sign-out></amplify-sign-out>
  </div>
  <div>
    <VueSidebarMenuAkahon 
     menuTitle="pharmacopia"
     bgColor ="#4F9F60"
     profileName="Patient John Q"
     profileRole=""
    />
  </div>
</template>

<script>
import VueSidebarMenuAkahon from "vue-sidebar-menu-akahon";


export default {
  name: 'Home',
  components: {
    VueSidebarMenuAkahon
  }
}
</script>
