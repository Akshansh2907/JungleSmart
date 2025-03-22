<script lang="ts">
    import { api_url, user } from "../stores";
    import { onMount } from "svelte";

    let invoices = $state<{ id: number, amount: number, date: string}[]>([]);
    onMount(async () => {
        // Fetch invoices (sample data here)
        invoices = [
            { id: 1, amount: 150, date: "2025-03-20" },
            { id: 2, amount: 200, date: "2025-03-19" },
        ];
        // Uncomment for real API
        // const response = await fetch(`${$api_url}/billing`, { headers: { "Authorization": $user.token } });
        // invoices = await response.json();
    });

    const bill_data ={
  customer_name: "Akshansh Khairwar",
  customer_email: "akshanshkhairwar@gmail.com",
  items: [
    {
        name: "T-Shirt",
        quantity: 1,
        price: 799,
        hsn_code: "40141010",
    }, 
    {
        name: "Keyring",
        quantity: 2,
        price: 80,
        hsn_code: "1241512",
    }
  ]
}

    async function handleInvoiceCreate(e: MouseEvent) {
        e.preventDefault()
        await fetch(`${$api_url}/invoice/generate-invoice/`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(bill_data),
        })
    } 
</script>

<div class="billing-page">
    <h1>Billing</h1>
    <table>
        <thead>
            <tr>
                <th>ID</th>
                <th>Amount ($)</th>
                <th>Date</th>
            </tr>
        </thead>
        <tbody>
            {#each invoices as invoice}
                <tr>
                    <td>{invoice.id}</td>
                    <td>{invoice.amount}</td>
                    <td>{invoice.date}</td>
                </tr>
            {/each}
        </tbody>
    </table>
    <button onclick={handleInvoiceCreate}>Create Invoice</button>
</div>

<style lang="scss">
    .billing-page {
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
        background: #007bff;
        color: white;
    }
    button {
        width: 100%;
        margin: 0.5em .15em;
        border:none;
        outline: none;
        cursor: pointer;
        background: #007bff;
        padding: 1em 2em;
        color: white;
        font-weight: bold;
        border-radius: 3px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
</style>