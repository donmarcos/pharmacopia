<template>
    <div class="logout">
        <authenticator>
            <template v-slot="{ user, signOut }">
                <h1>Hello {{ user.username }}!</h1>
                <button @click="signOut">Sign Out</button>
            </template>
        </authenticator>
    </div>
</template>

<script>
import "@aws-amplify/ui-vue/styles.css";

export default {
    name: 'logout'
}
</script>
