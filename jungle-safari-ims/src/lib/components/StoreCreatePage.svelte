<script lang="ts">
  import { user, api_url } from "../stores";
  import type { Store } from "../types";

    let errorMessage = $state("");
    let successMessage = $state("");
    
    let store_name = $state("");
    let address = $state("");

    async function createStore(e: SubmitEvent) {
e.preventDefault();
        errorMessage = "";
        successMessage = "";
        
            if (!$user) return;
        const storeData = { name: store_name, address, owner_id: $user?.id };

        try {
            const response = await fetch(`${$api_url}/create_store`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(storeData),
            });

            const result = await response.json();

            $user.store = result.store as Store;
            
            successMessage = "Signup successful!";
        } catch (error) {
            console.log("error: ", error)
        }

    }
</script>


<form onsubmit={createStore}>
    <input type="text" placeholder="Store Name" bind:value={store_name} required />
    <input type="text" placeholder="Address" bind:value={address} required />

    <button type="submit">Create Store</button>

    {#if errorMessage}
        <p class="error">{errorMessage}</p>
    {/if}
    {#if successMessage}
        <p class="success">{successMessage}</p>
    {/if}
</form>

<style lang="scss">
    form {
        display: flex;
        flex-direction: column;
        gap: 1rem;
        max-width: 400px;
        margin: 2rem auto;
        padding: 2rem;
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
        padding: 0.5rem;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        &:hover {
            background: #218838;
        }
    }
    .error {
        color: #dc3545;
    }
    .success {
        color: #28a745;
    }
</style>