<script lang="ts">
    import { current } from "../stores";

    function handleCreateStore(e: MouseEvent) {
        e.preventDefault()
        $current = "store-create"
    }

</script>


<button onclick={handleCreateStore}>Create Store</button>
<input type="text">

<style lang="scss">
    div {
        padding: 2rem;
        max-width: 400px;
        margin: 0 auto;
        display: flex;
        flex-direction: column;
        gap: 1rem;
        background: #fff;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    input {
        padding: 0.5rem;
        border: 1px solid #ccc;
        border-radius: 5px;
    }
    button {
        background: #28a745;
        color: white;
        padding: 0.5rem 1rem;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        &:hover {
            background: #218838;
        }
    }
</style>