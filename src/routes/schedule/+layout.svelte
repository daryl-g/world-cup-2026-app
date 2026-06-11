<script lang="ts">
    import { goto } from '$app/navigation';
    import { page } from '$app/state';
    let { children } = $props();
</script>

<style>
    .schedule-container {
        background-image: url('$lib/assets/img/page_bg.png');
        background-size: cover;
        background-position: center;
        min-height: 91.8vh;
    }

    .schedule-content {
        padding: 2rem;
        color: white;
    }

    .schedule-tabs {
        display: flex;
        gap: 0.5rem;
        justify-content: center;
        border-bottom: 3px solid rgba(255, 255, 255, 0.7);
    }

    .schedule-tabs button {
        background: rgba(255, 255, 255);
        border: none;
        border-radius: 10px 10px 0 0;
        padding: 0.5rem 1.25rem;
        color: black;
        font-family: 'Inter', sans-serif;
        font-size: 1.2rem;
        font-weight: bold;
        cursor: pointer;
        transition: background 0.3s;
    }

    .schedule-tabs button.active,
    .schedule-tabs button:hover {
        background: rgba(0, 0, 0, 0.7);
        color: white;
    }
</style>

<div class="schedule-container">
    <div class="schedule-content">
        <div class="schedule-tabs">
            <button onclick={() => goto('/schedule/groups')} class:active={page.url.pathname === '/schedule/groups'}>Groups</button>
            <button onclick={() => goto('/schedule/bracket')} class:active={page.url.pathname === '/schedule/bracket'}>Bracket</button>
            <button onclick={() => goto('/schedule/matches')} class:active={page.url.pathname === '/schedule/matches'}>Matches</button>
        </div>

        {@render children()}
    </div>
</div>