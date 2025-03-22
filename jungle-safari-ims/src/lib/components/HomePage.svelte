<script lang="ts">
    import { page } from "../stores";
    import AnalysisPage from "./AnalysisPage.svelte";
    import BillingPage from "./BillingPage.svelte";
    import EmployeesPage from "./EmployeesPage.svelte";
    import InventoryPage from "./InventoryPage.svelte";
    import Navigation from "./Navigation.svelte";
    import SettingsPage from "./SettingsPage.svelte";
</script>
<main>
    <div class="navigation">
        <Navigation/>
    </div>
    
    
    {#if $page === "analysis"}
        <div>
            <AnalysisPage/>
        </div>
    {:else if $page == "billing"}
        <div>
            <BillingPage/>
        </div>
    {:else if $page == "employees"}
        <div>
            <EmployeesPage/>
        </div>
    {:else if $page == "inventory"}
        <div>
            <InventoryPage/>
        </div>
    {:else if $page == "settings"}
        <div>
            <SettingsPage/>
        </div>
    {/if}
</main>


<style lang="scss">
    main {
        position: relative;
    }
    .navigation {
        position: fixed;
        bottom: 10px;
        left: 10px;
        right: 10px;
    }

</style>