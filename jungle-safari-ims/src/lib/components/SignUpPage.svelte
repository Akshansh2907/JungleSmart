<script lang="ts">
    import { current, user, api_url } from "../stores";
    import type { User } from "../types";
    
    let full_name = $state("");
    let username = $state("");
    let contact_no = $state("");
    let email = $state("");
    let password = $state("");
    let errorMessage = $state("");
    let successMessage = $state("");

    async function signup(e: SubmitEvent) {
        e.preventDefault();
        errorMessage = "";
        successMessage = "";

        const userData = { full_name, username, contact_no, email, password };

        try {
            const response = await fetch(`${$api_url}/auth/signup`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(userData),
            });

            const result = await response.json();

            $user = result.user as User;
            $current = "store-select";

            successMessage = "Signup successful!";
        } catch (error) {
            console.log("error: ", error)
        }
    }
</script>

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
        background: #007bff;
        color: white;
        padding: 0.5rem;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        &:hover {
            background: #0056b3;
        }
    }
    .error {
        color: #dc3545;
    }
    .success {
        color: #28a745;
    }
</style>

<form onsubmit={signup}>
    <input type="text" placeholder="Full Name" bind:value={full_name} required />
    <input type="text" placeholder="Username" bind:value={username} required />
    <input type="text" placeholder="Contact No" bind:value={contact_no} required />
    <input type="email" placeholder="Email" bind:value={email} required />
    <input type="password" placeholder="Password" bind:value={password} required />
    <button type="submit">Sign Up</button>

    {#if errorMessage}
        <p class="error">{errorMessage}</p>
    {/if}
    {#if successMessage}
        <p class="success">{successMessage}</p>
    {/if}
</form>
