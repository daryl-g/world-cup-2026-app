<script lang="ts">
    // Custom components
    import GroupCard from '$lib/components/GroupCard.svelte';

    // Static types
    type Tab = 'groups' | 'bracket' | 'matches';
    let activeTab: Tab = $state<Tab>('groups');
</script>
<style>
    .schedule-container {
        background-image: url('$lib/assets/img/page_bg.png');
        background-size: cover;
        background-position: center;
        min-height: 91.8vh;
        max-height: 91.8vh;
    }

    .schedule-content {
        padding: 2rem;
        color: white;
    }

    .schedule-tabs {
        display: flex;
        gap: 0.5rem;
        margin-bottom: 0.5rem;
        justify-content: center;
    }

    .schedule-tabs button {
        background: rgba(255, 255, 255, 0.2);
        border: none;
        padding: 0.5rem 1.25rem;
        color: black;
        cursor: pointer;
        transition: background 0.3s;
    }

    .schedule-tabs button.active,
    .schedule-tabs button:hover {
        background: rgba(255, 255, 255, 0.4);
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
            <div class="schedule-groups">
                <div class="groups-grid">
                    {#each groups as group (index)}
                        <GroupCard id={group.id} name={group.name} teams={group.teams} />
                    {/each}
                </div>
            </div>
        {:else if activeTab === 'bracket'}
            <p>Bracket content goes here...</p>
        {:else if activeTab === 'matches'}
            <p>Matches content goes here...</p>
        {/if}
    </div>
</div>