<script lang="ts">
    import { user } from "../stores";
    import type { User } from "../types";
    import { current, api_url } from "../stores";

    let username = $state("");
    let password = $state("");
    let error = $state("");

    async function handleLogin(e: MouseEvent) {
        e.preventDefault()
        try {
            console.log(import.meta.env)
            const response = await fetch(`${$api_url}/auth/login`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ username, password }),
            })
            if (!response.ok) {
                throw new Error(`Couldn't login due to: ${response.headers}`)
            }
            $user = (await response.json()).user as User;
            $current = "default"
        } catch (error) {
            console.error("Error Loggin in:", error)
        }
    }

    async function handleSignUp(e: MouseEvent) {
        e.preventDefault()
        $current = "signup"
    }
</script>

<div class="login-page">
    <h1>Login</h1>
    <input type="text" bind:value={username} placeholder="Username" />
    <input type="password" bind:value={password} placeholder="Password" />
    <button onclick={handleLogin}>Login</button>
    <button onclick={handleSignUp}>SignUp</button>
    {#if error}
        <p class="error">{error}</p>
    {/if}
</div>

<style lang="scss">
    .login-page {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 1rem;
        padding: 2rem;
        max-width: 400px;
        margin: 0 auto;
        background: #fff;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    h1 {
        color: #242424;
        font-size: 2rem;
    }
    input {
        width: 100%;
        padding: 0.5rem;
        border: 1px solid #ccc;
        border-radius: 5px;
    }
    button {
        background: #007bff;
        color: white;
        padding: 0.5rem 1rem;
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
</style>