<script lang="ts">
    import LoginPage from "./LoginPage.svelte";
    import SignUpPage from "./SignUpPage.svelte";
    import StoreSelectPage from "./StoreSelectPage.svelte";
    import StoreCreatePage from "./StoreCreatePage.svelte";
    import { current } from "../stores";
  import HomePage from "./HomePage.svelte";
    
</script>

{#if $current === "login"}
    <LoginPage/>
{:else if $current === "signup"}
    <SignUpPage/>
{:else if $current === "store-select"}
    <StoreSelectPage/>
{:else if $current === "store-create"}
    <StoreCreatePage/>
{:else if $current === "default"}
    <HomePage/>
{/if}