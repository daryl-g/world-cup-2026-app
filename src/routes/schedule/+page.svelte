<script lang="ts">
    // Custom components
    import GroupCard from '$lib/components/GroupCard.svelte';

    // Static types
    type Tab = 'groups' | 'bracket' | 'matches';
    let activeTab: Tab = $state<Tab>('groups');

    type Sort = 'date' | 'group' | 'round';
    let activeSort: Sort = $state<Sort>('date');

    // Data
    let { data } = $props();
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

    .groups-grid, .bracket-content, .matches-content {
        background: rgba(255, 255, 255, 0.5);
        border-radius: 0px 0px 10px 10px;
        width: 100%;
        height: 100%;
    }

    .groups-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        justify-items: center;
        padding-top: 2rem;
        padding-bottom: 0.5rem;
        gap: 1rem;
    }

    .matches-sort {
        display: flex;
        align-items: center;
        justify-content: center;
        color: black;
        gap: 0.5rem;
        padding: 1rem;
    }

    .matches-sort button {
        background: rgba(255, 255, 255);
        border: none;
        border-radius: 10px;
        padding: 0.5rem 1rem;
        color: black;
        font-family: 'Inter', sans-serif;
        font-size: 1rem;
        font-weight: bold;
        cursor: pointer;
        transition: background 0.3s;
    }
</style>
<div class="schedule-container">
    <div class="schedule-content">
        <div class="schedule-tabs">
            <button onclick={() => activeTab = 'groups'} class:active={activeTab === 'groups'}>Groups</button>
            <button onclick={() => activeTab = 'bracket'} class:active={activeTab === 'bracket'}>Bracket</button>
            <button onclick={() => activeTab = 'matches'} class:active={activeTab === 'matches'}>Matches</button>
        </div>

        {#if activeTab === 'groups'}
            <div class="groups-grid">
                {#each data.groups as group}
                    <GroupCard
                        id={group.id}
                        name={group.name}
                        primaryColor={group.primaryColor}
                        textColor={group.textColor}
                        teams={group.teams}
                    />
                {/each}
            </div>
        {:else if activeTab === 'bracket'}
            <div class="bracket-content">
                <p>Bracket content goes here...</p>
            </div>
        {:else if activeTab === 'matches'}
            <div class="matches-content">
                <div class="matches-sort">
                    <h3>Sort by:</h3>
                    <button onclick={() => activeSort = 'date'} class:active={activeSort === 'date'}>Date</button>
                    <button onclick={() => activeSort = 'group'} class:active={activeSort === 'group'}>Group</button>
                    <button onclick={() => activeSort = 'round'} class:active={activeSort === 'round'}>Round</button>
                </div>
            </div>
        {/if}
    </div>
</div>