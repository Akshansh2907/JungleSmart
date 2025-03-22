<script lang="ts">
    import { api_url, user } from "../stores";
    import { onMount } from "svelte";
    let items = $state<{id:number, name:string, quantity:number}[]>([]);
    onMount(async () => {
        // Sample data
        items = [
            { id: 1, name: "Laptop", quantity: 10 },
            { id: 2, name: "Mouse", quantity: 50 },
        ];
        // Uncomment for real API
        // const response = await fetch(`${$api_url}/inventory`, { headers: { "Authorization": $user.token } });
        // items = await response.json();
    });
</script>

<div class="inventory-page">
    <h1>Inventory</h1>
    <table>
        <thead>
            <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Quantity</th>
            </tr>
        </thead>
        <tbody>
            {#each items as item}
                <tr>
                    <td>{item.id}</td>
                    <td>{item.name}</td>
                    <td>{item.quantity}</td>
                </tr>
            {/each}
        </tbody>
    </table>
</div>

<style lang="scss">
    .inventory-page {
        padding: 2rem;
        max-width: 1200px;
        margin: 0 auto;
    }
    h1 {
        color: #242424;
        font-size: 2rem;
        margin-bottom: 1rem;
    }
    table {
        width: 100%;
        border-collapse: collapse;
        background: #fff;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        border-radius: 8px;
    }
    th, td {
        padding: 1rem;
        text-align: left;
        border-bottom: 1px solid #ccc;
    }
    th {
        background: #28a745;
        color: white;
    }
</style>