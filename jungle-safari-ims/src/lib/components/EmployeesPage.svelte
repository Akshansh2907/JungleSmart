<script lang="ts">
    import { api_url, user } from "../stores";
    import { onMount } from "svelte";

    let employees = $state<{id: number, name:string, role:string}[]>([]);
    onMount(async () => {
        // Sample data
        employees = [
            { id: 1, name: "John Doe", role: "Manager" },
            { id: 2, name: "Jane Smith", role: "Cashier" },
        ];
        // Uncomment for real API
        // const response = await fetch(`${$api_url}/employees`, { headers: { "Authorization": $user.token } });
        // employees = await response.json();
    });
</script>

<div class="employees-page">
    <h1>Employees</h1>
    <table>
        <thead>
            <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Role</th>
            </tr>
        </thead>
        <tbody>
            {#each employees as employee}
                <tr>
                    <td>{employee.id}</td>
                    <td>{employee.name}</td>
                    <td>{employee.role}</td>
                </tr>
            {/each}
        </tbody>
    </table>
</div>

<style lang="scss">
    .employees-page {
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
        background: #dc3545;
        color: white;
    }
</style>