<script lang="ts">
    // Custom component
    import PlayerRow from '$lib/components/teams/PlayerRow.svelte';
    import MatchList from '$lib/components/schedule/MatchList.svelte';

    // Data
    let { data } = $props();
</script>

<style>
    .team-detailed-container {
        background-image: url('$lib/assets/img/page_bg.png');
        background-size: cover;
        background-position: center;
        min-height: 91.8vh;
        overflow: hidden;
    }

    .team-header {
        display: flex;
        flex-direction: row;
        gap: 1rem;
        align-items: center;
        margin-top: 2rem;
        padding: 0.5rem 2rem;
    }

    .team-header h1 {
        font-family: 'Inter', sans-serif;
        font-weight: 700;
        font-size: clamp(1.5rem, 2.5vw, 2.5rem);
        padding-top: 1rem;
    }

    .team-info {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 2rem;
        padding: 1rem 2rem;
    }

    .team-stats-fixtures {
        display: flex;
        flex-direction: column;
        gap: 1rem;
    }

    .team-squad, .team-stats, .team-fixtures {
        background-color: rgba(255, 255, 255, 0.4);
        border-radius: 10px;
        padding: 1rem;
    }
</style>

<div class="team-detailed-container">
    <div class="team-header" style="background-color: {data.team.primaryColor}; color: {data.team.textColor}">
        <img src={data.team.flag} alt="{data.team.shortName} flag" width=50 class="team-flag" />
        <h1>{data.team.fullName}</h1>
    </div>
    <div class="team-info">
        <div class="team-squad">
            {#each data.team.squad.players as player}
                <PlayerRow player={player} shirt={data.team.shirt} />
            {/each}
        </div>
        <div class="team-stats-fixtures">
            <div class="team-fixtures">
                <MatchList
                    matches={data.matches}
                    filter={'team'}
                    value={data.team.id}
                />
            </div>
            <div class="team-stats">
                <h3>Stats</h3>
            </div>
        </div>
    </div>
</div>