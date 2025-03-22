<script lang="ts">
    import { user, api_url } from "../stores";

    let username = $state($user?.username || "");
    let email = $state($user?.email || "");

    async function updateSettings(e: SubmitEvent) {
        e.preventDefault();
        if(!$user){
                    throw new Error("User not available")
                }
        try {
            const response = await fetch(`${$api_url}/user/update`, {
                method: "PUT",
                body: JSON.stringify({ username, email }),
            });
            if (response.ok) {

                $user.username = username;
                $user.email = email;
                alert("Settings updated!");
            }
        } catch (error) {
            console.error("Error updating settings:", error);
        }
    }
</script>

<div class="settings-page">
    <h1>Settings</h1>
    <form onsubmit={updateSettings}>
        <input type="text" placeholder="Username" bind:value={username} required />
        <input type="email" placeholder="Email" bind:value={email} required />
        <button type="submit">Update Settings</button>
    </form>
</div>

<style lang="scss">
    .settings-page {
        padding: 2rem;
        max-width: 1200px;
        margin: 0 auto;
    }
    h1 {
        color: #242424;
        font-size: 2rem;
        margin-bottom: 1rem;
    }
    form {
        display: flex;
        flex-direction: column;
        gap: 1rem;
        max-width: 400px;
        background: #fff;
        padding: 1rem;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    input {
        padding: 0.5rem;
        border: 1px solid #ccc;
        border-radius: 5px;
    }
    button {
        background: #ffc107;
        color: #242424;
        padding: 0.5rem;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        &:hover {
            background: #e0a800;
        }
    }
</style>