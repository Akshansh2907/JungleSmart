<script lang="ts">
    import { page } from "../stores";
    import Icon from "@iconify/svelte";
</script>

<nav>
    <button onclick={() => $page = "analysis"}><Icon icon="material-symbols-light:analytics"/></button>
    <button onclick={() => $page = "inventory"}><Icon icon="material-symbols-light:warehouse"/></button>
    <button onclick={() => $page = "employees"}><Icon icon="material-symbols-light:account-child-invert"/></button>
    <button onclick={() => $page = "billing"}><Icon icon="material-symbols-light:list-alt"/></button>
    <button onclick={() => $page = "settings"}><Icon icon="material-symbols-light:settings"/></button>
</nav>

<style lang="scss">
    nav {
        display: flex;
        justify-content: space-around;
        padding: .5rem 1rem;
        background: #242424;
        border-radius: 10px;
    }
    button {
        background: none;
        border: none;
        color: white;
        font-size: 1.5rem;
        cursor: pointer;
        padding: 0.5rem;
        border-radius: 5px;
        &:hover {
            background: #007bff;
        }
    }
</style>