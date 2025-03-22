<script lang="ts">
    import { onMount,onDestroy } from "svelte";
    import { api_url } from "../stores";
    import Chart from "chart.js/auto"; // Import Chart.js

    // Sample data (replace with API fetch)
    let weeklySalesData = {
        labels: ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
        datasets: [{
            label: "Sales ($)",
            data: [120, 190, 300, 500, 200, 350, 400],
            borderColor: "#007bff",
            tension: 0.4,
            fill: false,
        }],
    };

    let categorySalesData = {
        labels: ["Electronics", "Clothing", "Food", "Books"],
        datasets: [{
            data: [300, 250, 150, 100],
            backgroundColor: ["#007bff", "#28a745", "#dc3545", "#ffc107"],
            hoverOffset: 4,
        }],
    };

    // Chart options
    const lineOptions = {
        responsive: true,
        scales: { y: { beginAtZero: true } },
    };

    const pieOptions = {
        responsive: true,
    };

    let lineChart: Chart;
    let pieChart: Chart;

    onMount(() => {
        // Initialize Line Chart
        const lineCtx = document.getElementById("weeklySalesChart") as HTMLCanvasElement;
        lineChart = new Chart(lineCtx, {
            type: "line",
            data: weeklySalesData,
            options: lineOptions,
        });

        // Initialize Pie Chart
        const pieCtx = document.getElementById("categorySalesChart") as HTMLCanvasElement;
        pieChart = new Chart(pieCtx, {
            type: "pie",
            data: categorySalesData,
            options: pieOptions,
        });

        // Fetch real data from API (uncomment and adjust as needed)
        /*
        (async () => {
            try {
                const response = await fetch(`${$api_url}/weekly_data`);
                const data = await response.json();
                weeklySalesData = {
                    labels: data.map(dt => dt["day"]),
                    datasets: [{
                        label: "Sales ($)",
                        data: data.map(dt => dt["sales"]),
                        borderColor: "#007bff",
                        tension: 0.4,
                        fill: false,
                    }],
                };
                lineChart.data = weeklySalesData;
                lineChart.update();

                const categoryResponse = await fetch(`${$api_url}/profitable_categories`);
                const categoryData = await categoryResponse.json();
                categorySalesData = {
                    labels: categoryData.map(dt => dt.category),
                    datasets: [{
                        data: categoryData.map(dt => dt.revenue),
                        backgroundColor: ["#007bff", "#28a745", "#dc3545", "#ffc107"],
                        hoverOffset: 4,
                    }],
                };
                pieChart.data = categorySalesData;
                pieChart.update();
            } catch (error) {
                console.error("Error fetching sales data:", error);
            }
        })();
        */
    });

    // Cleanup charts on component unmount
    onDestroy(() => {
        if (lineChart) lineChart.destroy();
        if (pieChart) pieChart.destroy();
    });
</script>

<div class="analysis-page">
    <h1>Sales Analysis</h1>
    <div class="chart-container">
        <h2>Weekly Sales</h2>
        <canvas id="weeklySalesChart" width="400" height="200"></canvas>
    </div>
    <div class="chart-container">
        <h2>Sales by Category</h2>
        <canvas id="categorySalesChart" width="400" height="200"></canvas>
    </div>
</div>

<style lang="scss">
    .analysis-page {
        padding: 2rem;
        display: flex;
        flex-direction: column;
        gap: 2rem;
        max-width: 1200px;
        margin: 0 auto;
        padding-bottom: 4rem;
    }
    .chart-container {
        background: #fff;
        padding: 1rem;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    h1 {
        color: #242424;
        font-size: 2rem;
    }
    h2 {
        color: #007bff;
        font-size: 1.5rem;
        margin-bottom: 1rem;
    }
    canvas {
        max-width: 100%;
    }
</style>